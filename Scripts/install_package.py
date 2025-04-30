import os
import requests
from requests.auth import HTTPBasicAuth
import yaml

def load_config():
    try:
        with open(os.path.join(os.path.dirname(__file__), "../Configuration/config.yaml"), 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def download_installer():
    config = load_config()
    if not config:
        return

    machine_config = config["package_details"]
    url, path, username, password, name = (machine_config[key] for key in
        ["package_install_url", "download_path", "gsa_username", "gsa_password", "package_name"])
    output_path = os.path.join(path, name)

    print(f"📥 Downloading from: {url}\n📁 Saving to: {output_path}")

    try:
        response = requests.get(url, stream=True, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            os.makedirs(path, exist_ok=True)
            total_size = int(response.headers.get('content-length', 0))
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        print(f"\rDownloading... {100 * (f.tell() / total_size):.2f}% complete", end='')
            print("\n Download complete.")
        else:
            print(f"Failed to download. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    download_installer()
