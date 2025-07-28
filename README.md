# AI Storytelling Application

This application allows users to generate personalized stories using OpenAI's LLMs (Large Language Models). Users can input parameters like genre, number of characters, character names, and number of paragraphs to get a customized story.

## Features

- User-friendly web interface for story generation
- Integration with OpenAI's powerful language models (GPT-3.5 Turbo and GPT-4 Turbo)
- Customizable story parameters (genre, characters, length)
- Responsive design that works on both desktop and mobile devices
- RESTful API endpoints for story generation and model selection

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation Steps

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd AssignmentModule3
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   - Create an account on OpenAI if you don't have one
   - Obtain your API key from your OpenAI account dashboard
   - Edit the `.env` file and replace the placeholder with your actual OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Running the Application

You can run the application using either of these methods:

1. Using the run script:
   ```bash
   python run.py
   ```

2. Or using the setup script which sets up the environment and dependencies:
   ```bash
   ./setup.sh
   python run.py
   ```

Then open your web browser and navigate to `http://localhost:5000`

## How to Use

1. Select a story genre from the dropdown menu (Action, Comedy, Sci-Fi, Mystery, etc.)
2. Enter the number of characters you want in your story (1-10)
3. (Optional) Add names for your characters
4. Choose the number of paragraphs for your story (1-10)
5. Select which OpenAI model to use (GPT-3.5 Turbo or GPT-4 Turbo)
6. Click "Generate Story" and wait for your personalized story to appear

## Project Structure

```
AssignmentModule3/
│
├── .env                  # Environment variables (OpenAI API key)
├── requirements.txt      # Python dependencies
├── run.py                # Application entry point
├── setup.sh              # Setup script for environment and dependencies
│
└── src/
    └── code/
        └── assignment/
            ├── __init__.py      # Package initialization
            ├── app.py           # Flask application and routes
            ├── openai_api.py    # OpenAI API integration
            │
            └── static/          # Frontend files
                └── index.html   # Main web interface
```

## API Endpoints

The application exposes the following REST API endpoints:

1. **Generate Story**
   - URL: `/api/generate-story`
   - Method: `POST`
   - Parameters:
     - `genre`: Type of story (action, comedy, sci-fi, etc.)
     - `num_characters`: Number of characters in the story
     - `character_names`: List of character names (optional)
     - `num_paragraphs`: Number of paragraphs to generate
     - `model`: OpenAI model to use (gpt-3.5-turbo or gpt-4-turbo)
   - Returns: JSON with generated story content

2. **Available Models**
   - URL: `/api/models`
   - Method: `GET`
   - Returns: List of available OpenAI models with IDs and descriptions

## Customization

You can modify the story generation by:

1. Editing the prompt template in `openai_api.py` to change how stories are structured
2. Adding more genres in the HTML interface (`static/index.html`)
3. Adjusting the generation parameters like temperature (creativity level) and max_tokens (story length)
4. Adding more OpenAI models in the `get_available_models()` function in `app.py`

## Dependencies

- Flask (2.3.3): Web framework for the application
- Requests (2.31.0): HTTP library for API calls
- python-dotenv (1.0.0): Environment variable management
- flask-cors (4.0.0): Cross-Origin Resource Sharing support
- openai (1.12.0): OpenAI API client
