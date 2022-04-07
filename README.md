## BembaSpeech ASR Corpus

-----------------

### 1. INTRODUCTION

----------------------

[BembaSpeech](https://arxiv.org/pdf/2102.04889.pdf) is an ASR corpus for the Bemba language of Zambia. It contains read speech from diverse publicly available Bemba sources; literature books, radio/TV shows transcripts, Youtube video transcripts as well as various open online sources. Its purpose is to enable the training and testing of automatic speech recognition(ASR) systems in Bemba language. The corpus has 14, 438 utterances culminating into 24.5 hours of speech data.

All signal files are encoded in Waveform Audio File Format (WAVE) from a mono recording with a sample rate of 16K Hz. 

### 2. STRUCTURE

----------------

The repository is structured as follows:

        BembaSpeech
            ├── data
            │   ├── audio
            │   └── splits
            │       ├── dev.csv
            │       ├── test.csv
            │       └── train.csv
            ├── Data Statement.md
            ├── README.md
            ├── speaker_info.txt
            └── text.zip


The corpus is split into three parts:

* [train](BembaSpeech/data/splits/train.csv) - training set, of approximately 20 hours of speech 
* [dev](BembaSpeech/data/splits/dev.csv)   - development set, of approximately 2.5 hours of speech
* [test](BembaSpeech/data/splits/test.csv)  - testing set, of approximately 2 hours of speech

These subsets are disjoint, i.e. the audio of each speaker is assigned to exactly one subset. The allocation of each speaker contribution is as follows:

    _____________________________________________________________________________________________
    | NAME  | DURATION |  UNITS | 		SPEAKERS		|   Male   |    Female      |
    _____________________________________________________________________________________________
    | Train | 20:05:09 | 11,906 | 01, 03, 04, 05, 07, 08, 09, 10	|      5   |       3        |
    .--------------------------------------------------------------------------------------------
    | Dev	| 02:27:20 | 1,555  | 02, 11, 13, 14, 15, 16, 17	|      3   |       4        | 
    .--------------------------------------------------------------------------------------------
    | Test	| 02:03:03 | 977    | 06, 12				|      1   |       1        |
    ---------------------------------------------------------------------------------------------
    

### 3. CITATION

------------------------

If you use this speech dataset in your project or research, please consider citing as follows:

    @inproceedings{sikasote-anastasopoulos21bembaspeech,
        abstract = {We present a preprocessed, ready-to-use automatic speech recognition corpus, BembaSpeech, consisting over 24 hours of read speech in the Bemba language, a written but low-resourced language spoken by over 30% of the population in Zambia. To assess its usefulness for training and testing ASR systems for Bemba, we train an end-to-end Bemba ASR system by fine-tuning a pre-trained DeepSpeech English model on the training portion of the BembaSpeech corpus. Our best model achieves a word error rate (WER) of 54.78%. The results show that the corpus can be used for building ASR systems for Bemba.},
        title = {BembaSpeech: A Speech Recognition Corpus for the Bemba Language},
        author = {Sikasote, Claytone and Anastasopoulos, Antonios},
        booktitle = {Proceedings of AfricaNLP},
        address = {Online},
        month = {April},
        year = {2021},
        url = {https://arxiv.org/pdf/2102.04889.pdf}
    }
    
------------------------
    
### 4. LICENSE

------------------------

The dataset is made available to the research community licensed under the [Creative Commons BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) license
    
### 5. CONTACT

Please feel free to drop me an email `claytonsikasote@gmail.com` if you would like to discuss anything related to this work or anything else related. Cheers!
