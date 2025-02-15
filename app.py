from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def index():
    interpretation = None
    image_url = None
    if request.method == "POST":
        dream = request.form.get("dream")
        if dream:
            try:
                # Generate a Jungian interpretation using the chat API.
                # Using the function call openai.chat.completions.create (note the lowercase 'chat.completions')
                text_response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a Jungian analyst. Interpret the following dream using Carl Jung’s psychological theories. "
                                "Focus on archetypes, the collective unconscious, and individuation. Provide a symbolic analysis that reveals insights into the dream's hidden meanings."
                            )
                        },
                        {"role": "user", "content": dream}
                    ],
                    temperature=0.8,
                    max_tokens=200
                )
                interpretation = text_response.choices[0].message.content.strip()
                
                # Generate an image using the DALL·E endpoint.
                image_response = openai.Image.create(
                    prompt=f"A symbolic and surreal visual representation of a dream: {dream}",
                    n=1,
                    size="512x512"
                )
                image_url = image_response['data'][0]['url']
            except Exception as e:
                interpretation = f"Error: {str(e)}"
    return render_template("index.html", interpretation=interpretation, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
