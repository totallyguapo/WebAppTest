from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load the API key

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_url = None  # To store the image URL
    if request.method == "POST":
        prompt = request.form["prompt"]
        
        try:
            # Generate Jungian-based interpretation using GPT-3
               response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Use GPT model for generating interpretations
                messages=[
                    {"role": "system", "content": "You are a psychoanalyst trained in Jungian psychology. Your task is to interpret dreams, considering archetypes, symbols, and the unconscious mind. Use Carl Jung's theories to offer insights into the dream."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=150
            )
            
            # Extract the interpretation from the response
            result = interpretation_response['choices'][0]['message']['content'].strip()

            # Now, use the interpretation to generate an image with DALL·E
            image_response = openai.Image.create(
                prompt=result,  # Use the Jungian interpretation as the prompt for the image
                n=1,  # Generate one image
                size="1024x1024"  # Image size
            )
            
            # Get the URL of the generated image
            image_url = image_response['data'][0]['url']

        except Exception as e:
            result = f"Error: {str(e)}"
    
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
