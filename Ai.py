import whisper

model = whisper.load_model("base")      # Choose tiny, base, small, medium, large
result = model.transcribe("myfile.mp3")
print(result["text"])

audio = whisper.load_audio("file.mp3")
audio = whisper.pad_or_trim(audio)
mel = whisper.log_mel_spectrogram(audio).to(model.device)

_, probs = model.detect_language(mel)
print("Language:", max(probs, key=probs.get))

options = whisper.DecodingOptions(language="en")
result = whisper.decode(model, mel, options)
print(result.text)





def check_password():
    user_password = input("Enter your password: ")
    correct_password = "Jeevan"
    if user_password == correct_password:
        return True
    else:
        return False

if check_password():
    print("Access Granted")
else:
    print("Access Denied")
    exit()



name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address name: ")

users =[
    {"name":"Jeevan","age":20,"school":"St. Joseph's"}
]
print("Your details")
print(f"Name:{name}")
print(f"Age: {age}")
print(f"Address: {address}")





def greet():
    print(f"Good morning sir {name}")
    print(f"Should we be for school { address}")
greet()