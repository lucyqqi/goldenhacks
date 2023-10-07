import assemblyai as aai
from secret_case import API_TOKEN
from deep_translator import GoogleTranslator

aai.settings.api_key = API_TOKEN

FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL)

# IF X IS TRUE: basic summarry 
"""
params = {
    "context": "There was a fire",
    "answer_format": "Bullet points"
    result = transcript.lemur.summarize(**params)
}
"""

# IF Y IS TRUE: Translate to selected language
"""

to_translate = result.response

translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)

"""

# IF Z IS TRUE: basic transcription
"""

return transcript

"""


