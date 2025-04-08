# Streamlit AI Agent

This project is a Streamlit application that serves as a chat interface for an AI agent capable of generating content. The AI agent can respond to user inputs by calling various content generation functions.

## Project Structure

```
streamlit-ai-agent
├── src
│   ├── main.py               # Entry point of the Streamlit application
│   ├── agent.py              # Contains the AIAgent class for handling responses
│   ├── functions             # Package for content generation functions
│   │   ├── __init__.py       # Initializes the functions package
│   │   ├── content_generator.py # Functions for generating articles and summaries
│   │   └── utils.py          # Utility functions for text formatting and validation
│   └── config.py             # Configuration settings for the application
├── requirements.txt          # Project dependencies
├── .env.example              # Template for environment variables
└── README.md                 # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/streamlit-ai-agent.git
   cd streamlit-ai-agent
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Copy the `.env.example` file to `.env` and fill in the necessary values for your API keys and configuration settings.

5. **Run the application:**
   ```
   streamlit run src/main.py
   ```

## Usage

Once the application is running, you will be able to interact with the AI agent through the chat interface. You can ask the agent to generate articles or summaries based on your input.

## AI Agent Capabilities

- **Content Generation:** The AI agent can generate articles and summaries using the functions defined in `src/functions/content_generator.py`.
- **User Interaction:** The chat interface allows for real-time interaction with the AI agent, making it easy to request and receive content.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.