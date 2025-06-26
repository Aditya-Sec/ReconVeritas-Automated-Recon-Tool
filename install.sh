#!/bin/bash

echo "🔧 Starting ReconVeritas installation..."

# Step 1: Update & install system tools
echo "📦 Installing required system packages..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y nmap whatweb wafw00f dnsrecon sslscan git python3-pip

# Step 2: Clone external tools into tools/ directory
echo "📁 Cloning required recon tools..."

mkdir -p tools

# Dirsearch
if [ ! -d "tools/dirsearch" ]; then
  git clone https://github.com/maurosoria/dirsearch.git tools/dirsearch
fi

# Sublist3r
if [ ! -d "tools/Sublist3r" ]; then
  git clone https://github.com/aboul3la/Sublist3r.git tools/Sublist3r
fi

# Nuclei
if [ ! -d "tools/nuclei" ]; then
  git clone https://github.com/projectdiscovery/nuclei.git tools/nuclei
  echo "⚙️ Installing Go (for nuclei)..."
  sudo apt install -y golang
  cd tools/nuclei
  go install
  cd ../../
fi

# Step 3: Python dependencies
echo "🐍 Installing Python packages..."
pip3 install -r requirements.txt

# Step 4: Make main script executable
chmod +x recon-suite.py

echo "✅ Installation complete!"
echo "👉 Run the tool using: python3 recon-suite.py -t example.com"
