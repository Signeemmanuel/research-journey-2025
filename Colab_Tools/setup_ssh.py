
import os
import subprocess
import sys

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def main():
    print("🔑 INITIALIZING SSH ENVIRONMENT...")
    
    # Paths
    drive_key = "/content/drive/MyDrive/ssh_keys/github_key"
    root_ssh = "/root/.ssh"
    
    # 1. Create .ssh dir
    if not os.path.exists(root_ssh):
        os.makedirs(root_ssh)
    
    # 2. Copy Key
    if not os.path.exists(drive_key):
        print(f"❌ Error: SSH Key not found at {drive_key}")
        return
        
    run(f'cp "{drive_key}" "{root_ssh}/id_ed25519"')
    run(f'chmod 600 "{root_ssh}/id_ed25519"')
    
    # 3. Add GitHub to Known Hosts
    print("🌐 Scanning GitHub keys...")
    run(f'ssh-keyscan -t ed25519 github.com >> "{root_ssh}/known_hosts"')
    
    # 4. Configure Git Identity
    print("👤 Configuring Git Global Identity...")
    run(f'git config --global user.email "signeemmanuel28@gmail.com"')
    run(f'git config --global user.name "Josue Emmanuel Signe"')
    
    # 5. Test Connection
    print("Testing connection...")
    try:
        subprocess.run("ssh -T git@github.com", shell=True, check=True)
    except subprocess.CalledProcessError as e:
        # GitHub returns exit code 1 on success for this specific command text, so we ignore it
        pass
    print("✅ SSH Setup Complete.")

if __name__ == "__main__":
    main()
