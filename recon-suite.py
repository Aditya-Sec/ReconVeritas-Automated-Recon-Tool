#!/usr/bin/env python3

import os
import subprocess
import argparse
from datetime import datetime

def run_command(command, output_file=None):
    try:
        print(f"[+] Running: {command}")
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        if output_file:
            with open(output_file, 'w') as f:
                f.write(result)
        return result
    except subprocess.CalledProcessError as e:
        if output_file:
            with open(output_file, 'w') as f:
                f.write(e.output)
        return e.output

def setup_output_dir(target):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    directory = f"recon_results_{target}_{now}"
    os.makedirs(directory, exist_ok=True)
    return directory

def recon(target):
    output_dir = setup_output_dir(target)

    # Nmap
    nmap_output = os.path.join(output_dir, "nmap.txt")
    run_command(f"nmap -sS -Pn -T4 {target}", nmap_output)

    # WhatWeb
    whatweb_output = os.path.join(output_dir, "whatweb.txt")
    run_command(f"whatweb {target}", whatweb_output)

    # Dirsearch
    dirsearch_output = os.path.join(output_dir, "dirsearch.txt")
    run_command(f"python3 dirsearch/dirsearch.py -u {target} -e php,html,js,txt -o {dirsearch_output}", dirsearch_output)

    # Sublist3r
    sublist3r_output = os.path.join(output_dir, "sublist3r.txt")
    run_command(f"python3 Sublist3r/sublist3r.py -d {target}", sublist3r_output)

    # Nuclei
    nuclei_output = os.path.join(output_dir, "nuclei.txt")
    run_command(f"nuclei -u {target} -silent", nuclei_output)

    # WAFW00F
    waf_output = os.path.join(output_dir, "wafw00f.txt")
    run_command(f"wafw00f {target}", waf_output)

    # DNSRecon
    dnsrecon_output = os.path.join(output_dir, "dnsrecon.txt")
    run_command(f"dnsrecon -d {target}", dnsrecon_output)

    # SSLScan
    sslscan_output = os.path.join(output_dir, "sslscan.txt")
    run_command(f"sslscan {target}", sslscan_output)

    print(f"[✔] Recon complete. Reports saved to: {output_dir}")

def main():
    parser = argparse.ArgumentParser(description="ReconVeritas - Automated Recon Suite")
    parser.add_argument("-t", "--target", help="Target domain or IP", required=True)
    args = parser.parse_args()
    recon(args.target)

if __name__ == "__main__":
    main()
