import streamlit as st
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_prompts(filepath="prompts.json"):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        st.error("Configuration file 'prompts.json' not found.")
        return {}

def main():
    st.set_page_config(page_title="Smart NLP Assistant", page_icon="🧠", layout="centered")
    
    st.title("🧠 Smart NLP Assistant")
    st.markdown("Build with **Google Gemini AI**. Enter some text below to summarize, analyze sentiment, or extract key entities!")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "YOUR_API_KEY_HERE":
        st.warning("⚠️ API Key is missing! Please make sure your .env file has your real GEMINI_API_KEY.")
        return

    genai.configure(api_key=api_key)
    
    try:
        model = genai.GenerativeModel('gemini-3.5-flash')
    except Exception as e:
        st.error(f"Failed to initialize Gemini model: {e}")
        return

    prompts = load_prompts()

    # Create the UI layout
    task = st.selectbox(
        "What would you like the AI to do?",
        ("Summarize Document", "Analyze Sentiment", "Extract Entities")
    )
    
    user_input = st.text_area("Enter your text here:", height=200, placeholder="Paste a paragraph or document here...")

    if st.button("Run AI Analysis ✨"):
        if not user_input.strip():
            st.warning("Please enter some text to analyze.")
            return
            
        with st.spinner("The AI is thinking..."):
            prompt_template = ""
            if task == "Summarize Document":
                prompt_template = prompts.get("summarization_prompt", "")
            elif task == "Analyze Sentiment":
                prompt_template = prompts.get("sentiment_analysis_prompt", "")
            elif task == "Extract Entities":
                prompt_template = prompts.get("entity_extraction_prompt", "")
                
            final_prompt = prompt_template.replace("{text}", user_input)
            
            try:
                response = model.generate_content(final_prompt)
                st.success("Analysis Complete!")
                
                st.markdown("### Result:")
                st.info(response.text)
            except Exception as e:
                st.error(f"An error occurred during generation: {e}")

if __name__ == "__main__":
    main()
