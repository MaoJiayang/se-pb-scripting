"""
sync-pb-api.py — 将 malforge/malforge.github.io 的 input/pb 类型文档同步到 skill references/pb-api/
该脚本用于更新/下载 PB API 相关的 Markdown 文档
用法：
    python sync-pb-api.py          # 首次运行自动 clone，后续自动 pull 更新
    python sync-pb-api.py --force  # 强制重新复制所有文件，忽略时间戳比较

源仓库会被 sparse-checkout 到本脚本旁的 .cache/malforge/ 目录（已加入 .gitignore）。
只克隆 input/pb/ 子目录，避免 Windows 长路径问题。
"""

import argparse
import fnmatch
import os
import shutil
import subprocess
import sys

REMOTE_URL = "https://github.com/malforge/malforge.github.io"
SPARSE_PATHS = ["input/pb", "input/mod"]  # 需要的子目录

# 只复制这些命名空间的类型级文件（不含 @ 成员文件），来源：input/pb/
NAMESPACE_PATTERNS = [
    "Sandbox.ModAPI.Ingame.*.md",
    "SpaceEngineers.Game.ModAPI.Ingame.*.md",
    "VRageMath.*.md",
]

# 需要从其他目录单独复制的文件，格式：(相对缓存根的源路径, 目标文件名)
SINGLE_FILES = [
    ("input/mod/List-Of-Terminal-Properties-And-Actions.md", "List-Of-Terminal-Properties-And-Actions.md"),
]

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.normpath(os.path.join(SCRIPT_DIR, ".."))
CACHE_DIR = os.path.join(REPO_ROOT, ".cache", "malforge")
DEST_DIR = os.path.normpath(os.path.join(REPO_ROOT, "references", "pb-api"))


def sanitize_filename(name):
    """清理发布包校验不接受的文件名字符。"""
    return name.replace("+", "-").replace("{", "_").replace("}", "_")


def remove_stale_unsanitized_file(name, dst_path):
    """删除清理命名后遗留的旧原名文件。"""
    stale_path = os.path.join(DEST_DIR, name)
    if stale_path != dst_path and os.path.exists(stale_path):
        os.remove(stale_path)


def run(args, cwd=None, check=True):
    """运行子进程，出错时打印命令并退出。"""
    result = subprocess.run(args, cwd=cwd)
    if check and result.returncode != 0:
        print(f"错误：命令失败（退出码 {result.returncode}）：{' '.join(args)}", file=sys.stderr)
        sys.exit(result.returncode)
    return result


def ensure_clone():
    """首次运行时 sparse-clone 源仓库，已存在则执行 git pull。"""
    git_dir = os.path.join(CACHE_DIR, ".git")

    if not os.path.isdir(git_dir):
        print(f"首次运行，正在 sparse-clone {REMOTE_URL} ...")
        os.makedirs(CACHE_DIR, exist_ok=True)
        run(["git", "clone", "--no-checkout", "--filter=blob:none", REMOTE_URL, "."], cwd=CACHE_DIR)
        run(["git", "sparse-checkout", "init", "--cone"], cwd=CACHE_DIR)
        run(["git", "sparse-checkout", "set"] + SPARSE_PATHS, cwd=CACHE_DIR)
        run(["git", "checkout"], cwd=CACHE_DIR)
        print("Clone 完成。")
    else:
        print(f"正在更新缓存（git pull）...")
        result = run(["git", "pull"], cwd=CACHE_DIR, check=False)
        if result.returncode != 0:
            print("警告：git pull 失败，将使用本地现有缓存继续。", file=sys.stderr)


def sync_files(force: bool):
    """将 .cache/malforge/input/pb/ 中的类型级文件同步到 pb-api/ 目录。"""
    src = os.path.join(CACHE_DIR, "input", "pb")
    if not os.path.isdir(src):
        print(f"错误：缓存中找不到 {src}，clone 可能失败。", file=sys.stderr)
        sys.exit(1)

    os.makedirs(DEST_DIR, exist_ok=True)

    copied = 0
    skipped = 0
    all_files = os.listdir(src)

    for pattern in NAMESPACE_PATTERNS:
        for name in all_files:
            if "@" in name:
                continue  # 跳过成员级文件（IMyThrust@ThrustOverride.md 之类）
            if not fnmatch.fnmatch(name, pattern):
                continue

            src_path = os.path.join(src, name)
            dst_path = os.path.join(DEST_DIR, sanitize_filename(name))

            if not os.path.isfile(src_path):
                continue

            if not force:
                src_mtime = os.path.getmtime(src_path)
                dst_mtime = os.path.getmtime(dst_path) if os.path.exists(dst_path) else 0
                if src_mtime <= dst_mtime:
                    remove_stale_unsanitized_file(name, dst_path)
                    skipped += 1
                    continue

            shutil.copy2(src_path, dst_path)
            remove_stale_unsanitized_file(name, dst_path)
            copied += 1

    # 单独复制指定文件（来自 input/mod/ 等其他目录）
    for rel_src, dest_name in SINGLE_FILES:
        src_path = os.path.join(CACHE_DIR, rel_src.replace("/", os.sep))
        dst_path = os.path.join(DEST_DIR, sanitize_filename(dest_name))
        if not os.path.isfile(src_path):
            print(f"警告：找不到单文件源 {src_path}，跳过。", file=sys.stderr)
            continue
        if not force:
            src_mtime = os.path.getmtime(src_path)
            dst_mtime = os.path.getmtime(dst_path) if os.path.exists(dst_path) else 0
            if src_mtime <= dst_mtime:
                remove_stale_unsanitized_file(dest_name, dst_path)
                skipped += 1
                continue
        shutil.copy2(src_path, dst_path)
        remove_stale_unsanitized_file(dest_name, dst_path)
        copied += 1

    print()
    print("同步完成。")
    print(f"  已复制/更新：{copied} 个文件")
    print(f"  已跳过（未变更）：{skipped} 个文件")
    print(f"  目标目录：{DEST_DIR}")


def main():
    parser = argparse.ArgumentParser(
        description="自动 clone/更新 malforge PB API 文档并同步到 skill references/pb-api/"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="强制重新复制所有文件，忽略时间戳比较",
    )
    args = parser.parse_args()

    ensure_clone()
    sync_files(force=args.force)


if __name__ == "__main__":
    main()
