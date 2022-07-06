import os
import random
import time
import tkinter
from tkinter import *
print('Программа работает только на windows')
def start(): 
    try:
        from vosk import Model, KaldiRecognizer 
        import speech_recognition  
        import pyttsx3  
        import wave  
        import json 
        import os  
        import random
        import time
        class VoiceAssistant:
            """
            Настройки голосового ассистента, включающие имя, пол, язык речи
            """
            name = ""
            sex = ""
            speech_language = ""
            recognition_language = ""


        def setup_assistant_voice():
            voices = ttsEngine.getProperty("voices")

            if assistant.speech_language == "en":
                assistant.recognition_language = "en-US"
                if assistant.sex == "man":
                    ttsEngine.setProperty("voice", voices[1].id)
                else:
                    ttsEngine.setProperty("voice", voices[2].id)
            else:
                assistant.recognition_language = "ru-RU"
                ttsEngine.setProperty("voice", voices[0].id)


        def play_voice_assistant_speech(text_to_speech):
            """
            Проигрывание речи ответов голосового ассистента (без сохранения аудио)
            :param text_to_speech: текст, который нужно преобразовать в речь
            """
            ttsEngine.say(str(text_to_speech))
            ttsEngine.runAndWait()


        def record_and_recognize_audio(*args: tuple):
            """
            Запись и распознавание аудио
            """
            with microphone:
                recognized_data = ""
                recognizer.adjust_for_ambient_noise(microphone, duration=2)

                try:
                    print("Говорите...")
                    audio = recognizer.listen(microphone, 5, 5)

                    with open("microphone-results.wav", "wb") as file:
                        file.write(audio.get_wav_data())

                except speech_recognition.WaitTimeoutError:
                    print("Error")
                    return
                try:
                    print("Распознавание")
                    recognized_data = recognizer.recognize_google(audio, language="ru").lower()

                except speech_recognition.UnknownValueError:
                    pass
                except speech_recognition.RequestError:
                    print("РаспознаванПопытка использовать офлайн-распознавание...")
                    recognized_data = use_offline_recognition()

                return recognized_data
        def record_and_recognize_audio2(*args: tuple):
            """
            Запись и распознавание аудио
            """
            with microphone:
                recognized_data = ""
                recognizer.adjust_for_ambient_noise(microphone, duration=2)

                try:
                    print("Говорите...")
                    audio = recognizer.listen(microphone, 5, 5)

                    with open("microphone-find.wav", "wb") as file:
                        file.write(audio.get_wav_data())

                except speech_recognition.WaitTimeoutError:
                    print("Error")
                    return
                try:
                    print("Распознавание")
                    recognized_data2 = recognizer.recognize_google(audio, language="ru").lower()

                except speech_recognition.UnknownValueError:
                    pass
                except speech_recognition.RequestError:
                    print("РаспознаванПопытка использовать офлайн-распознавание...")
                    recognized_data2 = use_offline_recognition()

                return recognized_data2

        def use_offline_recognition():
            recognized_data = ""
            try:
                if not os.path.exists("models/vosk-model-small-ru-0.4"):
                    print("Please download the model from:\n"
                          "https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
                    exit(1)
                wave_audio_file = wave.open("microphone-results.wav", "rb")
                model = Model("models/vosk-model-small-ru-0.4")
                offline_recognizer = KaldiRecognizer(model, wave_audio_file.getframerate())

                data = wave_audio_file.readframes(wave_audio_file.getnframes())
                if len(data) > 0 and offline_recognizer.AcceptWaveform(data):
                    recognized_data = offline_recognizer.Result()
                    recognized_data = json.loads(recognized_data)
                    recognized_data = recognized_data["text"]
            except Exception:
                print("Sorry, speech service is unavailable. Try again later")

            return recognized_data

        if __name__ == "__main__":
            recognizer = speech_recognition.Recognizer()
            microphone = speech_recognition.Microphone()
            ttsEngine = pyttsx3.init()
            assistant = VoiceAssistant()
            assistant.name = "Karl"
            assistant.sex = "man"
            assistant.speech_language = "ua"
            setup_assistant_voice()
            while True:
                voice_input = record_and_recognize_audio()
                os.remove("microphone-results.wav")
                print(voice_input)
                voice_input = voice_input.split(" ")
                try:
                    command = voice_input[0] + voice_input[1] + voice_input[2]+ voice_input[3]
                except:
                    try:
                        command = voice_input[0] + voice_input[1] + voice_input[2]
                    except:
                        try:
                            command = f'{voice_input[0]}{voice_input[1]}'
                        except:
                            command = voice_input[0]
                if 'привет' == command:
                    play_voice_assistant_speech('Привет, я `Элис')
                elif 'откройgoogle' == command:
                    play_voice_assistant_speech('Открываю гугл')
                    import webbrowser
                    webbrowser.open('https://www.google.com')
                    time.sleep(0.2)
                    play_voice_assistant_speech('Готово')
                elif 'поискgoogle' == command:
                    play_voice_assistant_speech('Что вы хотите найти в гугл?')
                    voice_find = record_and_recognize_audio2()
                    os.remove("microphone-find.wav")
                    play_voice_assistant_speech(f'Поиск:{voice_find}')
                    find = voice_find
                    import webbrowser
                    webbrowser.open(f'https://www.google.com/search?q={find}&source=hp&ei=XbXBYvnbB5P-sAf5obrAAg&iflsig=AJiK0e8AAAAAYsHDbdl9QtXo7QQ_VdhIZlSHC1TugnZL&ved=0ahUKEwi5_pCNhN34AhUTP-wKHfmQDigQ4dUDCAY&uact=5&oq=котики&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEIAEELEDMgsIABCABBCxAxCDATIFCAAQgAQyCAguEIAEENQCMggILhCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOggILhCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6CwguEIAEELEDEIMBOgsILhCABBCxAxDUAjoFCC4QgAQ6CAgAELEDEIMBSgUIOxIBMVDHBVihDWCREGgAcAB4AIABgwGIAbsEkgEDNS4ymAEAoAEBsAEA&sclient=gws-wiz')
                elif 'поисквикипедия' == command:
                    play_voice_assistant_speech('Что вы хотите найти в википедии?')
                    voice_find = record_and_recognize_audio2()
                    os.remove("microphone-find.wav")
                    play_voice_assistant_speech(f'Поиск:{voice_find}')
                    find = voice_find
                    import webbrowser
                    webbrowser.open(f'https://ru.wikipedia.org/wiki/{find}')
                elif 'поискstackoverflow' == command:
                    play_voice_assistant_speech('Что вы хотите найти в stackowerflow?')
                    voice_find = record_and_recognize_audio2()
                    os.remove("microphone-find.wav")
                    play_voice_assistant_speech(f'Поиск:{voice_find}')
                    find = voice_find
                    import webbrowser
                    webbrowser.open(f'https://ru.stackoverflow.com/search?q={find}')
                elif 'отключись' == command:
                    play_voice_assistant_speech('Отключаюсь')
                    os.system("TASKKILL /F /IM python.exe")
                elif 'скольковремени' == command:
                    import datetime
                    from datetime import datetime
                    m = datetime.now()
                    n = str(m)
                    if n[12] != 0:
                        house1 = n[11]
                        hource2 = n[12]
                        hource = str(house1) + str(hource2)
                        if n[14] != 0:
                            minute1 = n[14]
                            minute2 = n[15]
                            minute = str(minute1) + str(minute2)
                        else:
                            minute = n[15]
                    else:
                        hource2 = n[12]
                        hource = n[12]
                    print(n)
                    play_voice_assistant_speech('Сейчас' + str(hource) + 'час,' + str(minute) + 'минут.')
                elif '' == command:
                    print('\r')
                elif 'элис' == command or 'эй' == command:
                    play_voice_assistant_speech('Шоо')
                elif 'утебяестьпитомец' in command:
                    play_voice_assistant_speech('У меня есть виртуальный кот Боб. Мяу')
                elif 'программа' == command:
                    play_voice_assistant_speech('какую программу вы хотите запустить?')
                    voice_find = record_and_recognize_audio2()
                    os.remove("microphone-find.wav")
                    play_voice_assistant_speech(f'Открываю:{voice_find}')
                    find = voice_find
                    h = os.listdir('C:/Users/ilyas/OneDrive/Рабочий стол')
                    if f'{find.title()}.lnk' in h:
                        os.system('"C:/Users/ilyas/OneDrive/Рабочий стол/' + find + '.lnk"')
                    elif f'{find.title()}.url' in h:
                        os.system('"C:/Users/ilyas/OneDrive/Рабочий стол/' + find + '.url"')
                    elif f'{find.title()}.exe' in h:
                        os.system('"C:/Users/ilyas/OneDrive/Рабочий стол/' + find + '.exe"')
                    else:
                        play_voice_assistant_speech('Я не нашла такой программы на рабочем столе')
                        start()
                elif 'ктоты' == command:
                    play_voice_assistant_speech('Я Э`лис, я друг OK google и Siry, а мой заклятый враг яндэкс Алиса')
                elif 'ктотебясоздал' == command:
                    play_voice_assistant_speech('меня создал крутой человек, сказать честно, по началу я думала он недаумок, но он опровергнул мои ожидания')
                elif 'изкакойтыстраны' == command:
                    play_voice_assistant_speech('Я из украи`ны, слава украи`не')
                else:
                    play_voice_assistant_speech('Простите, я не понимаю')
    except:
        start()
start()