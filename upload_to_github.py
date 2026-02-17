import os
import requests
import base64
from pathlib import Path

# GitHub info
GITHUB_USERNAME = "YekutielRoob"
REPO_NAME = "nihulit-100"
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN"  # אתה צריך ליצור Personal Access Token

# Directory to upload
SOURCE_DIR = r"d:\Users\user\Desktop\code\n100"

# Files to ignore
IGNORE = ['.git', '.gitignore', 'node_modules', '.firebaserc', 'deploy.py', 'deploy.js', 'deploy.bat']

def upload_file(filepath, file_content):
    """Upload file to GitHub"""
    
    relative_path = os.path.relpath(filepath, SOURCE_DIR)
    file_path_in_repo = relative_path.replace('\\', '/')
    
    # Encode content
    encoded_content = base64.b64encode(file_content.encode()).decode()
    
    # GitHub API URL
    url = f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}/contents/{file_path_in_repo}"
    
    # Prepare data
    data = {
        "message": f"Add {file_path_in_repo}",
        "content": encoded_content,
        "branch": "main"
    }
    
    # Headers
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    # Upload
    response = requests.put(url, json=data, headers=headers)
    
    if response.status_code == 201:
        print(f"✅ Uploaded: {file_path_in_repo}")
    elif response.status_code == 422:
        print(f"⏳ Already exists: {file_path_in_repo}")
    else:
        print(f"❌ Error uploading {file_path_in_repo}: {response.status_code}")
        print(response.json())

def main():
    print("🚀 Starting upload to GitHub...")
    
    # Scan directory
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Remove ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE]
        
        for file in files:
            # Skip ignored files
            if any(file.endswith(ig) or file.startswith(ig) for ig in IGNORE):
                continue
            
            filepath = os.path.join(root, file)
            
            # Read file
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                upload_file(filepath, content)
            except Exception as e:
                print(f"❌ Error processing {filepath}: {e}")
    
    print("\n✅ Upload complete!")

if __name__ == "__main__":
    if GITHUB_TOKEN == "YOUR_GITHUB_TOKEN":
        print("❌ Error: Please set your GitHub token first!")
        print("\nTo get a token:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Create new Personal Access Token")
        print("3. Check 'repo' permission")
        print("4. Copy the token and replace 'YOUR_GITHUB_TOKEN' in this script")
    else:
        main()
