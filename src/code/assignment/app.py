from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
from .openai_api import OpenAIAPI

# Get the directory where static files are stored
static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
app = Flask(__name__, static_folder=static_folder)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Initialize the OpenAI API client
openai_client = OpenAIAPI()


@app.route("/api/generate-story", methods=["POST"])
def generate_story():
    """
    API endpoint to generate a story based on user inputs.
    """
    try:
        data = request.json

        # Extract parameters with defaults
        genre = data.get("genre", "comedy")
        num_characters = data.get("num_characters", 3)
        character_names = data.get("character_names", [])
        num_paragraphs = data.get("num_paragraphs", 4)
        model = data.get("model", "gpt-3.5-turbo")

        # Create the prompt
        prompt = openai_client.create_story_prompt(
            genre, num_characters, character_names, num_paragraphs
        )

        # Generate the story
        response = openai_client.generate_story(
            model_name=model,
            prompt=prompt,
            max_tokens=1500,  # Adjust based on expected story length
            temperature=0.8,  # Higher temperature for more creative stories
        )

        # Check for errors in the response
        if "error" in response:
            return jsonify({"success": False, "error": response["error"]}), 500

        # Extract the generated text from the response
        story = response["results"][0]["generated_text"]

        return jsonify({"success": True, "story": story, "prompt": prompt})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/models", methods=["GET"])
def get_available_models():
    """
    API endpoint to get a list of available OpenAI models.
    """
    models = [
        {
            "id": "gpt-3.5-turbo",
            "name": "GPT-3.5 Turbo",
            "description": "OpenAI's efficient and cost-effective model",
        },
        {
            "id": "gpt-4-turbo",
            "name": "GPT-4 Turbo",
            "description": "OpenAI's most powerful model for complex tasks",
        },
    ]

    return jsonify({"success": True, "models": models})


@app.route("/")
def index():
    """
    Serve the main HTML page.
    """
    return send_from_directory(static_folder, "index.html")


if __name__ == "__main__":
    app.run(debug=True)
