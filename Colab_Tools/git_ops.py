
import os
import argparse
import subprocess
from datetime import datetime

REPO_PATH = "/content/drive/MyDrive/Research-Journey-2025"

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Git Error: {e}")
        exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", type=str, default=None)
    parser.add_argument("-f", "--file", type=str, default=".")
    args = parser.parse_args()

    if not os.path.exists(REPO_PATH):
        print("❌ Error: Repository not found. Run manage_repo.py first.")
        exit(1)
        
    os.chdir(REPO_PATH)
    print(f"📂 Git Operations in: {REPO_PATH}")

    # Add
    run_command(f'git add "{args.file}"')

    # Commit
    msg = args.message if args.message else f"Auto-update: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    try:
        run_command(f'git commit -m "{msg}"')
        print(f"📝 Committed: {msg}")
    except:
        print("⚠️  Nothing to commit.")

    # Push
    print("🚀 Pushing...")
    run_command("git push origin main")
    print("✅ Success.")

if __name__ == "__main__":
    main()
