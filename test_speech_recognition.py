import speech_recognition as sr

r = sr.Recognizer()
m = sr.Microphone()

try:
    print("Please wait...")
    with m as source: r.adjust_for_ambient_noise(source)
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("I heard you...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            print("You said '{}'".format(value))
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
except KeyboardInterrupt:
    pass    