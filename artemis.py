import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Inicializar el reconocimiento de voz
recognizer = sr.Recognizer()

# Función para escuchar y responder
def voice_assistant():
    with sr.Microphone() as source:
        print("Di algo...")
        audio = recognizer.listen(source)

    try:
        # Reconocer el comando de voz
        command = recognizer.recognize_google(audio)
        print("Comando: " + command)

        # Generar respuesta de audio
        response_text = "Has dicho: " + command
        response_audio = gTTS(text=response_text, lang="es")
        response_audio.save("response.mp3")

        # Reproducir la respuesta de audio
        response_sound = AudioSegment.from_mp3("response.mp3")
        play(response_sound)

    except sr.UnknownValueError:
        print("No se pudo entender el comando.")
    except sr.RequestError:
        print("No se pudo completar la solicitud de reconocimiento de voz.")

if __name__ == "__main__":
    voice_assistant()
