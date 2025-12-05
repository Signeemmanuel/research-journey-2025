
import os
import shutil
import subprocess

REPO_URL = "git@github.com:Signeemmanuel/research-journey-2025.git"
TARGET_DIR = "/content/drive/MyDrive/Research-Journey-2025"

def main():
    print(f"📦 MANAGING REPOSITORY: {TARGET_DIR}")
    
    # 1. Check for Broken Repo (Folder exists but no .git)
    if os.path.exists(TARGET_DIR) and not os.path.exists(os.path.join(TARGET_DIR, ".git")):
        print("⚠️  Found broken directory (missing .git). Deleting...")
        shutil.rmtree(TARGET_DIR)
        
    # 2. Clone or Pull
    if not os.path.exists(TARGET_DIR):
        print("⬇️  Cloning repository...")
        subprocess.run(f'git clone {REPO_URL} "{TARGET_DIR}"', shell=True, check=True)
    else:
        print("🔄 Repository exists. Pulling latest changes...")
        os.chdir(TARGET_DIR)
        subprocess.run("git pull", shell=True, check=True)
        
    print("✅ Repository is ready.")

if __name__ == "__main__":
    main()
