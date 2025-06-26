#!/bin/bash

echo "🔧 Starting Recon Automation Suite installation..."

# Update and install required system tools
echo "📦 Installing system dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install -y nmap whatweb wafw00f dnsrecon sslscan git python3-pip

# Clone required tools
echo "📁 Cloning supporting tools..."

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
  cd tools/nuclei
  sudo apt install -y golang
  go install
  cd ../..
fi

# Install Python dependencies
echo "🐍 Installing Python packages..."
pip3 install -r requirements.txt

# Make recon script executable
chmod +x recon-suite.py

echo "✅ Installation complete!"
echo "Run the tool using: python3 recon-suite.py -t example.com"
