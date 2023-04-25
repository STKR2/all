# Powered By Kanna & Kaal

import os
import re
import textwrap

import aiofiles
import aiohttp
import numpy as np
import random

from PIL import Image, ImageChops, ImageOps, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from youtubesearchpython.__future__ import VideosSearch

from Telugucoders.core.resource import colors



def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def add_corners(im):
    bigsize = (im.size[0] * 3, im.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(im.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, im.split()[-1])
    im.putalpha(mask)



async def generate_cover(requested_by, title, views, duration, thumbnail):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("cache/thumbx.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    border = random.choice(colors)
    image1 = Image.open("cache/thumbx.png")
    image2 = Image.open(f"Telugucoders/core/resource/amala.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image3.convert("RGBA")
    background = image5.filter(filter=ImageFilter.BoxBlur(30))
    enhancer = ImageEnhance.Brightness(background)
    background = enhancer.enhance(0.6)
    background.save("cache/blur_image.png")

    Xcenter = image3.width / 2
    Ycenter = image3.height / 2
    x1 = Xcenter - 250
    y1 = Ycenter - 250
    x2 = Xcenter + 250
    y2 = Ycenter + 250

    logo = image3.crop((x1, y1, x2, y2))
    logo.thumbnail((520, 520), Image.ANTIALIAS)
    logo.save(f"cache/temp.png")
    if not os.path.isfile(f"cache/circle.png"):
        im = Image.open(f"cache/temp.png").convert("RGBA")
        add_corners(im)
        im.save(f"cache/circle.png")

    image7 = Image.open(f"cache/circle.png")
    image8 = image7.convert("RGBA")
    image8.thumbnail((365, 365), Image.ANTIALIAS)
    width = int((1280 - 365) / 2)
    background = Image.open("cache/blur_image.png")
    background.paste(image8, (width + 2, 138), mask=image8)
    background.paste(image4, (0, 0), mask=image4)
    img = ImageOps.expand(background, border=10, fill=f"{border}")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Telugucoders/core/resource/font2.ttf", 45)
    ImageFont.truetype("Telugucoders/core/resource/font2.ttf", 70)
    arial = ImageFont.truetype("Telugucoders/core/resource/font2.ttf", 30)
    ImageFont.truetype("Telugucoders/core/resource/font.ttf", 30)

    para = textwrap.wrap(title, width=32)
    try:
        draw.text(
            (450, 35),
            f"STARTED PLAYING",
            fill="white",
            stroke_width=1,
            stroke_fill="white",
            font=font,
        )
        if para[0]:
            text_w, text_h = draw.textsize(f"{para[0]}", font=font)
            draw.text(
                ((1280 - text_w) / 2, 560),
                f"{para[0]}",
                fill="white",
                stroke_width=1,
                stroke_fill="white",
                font=font,
            )
        if para[1]:
            text_w, text_h = draw.textsize(f"{para[1]}", font=font)
            draw.text(
                ((1280 - text_w) / 2, 610),
                f"{para[1]}",
                fill="white",
                stroke_width=1,
                stroke_fill="white",
                font=font,
            )
    except:
        pass
    text_w, text_h = draw.textsize(f"Duration: {duration} Mins", font=arial)
    draw.text(
        ((1280 - text_w) / 2, 665),
        f"Duration: {duration} Mins",
        fill="white",
        font=arial,
    )
    try:
        os.remove(f"cache/temp.png")
        os.remove(f"cache/circle.png")
        os.remove(f"cache/temp_image.png")
        os.remove(f"background.png")
    except:
        pass
    img.save(f"final.png")
    final = f"final.png"
    return final
