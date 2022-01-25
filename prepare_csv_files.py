from __future__ import absolute_import, division, print_function

import pandas as pd
import numpy as np
import progressbar
import unicodedata
import librosa
import fnmatch
import codecs
import shutil
import sys
import os

def copy_audio_and_split_sentences(extracted_dir, data_set, dest_dir):
    source_dir = os.path.join(extracted_dir, data_set)
    target_dir = os.path.join(extracted_dir, dest_dir)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    files = []
    ds_time_size = 0
    for root, dirnames, filenames in os.walk(source_dir):
        for filename in fnmatch.filter(filenames, "*_transcripts.txt"):
            trans_filename = os.path.join(root, filename)
            with codecs.open(trans_filename, "r", "utf-8") as fin:
                for line in fin:
                    # Parse each segment line
                    first_space = line.find(" ")
                    seqid, transcript = line[:first_space], line[first_space + 1 :]

                    transcript = (
                        unicodedata.normalize("NFKD", transcript)
                        .encode("ascii", "ignore")
                        .decode("ascii", "ignore")
                    )

                    transcript = transcript.lower().strip()

                    # Copy audio files to target folder
                    src_wav_file = os.path.join(root, seqid + ".wav")              
                    dst_wav_file = os.path.join(target_dir, seqid + ".wav")
                    wav_duration = librosa.get_duration(filename=src_wav_file)
                    ds_time_size = ds_time_size + (wav_duration/3600)
                    # check for duration of the audio
                    shutil.copy2(src_wav_file, dst_wav_file)
                    #files.append((os.path.abspath(dst_wav_file), transcript))
                    files.append((seqid+".wav", wav_duration, transcript))
                    
    set_df = pd.DataFrame(data=files, columns=["path", 'duration', "sentence"])
    return set_df, ds_time_size
    
def preprocess_data(source_dir):    
    # check if the dirs
    data_dir = os.path.join(source_dir, ".")

    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
   
    print("Preparing audio files and generating csv files for training the model ... \n")
    with progressbar.ProgressBar(max_value=3, widget=progressbar.AdaptiveETA) as bar:
        
        # processing training set
        train_clean, train_size = copy_audio_and_split_sentences(data_dir, "train", "audio")
        bar.update(0)
        train_clean.to_csv(os.path.join(data_dir, "train.csv"), sep = '\t', index=False)
        print('train.csv has been processed successfully!')
        print('training set size: {:.2f} hrs'.format(train_size))
        print('No of files:', len(train_clean))
        
        train_folder = os.path.join(data_dir, "train")
        if os.path.exists(train_folder):
            try:
                shutil.rmtree(train_folder)
            except OSError as e:
                print("Error:%s." % (e.strerror))
        
        # processing dev set
        dev_clean, dev_size = copy_audio_and_split_sentences(data_dir, "dev", "audio")
        bar.update(1)
        dev_clean.to_csv(os.path.join(data_dir, "dev.csv"), sep = '\t', index=False)
        print('dev.csv has been processed successfully!')
        print('evaluation set size: {:.2f} hrs'.format(dev_size))
        print('No of files:', len(dev_clean))
        
        dev_folder = os.path.join(data_dir, "dev")
        if os.path.exists(dev_folder):
            try:
                shutil.rmtree(dev_folder)
            except OSError as e:
                print("Error:%s." % (e.strerror))
        
        # processing test set
        test_clean, test_size = copy_audio_and_split_sentences(data_dir, "test", "audio")
        bar.update(2)
        test_clean.to_csv(os.path.join(data_dir, "test.csv"), sep = '\t', index=False)
        print('test.csv has been processed successfully!')
        print('test set size: {:.2f} hrs'.format(test_size))
        print('No. of file:', len(test_clean))
        
        test_folder = os.path.join(data_dir, "test")
        if os.path.exists(test_folder):
            try:
                shutil.rmtree(test_folder)
            except OSError as e:
                print("Error:%s." % (e.strerror))  
    

if __name__ == "__main__":
    source_dir = './BembaSpeech'
    preprocess_data(source_dir)
