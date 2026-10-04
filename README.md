# Gemini-Powered NLP CLI Tool

This project is a Natural Language Processing (NLP) command-line interface (CLI) tool that integrates with the Google Gemini API to perform several text analysis tasks.

## Features

- **Summarization**: Generates concise summaries of long texts or documents.
- **Sentiment Analysis**: Evaluates the sentiment of a given text (positive, negative, neutral) and provides reasoning.
- **Entity Extraction**: Identifies and extracts key entities such as people, organizations, locations, and dates from the text.

## Project Structure

- `main.py`: The core source code containing the Python CLI application.
- `prompts.json`: A configuration file holding the prompt templates used for interacting with the LLM.
- `.env`: A configuration file that holds the environment variables (like the `GEMINI_API_KEY`).
- `requirements.txt`: The required Python dependencies.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/siddharthvinayak4/NLP-project.git
   cd NLP-project
   ```

2. **Install dependencies**:
   Make sure you have Python 3.9+ installed. Run the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**:
   The project uses a `.env` file to manage the API key. The repository includes this configuration file initialized with the provided Gemini API key. If the API key expires, simply update the `GEMINI_API_KEY` variable in the `.env` file.

## Usage

You can pass either raw text or a path to a text file as the input argument.

```bash
python main.py <task> "<text_or_file_path>"
```

### Examples

**1. Summarization**
```bash
python main.py summarize "Artificial intelligence is a field of computer science..."
```
Alternatively, with a file:
```bash
python main.py summarize data.txt
```

**2. Sentiment Analysis**
```bash
python main.py sentiment "I am incredibly happy with the results of this project!"
```

**3. Entity Extraction**
```bash
python main.py entities "Google is headquartered in Mountain View, California."
```

## Technologies Used
- Python 3
- [Google Generative AI SDK](https://github.com/google/generative-ai-python)
- `python-dotenv` for configuration management