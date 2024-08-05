"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyCJ6HSWVu_IcFVgc8ZGGqDd9RVCLGJB5yk")  #os.environ["GEMINI_API_KEY"]

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

# TODO Make these files available on the local file system
# You may need to update the file paths
# audio_drive0 = upload_to_gemini("Recorded Audio May 20, 2024 - 12:13AM.ogg", mime_type="audio/ogg")

while True:
    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "Hello\n",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hello! 👋  What can I do for you today? 😊 \n",
        ],
        }, ]
    )

    inputMsg = input("You: ")
    response = chat_session.send_message(inputMsg)

    print("Gemini: ",response.text)
    print("=========================================================================================================")
#print(chat_session.history)