import random
import requests
import yaml
import sys

def load_config(config_file, team_name):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config[team_name]

def notify_slack(team_name, config_file):
    # Load team configuration
    team_config = load_config(config_file, team_name)
    
    # Select a random user
    selected_user = random.choice(team_config['slack_users'])
    
    # Message to be sent
    message = team_config['message'].replace("{user}", f"<@{selected_user}>")
    
    # Slack webhook URL
    webhook_url = team_config['webhook_url']
    
    # Payload to be sent to Slack
    payload = {
        "text": message
    }
    
    # Send the message to Slack
    response = requests.post(webhook_url, json=payload)
    
    # Print the response from Slack
    print(f"Response: {response.status_code}, {response.text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python notify_slack.py <team_name> <config_file>")
        sys.exit(1)
    
    team_name = sys.argv[1]
    config_file = sys.argv[2]
    
    notify_slack(team_name, config_file)

