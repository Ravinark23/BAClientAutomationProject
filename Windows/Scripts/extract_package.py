import os
import subprocess
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def extract_installer():
    config = load_config()
    if not config:
        return

    package = config["package_details"]
    exe_file = os.path.join(package['download_path'], package['package_name'])
    exe_dir = package['download_path']
    seven_zip = "7z"

    try:
        print(f"📂 Extracting {exe_file} to {exe_dir}...")
        process = subprocess.Popen([seven_zip, 'x', exe_file, f'-o{exe_dir}', '-y'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        for line in process.stdout:
            if "Extracting" in line:
                print(line.strip())

        process.wait()
        print(f"\n Extraction complete. Files are in: {exe_dir}")

    except Exception as e:
        print(f" Error: {e}")

if __name__ == "__main__":
    extract_installer()
