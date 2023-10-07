import assemblyai as aai

transcriber = aai.Transcriber()
transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/gettysburg.wav")

print(transcript.text)