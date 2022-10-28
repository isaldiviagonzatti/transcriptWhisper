# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Built based on 
#https://towardsdatascience.com/transcribe-audio-files-with-openais-whisper-e973ae348aa7
#https://www.assemblyai.com/blog/how-to-run-openais-whisper-speech-recognition-model/
#https://github.com/zhuzilin/whisper-openvino

import whisper
from pydub import AudioSegment
import os

#define working directory
os.getcwd()
os.chdir(r'C:\Users\...')

#File name. Don't forget the file extension ;)
source = r"File.m4a" 

#load audio file. change from_file if required (check repo)
sound = AudioSegment.from_file(source) # load source
sound = sound.set_channels(1) # mono
sound = sound.set_frame_rate(16000) # 16000Hz

# Extract a segment. Comment out if you want to conver it all
extract = sound[0:600000] #in miliseconds 1=60000

#save output as wav file
output_path = os.path.splitext(source)[0]+"_extract.wav"
extract.export(output_path, format="wav")

#load the model. Check repo for sizes: tiny, medium, large
model = whisper.load_model("small") 

#transcribe wav file. Language detection automatic
result= model.transcribe(r"file.wav")

#see result
result10min=result['text']

#save result as text file
text_file = open(r"textfile.txt", "w")
text_file.write(result10min)
text_file.close()
