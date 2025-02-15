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
    image_url = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "developer", "content": "You are a jungian analyst. Interpret the following fream using Jung's psychological theories. Focus on archetypes, the collective unconscious, and individuation. Provide a symbolic analysis that reveals insights into the dreams hidden meanings."}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.2,
                          max_completion_tokens=50
            )
            result = response.choices[0].message.content
            # Generate an image using the DALL·E endpoint.
            image_response = openai.images.generate(
                    prompt=f"A symbolic and surreal visual representation of a dream: {prompt}",
                model = "dall-e-3"  
                )
            image_url = image_response['data'][0]['url']
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
