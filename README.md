## BembaSpeech: a Speech Recognition Corpus for the Bemba Language

[![License: CC BY NC ND 4.0](https://img.shields.io/badge/License-CC_BY_NC_ND_4.0-green.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/)

### 1. Introduction

----------------------

[BembaSpeech](http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.790.pdf) is an ASR corpus for the Bemba language of Zambia. It contains read speech from diverse publicly available Bemba sources; literature books, radio/TV shows transcripts, Youtube video transcripts as well as various open online sources. Its purpose is to enable the training and testing of automatic speech recognition(ASR) systems in Bemba language. The corpus has 14, 438 utterances culminating into 24.5 hours of speech data.

All signal files are encoded in Waveform Audio File Format (WAVE) from a mono recording with a sample rate of 16K Hz.

The corpus is split into three parts:

* training set - of approximately 20 hours of speech 
* development set- of approximately 2.5 hours of speech
* testing set - of approximately 2 hours of speech

### 2. Structure

----------------

The repository is structured as follows:

        BembaSpeech
            ├── bem
            │   ├── audio/*
            │   ├── dev.csv
            │   ├── test.csv
            │   └── train.csv
            ├── Data Statement.md
            ├── README.md
            └── speaker_info.txt

### 3. Citation

------------------------

If you use this speech dataset in your project or research, please consider citing as follows:

        @InProceedings{sikasote-anastasopoulos:2022:LREC,
          author    = {Sikasote, Claytone  and  Anastasopoulos, Antonios},
          title     = {BembaSpeech: A Speech Recognition Corpus for the Bemba Language},
          booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
          month          = {June},
          year           = {2022},
          address        = {Marseille, France},
          publisher      = {European Language Resources Association},
          pages     = {7277--7283},
          abstract  = {We present a preprocessed, ready-to-use automatic speech recognition corpus, BembaSpeech, consisting over 24 hours of read speech in the Bemba language, a written but low-resourced language spoken by over 30\% of the population in Zambia. To assess its usefulness for training and testing ASR systems for Bemba, we explored different approaches; supervised pre-training (training from scratch), cross-lingual transfer learning from a monolingual English pre-trained model using DeepSpeech on the portion of the dataset and fine-tuning large scale self-supervised Wav2Vec2.0 based multilingual pre-trained models on the complete BembaSpeech corpus. From our experiments, the 1 billion XLS-R parameter model gives the best results. The model achieves a word error rate (WER) of 32.91\%, results demonstrating that model capacity significantly improves performance and that multilingual pre-trained models transfers cross-lingual acoustic representation better than monolingual pre-trained English model on the BembaSpeech for the Bemba ASR. Lastly, results also show that the corpus can be used for building ASR systems for Bemba language.},
          url       = {https://aclanthology.org/2022.lrec-1.790}
        }
    
------------------------

    
### 4. Contact

Please feel free to drop me an email `claytonsikasote@gmail.com` if you would like to discuss anything related to this work or anything else related. Cheers!
