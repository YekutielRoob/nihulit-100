#!/usr/bin/env node
/**
 * Firebase Hosting Deploy
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const PROJECT_ID = 'nihulit-100';
const SOURCE_DIR = 'd:\\Users\\user\\Desktop\\code\\n100';

console.log('🚀 Firebase Hosting Deployment');
console.log(`📁 Project: ${PROJECT_ID}`);
console.log(`📂 Source: ${SOURCE_DIR}`);

// Change to project directory
process.chdir(SOURCE_DIR);

// Check firebase.json
if (!fs.existsSync('firebase.json')) {
    console.log('❌ firebase.json not found!');
    process.exit(1);
}

console.log('✅ firebase.json found');
console.log('📤 Attempting deployment...\n');

try {
    // Try firebase deploy
    const cmd = `firebase deploy --project ${PROJECT_ID} --non-interactive`;
    console.log(`Running: ${cmd}\n`);
    
    execSync(cmd, {
        cwd: SOURCE_DIR,
        stdio: 'inherit'
    });
    
    console.log('\n✅ Deployment successful!');
    console.log(`🌐 Your site is live at: https://${PROJECT_ID}.web.app`);
} catch (error) {
    console.log('\n❌ Deployment failed');
    console.log('Error:', error.message);
    console.log('\nTrying with token environment variable...');
    
    // Try alternative
    try {
        const cmd2 = `firebase deploy --project ${PROJECT_ID} --token "%FIREBASE_TOKEN%"`;
        execSync(cmd2, { stdio: 'inherit' });
    } catch (e) {
        console.log('\n⚠️  Firebase authentication required');
        console.log('Please run: firebase login');
    }
}

