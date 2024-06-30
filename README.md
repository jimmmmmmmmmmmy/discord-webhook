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

# Initialize the webhook with your Discord webhook URL
webhook = DiscordWebhook("YOUR_WEBHOOK_URL_HERE")

# Send a simple message
webhook.send_message("Hello, Discord!")

# Send a message with a custom username
webhook.send_message("Custom username message", username="Custom Bot")

# Send a message with an embed
embed = {
    "description": "This is an embed",
    "title": "Embed Title"
}
webhook.send_message("Message with embed", embeds=[embed])

# Send a message with a file attachment
webhook.send_message("Message with file", file_path="path/to/your/file.png")

# Send a message with a resized image
webhook.send_message("Resized image", file_path="path/to/your/image.png", file_size=(300, 200))

# Send a message with everything
webhook.send_message("Full featured message",
                     username="Full Feature Bot",
                     embeds=[embed],
                     file_path="path/to/your/image.png")
                     
```
