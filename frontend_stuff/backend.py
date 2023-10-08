import assemblyai as aai
from secret_case import API_TOKEN
from deep_translator import GoogleTranslator

def translate_audio_to_language():
    # Initialize the AssemblyAI API
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


    return translated
