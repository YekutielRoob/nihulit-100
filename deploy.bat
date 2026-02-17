@echo off
REM This script deploys to firebase using gcloud SDK

REM Set environment
set PROJECT_ID=nihulit-100
set BUCKET_NAME=nihulit-100.firebasestorage.app

REM Authenticate with gcloud
echo Authenticating with Google Cloud...
gcloud auth login

REM Set project
gcloud config set project %PROJECT_ID%

REM Deploy using gcloud deploy
echo Deploying to Firebase Hosting...
gcloud firebase hosting:channel:deploy main --source . --message "Deploy from local"

echo.
echo ✅ Done! Your site is at: https://nihulit-100.web.app
pause
