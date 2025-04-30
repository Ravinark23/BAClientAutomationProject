import platform
import os

def print_os_details():
    print("Operating System Details:")
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Environment Variables (Partial): {os.environ.get('OS')}")

if __name__ == "__main__":
    print_os_details()
