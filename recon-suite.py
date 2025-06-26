#!/usr/bin/env python3

import os
import argparse
import datetime
import shutil

# 🏗️ Create output directory
def create_output_dir(target):
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    folder_name = f"results/{target}_{timestamp}"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name

# 🚀 Run command if tool/folder exists
def run_tool(tool_name, command, output_path, is_script=False, folder_check=None):
    if is_script:
        if not os.path.isdir(folder_check):
            print(f"❌ Folder missing: {folder_check}")
            print(f"👉 Clone it: git clone {folder_check}")
            return
    elif shutil.which(tool_name) is None:
        print(f"❌ Tool not found: {tool_name}")
        print(f"👉 Install it using your package manager.")
        return

    print(f"🔧 Running {tool_name}...")
    os.system(f"{command} > {output_path}")
    print(f"✅ Output saved: {output_path}")

# 🎯 Main Function
def main():
    parser = argparse.ArgumentParser(description="ReconVeritas – Automated Recon Suite")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP")
    args = parser.parse_args()

    target = args.target
    out_dir = create_output_dir(target)
    print(f"\n📁 Saving results to: {out_dir}\n")

    # List of tool runs
    tools = [
        {
            "name": "nmap",
            "cmd": f"nmap -sC -sV -Pn {target}",
            "out": f"{out_dir}/nmap.txt",
        },
        {
            "name": "whatweb",
            "cmd": f"whatweb {target}",
            "out": f"{out_dir}/whatweb.txt",
        },
        {
            "name": "wafw00f",
            "cmd": f"wafw00f {target}",
            "out": f"{out_dir}/wafw00f.txt",
        },
        {
            "name": "dnsrecon",
            "cmd": f"dnsrecon -d {target}",
            "out": f"{out_dir}/dnsrecon.txt",
        },
        {
            "name": "sslscan",
            "cmd": f"sslscan {target}",
            "out": f"{out_dir}/sslscan.txt",
        },
        {
            "name": "nuclei",
            "cmd": f"nuclei -u {target}",
            "out": f"{out_dir}/nuclei.txt",
        },
        {
            "name": "sublist3r",
            "cmd": f"python3 Sublist3r/sublist3r.py -d {target}",
            "out": f"{out_dir}/sublist3r.txt",
            "is_script": True,
            "folder": "Sublist3r"
        },
        {
            "name": "dirsearch",
            "cmd": f"python3 dirsearch/dirsearch.py -u http://{target}",
            "out": f"{out_dir}/dirsearch.txt",
            "is_script": True,
            "folder": "dirsearch"
        },
    ]

    # Execute tools
    for tool in tools:
        run_tool(
            tool_name=tool["name"],
            command=tool["cmd"],
            output_path=tool["out"],
            is_script=tool.get("is_script", False),
            folder_check=tool.get("folder", None)
        )

    print("\n✅ Recon Complete! Check the results folder.\n")

if __name__ == "__main__":
    main()



