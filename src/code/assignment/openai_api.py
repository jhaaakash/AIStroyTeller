import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class OpenAIAPI:
    """
    A class to handle interactions with the OpenAI API.
    """

    def __init__(self):
        """
        Initialize the OpenAI API client.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")

        # Simplified initialization without extra parameters
        self.client = OpenAI(api_key=self.api_key)

    def generate_story(self, model_name, prompt, max_tokens=1000, temperature=0.7):
        """
        Generate a story using OpenAI's model.

        Args:
            model_name (str): The name of the model to use.
            prompt (str): The prompt to generate from.
            max_tokens (int): Maximum number of tokens to generate.
            temperature (float): Controls randomness in output.

        Returns:
            dict: The response from the API.
        """
        try:
            response = self.client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "system", "content": "You are a creative storyteller."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )

            return {
                "results": [{"generated_text": response.choices[0].message.content}]
            }

        except Exception as e:
            print(f"Error making request to OpenAI API: {e}")
            return {"error": str(e)}

    def create_story_prompt(
        self, genre, num_characters, character_names, num_paragraphs
    ):
        """
        Create a prompt for story generation based on user inputs.

        Args:
            genre (str): The genre of the story.
            num_characters (int): Number of characters.
            character_names (list): List of character names if provided.
            num_paragraphs (int): Number of paragraphs requested.

        Returns:
            str: The formatted prompt for the story generation.
        """
        character_str = ""
        if character_names and len(character_names) > 0:
            character_str = f"with characters named {', '.join(character_names)}"
        else:
            character_str = f"with {num_characters} characters"

        prompt = f"""
        Write an engaging {genre} story {character_str}. 
        The story should have exactly {num_paragraphs} paragraphs.
        Make the story creative and captivating, with a clear beginning, middle, and end.
        Each paragraph should flow naturally from one to the next.
        """

        return prompt.strip()
