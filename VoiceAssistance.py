import datetime
import webbrowser

def voice_assistant():
    print("Voice Assistant Ready! (type 'exit' to quit)")
    while True:
        command = input("You: ").lower()

        if "hello" in command:
            print("Assistant: Hello! How can I help you?")
        elif "time" in command:
            now = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Assistant: The current time is {now}")
        elif "date" in command:
            today = datetime.date.today()
            print(f"Assistant: Today's date is {today}")
        elif "google" in command:
            print("Assistant: Opening Google...")
            webbrowser.open("https://www.google.com")
        elif "exit" in command:
            print("Assistant: Goodbye!")
            break
        else:
            print("Assistant: Sorry, I didn't understand that.")

voice_assistant()