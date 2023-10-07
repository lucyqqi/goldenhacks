import assemblyai as aai
from secret_case import API_TOKEN

transcriber = aai.Transcriber(API_TOKEN)
transcript = transcriber.transcribe("https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3")

print(transcript.text)

params = {
    "context": "There was a fire",
    "answer_format": "Bullet points"
}

result = transcript.lemur.summarize(**params)

print(result.response)

to_translate = result.response
translated = GoogleTranslator(source='auto', target='fr').translate(to_translate)
print(translated)