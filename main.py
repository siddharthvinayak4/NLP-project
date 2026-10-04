import os
import json
import argparse
import google.generativeai as genai
from dotenv import load_dotenv

def load_prompts(filepath="prompts.json"):
    with open(filepath, 'r') as file:
        return json.load(file)

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Configure Gemini API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables. Please check your .env file.")
        return
    
    genai.configure(api_key=api_key)
    
    # Initialize the generative model
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        print(f"Failed to initialize Gemini model: {e}")
        return
    
    prompts = load_prompts()

    parser = argparse.ArgumentParser(description="A Natural Language Processing CLI tool powered by Gemini API.")
    parser.add_argument("task", choices=["summarize", "sentiment", "entities"], help="The NLP task to perform.")
    parser.add_argument("text", help="The text to analyze, or path to a text file.")
    
    args = parser.parse_args()
    
    # Determine if text is a file path or raw text
    input_text = args.text
    if os.path.exists(args.text):
        try:
            with open(args.text, 'r', encoding='utf-8') as f:
                input_text = f.read()
        except Exception as e:
            print(f"Error reading file '{args.text}': {e}")
            return
        
    prompt_template = ""
    if args.task == "summarize":
        prompt_template = prompts["summarization_prompt"]
    elif args.task == "sentiment":
        prompt_template = prompts["sentiment_analysis_prompt"]
    elif args.task == "entities":
        prompt_template = prompts["entity_extraction_prompt"]
        
    final_prompt = prompt_template.replace("{text}", input_text)
    
    print(f"Running '{args.task}' task...")
    try:
        response = model.generate_content(final_prompt)
        print("\n--- Result ---\n")
        print(response.text)
        print("\n--------------\n")
    except Exception as e:
        print(f"An error occurred during API request: {e}")

if __name__ == "__main__":
    main()
