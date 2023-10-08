import assemblyai as aai
from secret_case import API_TOKEN
from deep_translator import GoogleTranslator

def translate_audio_to_language():
    # Initialize the AssemblyAI API
    aai.settings.api_key = API_TOKEN

    FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"
    FILE_URL2 = "https://github.com/Hashim-Khan0/mp3/blob/main/Emmanuel%20Macron's%20inauguration%20speech_%20France%20will%20always%20work%20on%20building%20long-term%20peace.mp3"

    transcriber = aai.Transcriber()
    transcriptC = transcriber.transcribe(FILE_URL)
    transcriptF = transcriber.transcribe(FILE_URL2)


    # IF X IS TRUE: summarizer

    paramsC = {
        "context": "There was a fire",
        "answer_format": "Bullet points"
    }

    paramsF = {
        "context": "President of France innaguration speech",
        "answer_format": "summarry"
    }

    resultC = transcriptC.lemur.summarize(**paramsC)
    resultF = transcriptF.lemur.summarize(**paramsF)

    to_translate = resultC.response
    to_translate2 = resultF.response

    translatedC = GoogleTranslator(source='auto', target='zh-CN').translate(to_translate)
    translatedF = GoogleTranslator(source='auto',target='en').translate(to_translate2)

    return translatedC, translatedF
