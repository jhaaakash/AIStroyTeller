import os
from src.code.assignment.app import app

if __name__ == "__main__":
    # Get the port from the environment variable or use the default port 5000
    port = int(os.environ.get("PORT", 5000))

    # Start the Flask application
    app.run(host="0.0.0.0", port=port, debug=True)
