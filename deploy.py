import os
import json
import subprocess
import sys

# Change to the project directory
os.chdir(r"d:\Users\user\Desktop\code\n100")

# Set the project
os.environ['GCLOUD_PROJECT'] = 'nihulit-100'

# Run firebase deploy
try:
    result = subprocess.run([
        sys.executable, '-m', 'pip', 'install', '--upgrade', 'firebase-admin'
    ], capture_output=True, text=True)
    
    print("Firebase Admin SDK installed")
    
    # Now attempt deploy using firebase CLI
    result = subprocess.run([
        'firebase', 'deploy', '--project', 'nihulit-100', '--token', os.environ.get('FIREBASE_TOKEN', '')
    ], capture_output=True, text=True)
    
    print(result.stdout)
    if result.stderr:
        print("Errors:", result.stderr)
        
except Exception as e:
    print(f"Error: {e}")
