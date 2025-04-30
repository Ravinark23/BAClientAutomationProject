import os
import yaml

def load_config():
    try:
        with open(os.path.join(os.path.dirname(__file__), "/Users/ravina/PycharmProjects/BAClientAutomationProject/Configuration/config.yaml"), 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return None
