import azure.cognitiveservices.speech as speechsdk

def from_file():
    speech_config = speechsdk.SpeechConfig(subscription="", region="westeurope")
    audio_input = speechsdk.AudioConfig(filename="sound.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input,language="tr-TR")
    
    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
 
from_file()