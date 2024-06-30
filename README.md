# DiscordWebhookPlus: Enhanced Discord Webhook Sender

DiscordWebhookPlus is a Python class that provides an easy-to-use interface for sending messages, embeds, and files to Discord channels via webhooks. It offers additional features like custom usernames and image resizing.

## Features

- Send simple text messages
- Add custom usernames to messages
- Include embeds in your messages
- Attach files to your messages
- Resize images before sending (requires PIL)
- Error handling for file operations and HTTP requests

## Requirements

- Python 3.6+
- `requests` library

## Installation

1. Clone this repository or download the `discord_webhook.py` file.
2. Install the required libraries:

```
pip install requests
```

## Usage

Here's a quick example of how to use DiscordWebhookPlus:

```python
from discord_webhook import DiscordWebhook

webhook_url = "__test_webhook_url__"
webhook = DiscordWebhook(webhook_url)

# Simple message
webhook.send_message("Hello, Discord!")

# Message with custom username
webhook.send_message("Custom username message", username="Custom Username")

# Message with embed
embed = {
    "description": "This is testing an embed",
    "title": "Test title"
}
webhook.send_message("Test message with embed", embeds=[embed])

# Message with file
webhook.send_message("Test message with image", file_path ="new "
                                                           "project.png")

# Message with everything
webhook.send_message("Full featured test message",
                     username="Full Feature Test Bot",
                     embeds=[embed],
                     file_path="new project.png")
```

![Screenshot 2024-06-29 at 9 44 01 PM](https://github.com/jimmmmmmmmmmmy/discord-webhook/assets/143036559/54a0ea94-397c-49bc-a15a-3e26d9f65f87)

