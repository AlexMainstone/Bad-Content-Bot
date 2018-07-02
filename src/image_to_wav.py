import pytesseract
from PIL import Image
import tts.sapi
import os

def processImage(opendir):
    image = Image.open("../tmp/posts/"+opendir)

    #IMAGE PROCESSING

    text = pytesseract.image_to_string(image)
    voice = tts.sapi.Sapi()

    processed_text = ""
    for line in text.split('\n'):
        #TEXT PROCESSING
        for c in line:
            if c == '>':
                line += ', ,'
        processed_text += line

    if not os.path.isdir("../tmp/tts"):
        os.mkdir("../tmp/tts")
    
    voice.create_recording("../tmp/tts/"+opendir+".wav", processed_text)
    
    
    
