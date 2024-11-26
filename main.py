from flask import Flask, request, jsonify
import json
import requests
app = Flask(__name__)

class ConfigManager:
    @staticmethod
    def load_config(config_path='config.json'):
        try:
            with open(config_path, 'r') as config_file:
                return json.load(config_file)
        except FileNotFoundError:
            default_config = {
                "paste_ee_api_key": "enter ur paste_ee api key",
                "default_syntax": "text",
                "default_description": "Pasted Text"
            }
            ConfigManager.save_config(default_config, config_path)
            return default_config
        except json.JSONDecodeError:
            return {
                "paste_ee_api_key": "uwXMcT9hnAffi8trfpsqJ5rwiW4wlOrvF0i7nOKNW",
                "default_syntax": "text",
                "default_description": "Pasted Text"
            }

    @staticmethod
    def save_config(config, config_path='config.json'):
        with open(config_path, 'w') as config_file:
            json.dump(config, config_file, indent=4)

class PasteEeUploader:
    def __init__(self, api_key):
        self.base_url = "https://api.paste.ee/v1/pastes"
        self.api_key = api_key
        self.headers = {
            "Content-Type": "application/json",
            "X-Authentication": self.api_key
        }

    def create_paste(self, text, description="Pasted Text", syntax="text"):
        if not self.api_key:
            return {"error": "No API key provided."}

        payload = {
            "key": self.api_key,
            "description": description,
            "sections": [
                {
                    "name": description,
                    "syntax": syntax,
                    "contents": text
                }
            ]
        }

        try:
            response = requests.post(
                self.base_url,
                json=payload,
                headers=self.headers
            )

            response_data = response.json()

            if response.status_code in [200, 201] and response_data.get('success'):
                return {"link": response_data.get('link')}
            else:
                return {"error": "Failed to create paste.", "details": response_data}

        except Exception as e:
            return {"error": str(e)}

@app.route('/create_paste', methods=['POST'])
def create_paste():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    text = data.get('text', '')
    description = data.get('description', 'Pasted Text')
    syntax = data.get('syntax', 'text')

    config = ConfigManager.load_config()
    api_key = config.get('paste_ee_api_key')

    uploader = PasteEeUploader(api_key)
    result = uploader.create_paste(text, description, syntax)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
