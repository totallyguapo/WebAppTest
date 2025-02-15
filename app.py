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
                #developer sets how bot should behave. at head of the chain of command for the bot
                messages=[{"role": "developer", "content": '''Taking a user prompt as a dream, output only your interpretation of the dream. Be very concise and surreal.
                Remember that a dream is a coherent message from the unconscious cloaked in symbolism. 
                When you interpret the dream and arrive at an interpretation that “clicks” or makes you say “a-ha,” then you’re on the right path. A couple of caveats:
                the unconscious will not send a message that you already know or are conscious of. Thus the dream’s message should be a surprise.
                If you arrive at a dream interpretation that is self-congratulatory and self-inflating, then that interpretation is probably incorrect.
                If you arrive at an interpretation that blames others, then that interpretation is also incorrect. Dreams are about you and not others. 
                Remember that all the characters in a dream represent aspects of the dreamer, even if they look like somebody familiar.''' }, 
                          {"role": "user", "content": prompt}],
                          temperature=1.7,
                          max_completion_tokens=50
            )
            result = response.choices[0].message.content
            # Generate an image using the DALL·E endpoint.
            image_response = openai.images.generate(
                    prompt=f"A symbolic and surreal visual representation of a dream: {prompt}",
                model = "dall-e-2"
                )
            image_url = image_response.data[0].url
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing
