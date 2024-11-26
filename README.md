# Paste.ee Uploader API

This is a simple Flask-based API that allows users to create pastes on Paste.ee using a provided API key. The API accepts text, description, and syntax as input, and returns a link to the created paste.

It is still under development, I will soon code the front_end page for this with some cool things, ( this is a side project for some stars nothing else )

## Features

- Create a paste using text input.
- Customizable description and syntax highlighting options.
- Returns a link to the created paste.

## API Endpoints

### `POST /create_paste`

This endpoint allows you to create a paste on Paste.ee.

#### Request Body

The request should be in JSON format with the following fields:

- **text** (required): The text content you want to paste.
- **description** (optional): A description for your paste (default: "Pasted Text").
- **syntax** (optional): Syntax highlighting for the paste (default: "text"). Available options include:
  - text, python, javascript, html, css, json, markdown, bash, cpp, java, php, sql

Example request:

```json
{
  "text": "Hello, this is a test paste from the API!",
  "description": "Test Paste",
  "syntax": "text"
}
```

Response
Success: Returns the link to the created paste.

Example Response:
```json
{
  "link": "https://paste.ee/p/abcd1234"
}
```

# Running the API Locally

### Config

The API uses a configuration file `config.json` If it doesn't exist, it will be created automatically with the following default values:
```json
{
  "paste_ee_api_key": "your-api-key-here",
  "default_syntax": "text",
  "default_description": "Pasted Text"
}
```
Replace "your-api-key-here" with your actual API key from Paste.ee.

### Running the API
1. Clone this repository:
```bash
git clone https://github.com/your-username/paste-ee-uploader.git
cd paste-ee-uploader
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the Flask app:
```bash
python main.py
```
4. The API will be available at `http://localhost:5001/create_paste`

# Support
If you encounter any issues or need help, feel free to reach out:

- Discord Server: https://discord.gg/ghouls
- Email: random@exril.xyz

# Licence 
- This project is licensed under the MIT License - see the LICENSE file for details.
