#!/usr/bin/env python
from __future__ import absolute_import, division, print_function

import codecs
import fnmatch
import os
import subprocess
import sys
import tarfile
import unicodedata
import pandas
import progressbar
import shutil
import librosa
#from sox import Transformer
#from tensorflow.python.platform import gfile

import requests
import progressbar

from os import path, makedirs

def get_audio_info(file_name):
    """Return specified audio file duration and sample rate
    """
    return librosa.get_duration(filename=file_name)

def preprocess_data(source_dir):

    # directories
    save_dest_dir = "."
    
    # check if the dirs
    work_dir = os.path.join(source_dir, save_dest_dir)
    if not os.path.exists(work_dir):
    	os.makedirs(work_dir)
    
   
    print("Preparing audio data and generating csv files for deepspeech model ...")
    with progressbar.ProgressBar(max_value=3, widget=progressbar.AdaptiveETA) as bar:
    	train_clean = copy_audio_and_split_sentences(work_dir, "train", "train_")
    	train_clean.info()
    	bar.update(0)
    	dev_clean = copy_audio_and_split_sentences(work_dir, "dev", "dev_")
    	bar.update(1)
    	test_clean = copy_audio_and_split_sentences(work_dir, "test", "test_")
    	bar.update(2)
    
    # Write sets to disk as CSV files
    train_clean.to_csv(os.path.join(work_dir, "train.csv"), sep = '\t', index=False) 
    dev_clean.to_csv(os.path.join(work_dir, "dev.csv"), sep = '\t', index=False)
    test_clean.to_csv(os.path.join(work_dir, "test.csv"), sep = '\t', index=False)

def copy_audio_and_split_sentences(extracted_dir, data_set, dest_dir):
    source_dir = os.path.join(extracted_dir, data_set)
    target_dir = os.path.join(extracted_dir, dest_dir)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)    
    files = []
    for root, dirnames, filenames in os.walk(source_dir):
        for filename in fnmatch.filter(filenames, "*_transcripts.txt"):
            trans_filename = os.path.join(root, filename)
            with codecs.open(trans_filename, "r", "utf-8") as fin:
                for line in fin:
                    # Parse each segment line
                    first_space = line.find(" ")
                    seqid, transcript = line[:first_space], line[first_space + 1 :]

                    # We need to do the encode-decode dance here because encode
                    # returns a bytes() object on Python 3, and text_to_char_array
                    # expects a string.
                    transcript = (
                        unicodedata.normalize("NFKD", transcript)
                        .encode("ascii", "ignore")
                        .decode("ascii", "ignore")
                    )

                    transcript = transcript.lower().strip()

                    # Copy WAV files to target folder
                    src_wav_file = os.path.join(root, seqid + ".wav")              
                    dst_wav_file = os.path.join(target_dir, seqid + ".wav")

                    # check for duration of the audio
                    shutil.copy2(src_wav_file, dst_wav_file)
                    files.append((os.path.abspath(dst_wav_file), transcript))

    return pandas.DataFrame(data=files, columns=["path", "sentence"])


if __name__ == "__main__":
	source_dir = './dataset'
	preprocess_data(source_dir)
