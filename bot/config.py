#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", default=3847632, cast=int)
    API_HASH = config("API_HASH", default="1a9708f807ddd06b10337f2091c67657")
    BOT_TOKEN = config("BOT_TOKEN", default="5494056691:AAE8an9G9x90d9pUIf5gk5G_EwMIMEpq_To")
    DEV = 2020270268
    OWNER = config("OWNER", default="2020270268")
    FFMPEG = config(
    "FFMPEG",
    default=('ffmpeg -map 0:v:0 -map 0:a:? -map 0:s:? -map -0:t -c:v libx264 -vf "[0:v]drawtext=fontfile=font.ttf:text=\'ANIMESPECTRUM\':fontsize=15:fontcolor=white:bordercolor=black:borderw=7:x=w-text_w-15:y=15,drawtext=fontfile=font.ttf:text=\'ANIMESPECTRUM\':fontsize=15:fontcolor=black:bordercolor=white:borderw=7:x=w-text_w-15:y=15",scale=846x480,format=yuv420p,smartblur=ls=-0.9:lt=-20 -crf 28 -preset veryfast -x264-params no-info=1 -c:a libfdk_aac -vbr 1 -ac 2 -metadata title="AnimeSpectrum" -metadata:s:v title="AnimeSpectrum" -metadata:s:a title="AnimeSpectrum" -profile:a aac_he_v2 -c:s copy')
)
    THUMB = config("THUMBNAIL", default="https://telegra.ph/file/059d8942b7c02750c01ab.jpg")

except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
