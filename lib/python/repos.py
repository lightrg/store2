import subprocess

def get_git_commit_history(repo_path):
    """
    Hàm này gọi lệnh git log để lấy danh sách commit id và commit message từ repository.
    Chúng ta không thêm dữ liệu mẫu trực tiếp trong code vì code này sẽ chạy trên repository thực tế của bạn.
    """
    # Lệnh git log sử dụng định dạng: commit hash và commit message
    cmd = ["git", "log", "--pretty=format:%H %s"]
    # Chạy lệnh trong thư mục repo (repo_path)
    result = subprocess.run(cmd, cwd=repo_path, capture_output=True, text=True)
    if result.returncode == 0:
        commits = result.stdout.strip().split("\n")
        return commits
    else:
        raise Exception("Lỗi khi gọi git log: " + result.stderr)
