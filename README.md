# ReconVeritas-Automated-Recon-Tool-
ReconVeritas is an advanced, fully automated reconnaissance framework built for red teamers, penetration testers, and security analysts. It consolidates top open-source recon tools into a single Python-driven pipeline, performing deep asset discovery, fingerprinting, WAF detection, and vulnerability scanning.


# 🧠 RedTeam Recon Suite 

An advanced, fully automated reconnaissance and attack surface mapping tool designed for Red Team operations. This suite leverages top open-source tools to perform passive and active recon, and generates a consolidated HTML report with risk scoring.


## 🔧 Included Tools & Modules

| Tool          | Purpose                                  |
|---------------|-------------------------------------------|
| `nmap`        | Port scanning + service/version detection |
| `whatweb`     | Web technology fingerprinting             |
| `sublist3r`   | Subdomain enumeration                     |
| `dirsearch`   | Hidden directories brute-force            |
| `dnsrecon`    | DNS record enumeration                    |
| `crt.sh`      | Passive subdomain discovery               |
| `httpx`       | Title/status/code/redirect checks         |
| `wafw00f`     | WAF vendor fingerprinting                 |
| `sslscan` / `testssl.sh` | TLS version/cipher testing     |
| `nuclei`      | Vulnerability template scanning           |

---

## 📁 Folder Structure

``bash
RedTeam-Recon-Suite/
├── recon-suite.py
├── README.md
├── requirements.txt
├── config/
│   └── wordlists/
├── logs/
│   ├── nmap.txt
│   ├── whatweb.txt
│   ├── subdomains.txt
│   ├── dirsearch.txt
│   ├── dnsrecon.txt
│   ├── waf.txt
│   ├── httpx.txt
│   ├── sslscan.txt
│   └── nuclei.txt
├── reports/
│   └── recon-[timestamp].html
├── utils/
│   └── generate_report.py
├── screenshots/

## 🚀 Usage

``bash
python3 recon-suite.py -t example.com
You can pass domains or IPs. The tool runs scans, stores logs, and generates a report.

💻 Installation
📦 Install Dependencies

sudo apt install nmap whatweb wafw00f dnsrecon sslscan
pip install -r requirements.txt

🔁 Clone Supporting Tools

git clone https://github.com/m4ll0k/dirsearch.git
git clone https://github.com/aboul3la/Sublist3r.git
git clone https://github.com/projectdiscovery/nuclei.git

🔐 Disclaimer
This tool is intended only for ethical hacking, educational, and authorized testing purposes.
⚠️ Do not use it against systems or domains you do not have explicit permission to assess.

🙋 About Me
I’m a Blue Teamer transitioning into Red Teaming, building practical offensive tools to understand how attackers think and operate.

🙋 Author: [Aditya Goswami](https://www.linkedin.com/in/aditya-kumar-goswami)  
🔗 GitHub: [Aditya-Sec](https://github.com/Aditya-Sec)

