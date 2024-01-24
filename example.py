import base64
import os
import requests
import json


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def generate(prompt, image_path=None):
    url = "http://localhost:8080/completion"
    headers = {"Content-Type": "application/json"}

    if image_path:
        encoded_image = encode_image(image_path)

    data = {
        "prompt": prompt,
        "n_predict": 100,
        "temperature": 0.7,
        "stream": True,
        "stop": [
            "<|im_end|>",
            "[/INST]",
            "USER:",
            "ASSISTANT:"
        ]
    }

    if image_path:
        data["image_data"] = [{"data": encoded_image, "id": 1}]

    full_response = ""  # Initialize an empty string to store the full response

    with requests.post(url, headers=headers, data=json.dumps(data), stream=True) as response:
        # print("Connected to model server, receiving stream...")
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')

                # Remove the 'data: ' prefix
                if decoded_line.startswith('data: '):
                    decoded_line = decoded_line.replace('data: ', '', 1)

                try:
                    response_json = json.loads(decoded_line)

                    # Check if the stream has ended
                    if response_json.get("stop"):
                        break

                    # Append the content to the full response
                    content = response_json.get("content", "")
                    full_response += content
                    # print('Received:', content)

                except json.JSONDecodeError:
                    print("Received non-JSON data:", decoded_line)
                    # Handle the non-JSON data as needed

    return full_response


prompt = '''USER:[img-1] What is it on the image?
ASSISTANT:
'''


response = generate(
    prompt,
    "/home/random/Documents/7.png"
)
print('Response:', response)
