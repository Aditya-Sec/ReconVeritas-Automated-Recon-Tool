#!/bin/bash

echo "🔧 Installing ReconVeritas Automated Recon Tool..."

# Step 1: Update & Install Dependencies
echo "📦 Installing required system packages..."
sudo apt update
sudo apt install -y nmap whatweb wafw00f dnsrecon sslscan python3 python3-pip

# Step 2: Install Python requirements
echo "🐍 Installing Python packages..."
pip3 install -r requirements.txt

# Step 3: Clone Required Tools if not already present
echo "📂 Cloning support tools (dirsearch, Sublist3r, nuclei)..."

[ ! -d "dirsearch" ] && git clone https://github.com/m4ll0k/dirsearch.git
[ ! -d "Sublist3r" ] && git clone https://github.com/aboul3la/Sublist3r.git
[ ! -d "nuclei" ] && git clone https://github.com/projectdiscovery/nuclei.git

# Step 4: Set Alias
echo "🔗 Creating alias 'reconveritas' for easy access..."
ALIAS_CMD="alias reconveritas='python3 $(pwd)/recon-suite.py -t'"

if ! grep -Fxq "$ALIAS_CMD" ~/.bashrc; then
  echo "$ALIAS_CMD" >> ~/.bashrc
  echo "✅ Alias added to ~/.bashrc"
else
  echo "✅ Alias already exists in ~/.bashrc"
fi

# Step 5: Final Instructions
echo "✅ Installation complete!"
echo "👉 Please run: source ~/.bashrc"
echo "👉 Now use the tool like this:"
echo ""
echo "   reconveritas example.com"
echo ""
