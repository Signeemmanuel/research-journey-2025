import os
import argparse
import subprocess
from datetime import datetime

# --- CONFIGURATION ---
REPO_PATH = "/content/drive/MyDrive/Research-Journey-2025"
EMAIL = "signeemmanuel28@gmail.com"
NAME = "Signe Josue Emmanuel"
BRANCH = "master"

def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.stderr}")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description="Automated Git Commit & Push for Colab")
    parser.add_argument("-m", "--message", type=str, help="Commit message", default=None)
    parser.add_argument("-f", "--file", type=str, help="Specific file to commit", default=".")
    args = parser.parse_args()

    # 1. Navigate to Repo
    if not os.path.exists(REPO_PATH):
        print(f"❌ Error: Repository path not found at {REPO_PATH}")
        exit(1)
    os.chdir(REPO_PATH)
    print(f"📂 Working in: {REPO_PATH}")

    # 2. Configure Git Identity (Ensures commits belong to you)
    run_command(f'git config --global user.email "{EMAIL}"')
    run_command(f'git config --global user.name "{NAME}"')

    # 3. Add Files
    print(f"➕ Adding files: {args.file}")
    run_command(f'git add "{args.file}"')

    # 4. Generate Message if not provided
    commit_msg = args.message
    if not commit_msg:
        commit_msg = f"Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"

    # 5. Commit
    print(f"📝 Committing with message: '{commit_msg}'")
    try:
        run_command(f'git commit -m "{commit_msg}"')
    except:
        print("⚠️ No changes to commit.")
        return

    # 6. Push
    print("🚀 Pushing to GitHub...")
    run_command(f'git push origin {BRANCH}')
    print("✅ Done!")

if __name__ == "__main__":
    main()
