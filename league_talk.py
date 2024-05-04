import time
from speech_recognition import Recognizer, Microphone, WaitTimeoutError, UnknownValueError
import keyboard

r = Recognizer()

with Microphone() as mic:
    while True:
        keyboard.wait('g')
        print('Listening...')
        try:
            audio = r.listen(mic, 1)
            text = r.recognize_google(audio)
        except (WaitTimeoutError, UnknownValueError):
            print('...no speech recognized')
            continue

        print(f'...recognized: "{text}"')
        keyboard.press_and_release('enter')
        time.sleep(0.01)
        keyboard.write(text)
