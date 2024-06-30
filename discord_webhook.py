import requests
import json
from typing import Optional, Dict, Any, List, Tuple

class DiscordWebhook:
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url

    def send_message(self, content: str, username: Optional[str] = None,
                     embeds: Optional[List[Dict[str, Any]]] = None,
                     file_path: Optional[str] = None,
                     file_size: Optional[Tuple[int, int]] = None) -> requests.Response:
        data = {"content": content}

        if username:
            data["username"] = username

        if embeds:
            data["embeds"] = embeds

        files = None
        if file_path:
            try:
                if file_size:
                    from PIL import Image
                    with Image.open(file_path) as img:
                        img = img.resize(file_size)
                        import io
                        img_byte_arr = io.BytesIO()
                        img.save(img_byte_arr, format=img.format)
                        img_byte_arr = img_byte_arr.getvalue()
                        files = {'file': (file_path, img_byte_arr)}
                else:
                    files = {'file': open(file_path, 'rb')}

                # When sending files, we need to send the JSON payload as a string in the 'payload_json' field
                response = requests.post(self.webhook_url,
                                         data={'payload_json': json.dumps(data)},
                                         files=files)
            except FileNotFoundError:
                print(f"Error: File not found - {file_path}")
                return None
            except ImportError:
                print("Error: PIL library not installed. Required for image resizing.")
                return None
            finally:
                if files and 'file' in files and hasattr(files['file'], 'close'):
                    files['file'].close()
        else:
            response = requests.post(self.webhook_url, json=data)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error: {err}")
        else:
            print(f"Payload delivered successfully, code {response.status_code}.")

        return response

# Example usage
if __name__ == "__main__":
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
