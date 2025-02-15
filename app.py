from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None  # To store the image URL
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            # Use ChatCompletion for text-based generation
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Use GPT-4 or GPT-3.5-turbo
                messages=[
                    {"role": "system", "content": "You are a psychedelic AI that speaks in Oulipian constraints. Your responses are short, surreal, and witty. Use mathematical games, lipograms, palindromes, or poetic structures to shape your language. Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."},
                    {"role": "user", "content": prompt}
                ],
                temperature=1.2,
                max_tokens=150
            )
            result = response['choices'][0]['message']['content'].strip()

            # Generate an image based on the text response using DALL·E
            image_response = openai.Image.create(
                prompt=result,  # Use the interpretation text as the image prompt
                n=1,  # Number of images to generate
                size="1024x1024"  # Image size
            )
            image_url = image_response['data'][0]['url']  # Get the URL of the generated image
        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
