# who-is-it-today
Who’s up next? This GitHub Action picks a random teammate and pings them on Slack—perfect for standups, duties, or just for fun.

A GitHub Action that posts a scheduled message to Slack, tagging a random team member from a configurable list. Supports multiple teams via YAML config files and uses an incoming webhook to send messages.

## 🚀 Features

- **Random User Selection**: Picks a random user from a predefined list.
- **Scheduled Notifications**: Runs on a schedule using GitHub Actions.
- **Multiple Teams Support**: Configurable via YAML files for different teams.
- **Slack Integration**: Uses Slack incoming webhook to send messages.

## 🛠️ Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kaylanx/who-is-it-today.git
   cd who-is-it-today
   ```
2. Create a Config File: Create a YAML file (e.g., teams_config.yml) with your team configurations.

Add GitHub Secrets (if needed for webhook security):

Not required for public incoming webhooks, but you can store the config path or team name as secrets.

## ⚙️ Congiguration

Example teams_config.yml:

```yaml
engineering:
  slack_users:
    - U12345678
    - U23456789
  webhook_url: https://hooks.slack.com/services/ENG/WEBHOOK/URL
  message: "Hey {user}, you're up this week for the engineering update!"

design:
  slack_users:
    - U34567890
    - U45678901
  webhook_url: https://hooks.slack.com/services/DESIGN/WEBHOOK/URL
  message: "🎨 {user}, it's your turn to share design progress!"

```

## 📅 Usage

GitHub Actions Workflow

```yaml
name: Who Is It Today

on:
  schedule:
    - cron: '0 9 * * 1'  # Every Monday at 9 AM UTC
  workflow_dispatch:

jobs:
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests pyyaml

      - name: Run Who Is It Today
        run: python who_is_it_today.py engineering teams_config.yml

```

## 📄 License

MIT License. See LICENSE for details.
