import base64
from io import BytesIO
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os
from PIL import Image


class image_base64(BaseModel):
    img_base64: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def basetoimage(base):
    try:
        im_bytes = base64.b64decode(base)  # im_bytes is a binary image
        im_file = BytesIO(im_bytes)  # convert image to file-like object
        img = Image.open(im_file)
        return img, 1
    except:
        return None, 0


@app.post("/")
async def read_image(file: image_base64):
    base64img = file.img_base64
    image, flag = basetoimage(base64img)
    result = {"Result": "1"}
    # if flag == 1:
    #     idx = predict(model, image)
    #     result.update(fetch(idx))
    # else:
    #     result = {"Result": "Please Provide Correct Input"}

    return result
