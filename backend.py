import assemblyai as aai
from secret_case import API_TOKEN
from deep_translator import GoogleTranslator

aai.settings.api_key = API_TOKEN

FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

# IF X IS TRUE: summarizer

params = {
    "context": "There was a fire",
    "answer_format": "Bullet points"
}

result = transcript.lemur.summarize(**params)

to_translate = result.response

translated = GoogleTranslator(source='auto', target='zh-CN').translate(to_translate)


# Read
"""
with open("output.html", "r", encoding="utf-8") as file:
    html_content = file.read()
"""


# Replace 
"""
html_content = html_content.replace("%TRANSLATED_TEXT%", translated)
"""


# Write
"""
with open("output.html", "w", encoding="utf-8") as file:
    file.write(html_content)
"""

