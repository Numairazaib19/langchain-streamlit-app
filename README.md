# langchain-streamlit-app

It is a Streamlit-based application that allows users to ask questions about uploaded images. Using advanced tools like image captioning and object detection, the app provides meaningful insights about the image. It leverages a conversational AI agent powered by Google's Gemini language model to understand and respond to user queries.

---

## Features

- **Image Upload:** Users can upload images in `.jpeg`, `.jpg`, or `.png` formats.
- **Conversational Interface:** Ask questions about the uploaded image in natural language.
- **Image Analysis Tools:** The app uses tools for:
  - Image captioning
  - Object detection
    
---

### Tools and Technologies
- **Streamlit:** For building the user interface.
- **LangChain:** To manage conversational agents and memory.
- **Google Gemini Model:** Used as the backend generative model for conversational AI.
- **Image Processing Tools:** Custom tools for image captioning and object detection.

---

## Requirements

### Prerequisites
1. Python 3.8 or above.
2. The following Python libraries:
   - `streamlit`
   - `langchain`
   - `langchain_google_genai`
   - Any additional dependencies for `tools.ImageCaptionTool` and `tools.ObjectDetectionTool`.

### Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the required dependencies
4. Set your Google API key as an environment variable
   ```bash
   export GOOGLE_API_KEY="your_google_api_key"
   ```

---

## Usage

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL provided by Streamlit

3. Upload an image and ask questions about it in the input box.

---



