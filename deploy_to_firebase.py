#!/usr/bin/env python3
"""
פשוט - עלייה ישירה לFirebase Hosting
"""

import os
import subprocess
import sys

PROJECT_ID = "nihulit-100"
SOURCE_DIR = r"d:\Users\user\Desktop\code\n100"

# שינוי לתיקיית הפרויקט
os.chdir(SOURCE_DIR)

print("🚀 Starting Firebase deployment...")
print(f"📁 Project: {PROJECT_ID}")
print(f"📂 Source: {SOURCE_DIR}")

# בדוק אם firebase.json קיים
if not os.path.exists("firebase.json"):
    print("❌ firebase.json not found!")
    sys.exit(1)

print("✅ firebase.json found")

# ננסה עם gcloud
try:
    print("\n📤 Deploying with gcloud...")
    result = subprocess.run([
        "gcloud", "firebase", "hosting:channel:deploy", "main",
        "--project", PROJECT_ID
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
    
    if result.returncode == 0:
        print("\n✅ Deployment successful!")
        print(f"🌐 Your site: https://{PROJECT_ID}.web.app")
    else:
        print("\n❌ Deployment failed - trying alternative method...")
        # ננסה firebase deploy בישירות
        result2 = subprocess.run([
            "firebase", "deploy", "--project", PROJECT_ID
        ], capture_output=True, text=True)
        
        print(result2.stdout)
        if result2.stderr:
            print("Errors:", result2.stderr)

except FileNotFoundError:
    print("❌ gcloud or firebase not found. Installing...")
    os.system("npm install -g firebase-tools")

print("\n" + "="*50)
print("✅ Done!")
print("="*50)
