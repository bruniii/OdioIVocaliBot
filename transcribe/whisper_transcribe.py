import whisper

MODEL = whisper.load_model("small", in_memory=True)

def transcribe_file(file) -> str:
    result = MODEL.transcribe(file, fp16=False, ) #, language="it", task='translate'
    return result["text"].rstrip('.')

if __name__ == "__main__":
    import os
    audio_path = os.path.join(os.path.dirname(__file__), "test_ita.oga")

    testo = transcribe_file(audio_path)
    print(testo)