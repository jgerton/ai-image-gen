import openai
from dotenv import load_dotenv
import os
#import json
#from pathlib import Path
#from datetime import datetime
import urllib.request

def init():
    load_dotenv()
    # Test that the API key exists
    if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
        print("OPENAI_API_KEY is not set")
        exit(1)

def main():
    init()

    #DATA_DIR = Path.cwd() / "responses"
    #DATA_DIR.mkdir(exist_ok=True)

    PROMPT = "High quality, wide shot, DSLR, futuristic photo of an astronaut riding a horse on the surface of the moon with planets in the sky"
    NMBR_OF_IMGS = 3
    IMG_SIZE = "512x512"
    B64_RESPONSE_FORMAT = "b64_json"
    URL_RESPONSE_FORMAT = "url"
    response = openai.Image.create(
        prompt = PROMPT,
        n = NMBR_OF_IMGS,
        size = IMG_SIZE,
        response_format = URL_RESPONSE_FORMAT
    )

    # save the images locally
    if "data" in response:
        for key, obj in enumerate(response["data"]):
            filename ='my_image_'+str(key)+".jpg"
            urllib.request.urlretrieve(obj['url'], filename)
        print('Images have been downloaded and saved locally')
    else:
        print("Failed to generate image")

if __name__ == '__main__':
    main()
