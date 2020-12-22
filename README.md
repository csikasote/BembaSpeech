## Bemba ASR Corpus

1. INTRODUCTION

----------------------

BembaSpeech is a corpus of read speech in Bemba language of Zambia, based on publicly available Bemba literature books. Its purpose is to enable the training and testing of automatic speech recognition(ASR) systems. The corpus has 14, 438 utterances culminating into over 24 hours of speech.

All signal files are encoded in Waveform Audio File Format (WAVE) from a mono recording with a sample rate of 16K Hz.

2. STRUCTURE

-------------

The corpus is split into three parts:

* train - for training 
* dev   - for validation
* test  - for testing 

These subsets are disjointed, i.e. the audio of each speaker is assigned to exactly one subset. The allocation of each speaker contribution is as follows:

    --------------------------------------------------------
    | NAME  | 	SPEAKER ID                | DURATION   |
    --------------------------------------------------------
    | Train | 01, 03, 04, 05, 07, 08, 09, 10  | ~ 20:05:09 |
    .-------------------------------------------------------
    | dev   | 02, 11, 13, 14, 15, 16, 17      | ~ 2:27:20  | 
    .-------------------------------------------------------
    | test	| 06, 12                          | ~ 2:03:03  |
    --------------------------------------------------------
    

3. ORGANIZATION

----------------

    <corpus root>
        |
        .- DATASTATEMENT.md
        |
        .- README.TXT
        |
        .- SPEAKERS.TXT
        |
        .- train -/
        |        |
        .        .- 01 - /
        |           |
        .           .- 180101-020137_bem_d31_elicit - /
        |           |	    |
        .           .	    .- 01-180101-020137_bem_d31_elicit_raw_script.txt
        |           |	    |
        .           .	    .- 01-180101-020137_bem_d31_elicit_transcript.txt
        |           |	    |    
        .           .	    .- 01-180101-020137_bem_d31_elicit_0.wav
        |           |	    |
        .           .	    .- 01-180101-020137_bem_d31_elicit_1.wav
        |           |	    |
        .           |	    . ...
        |           |
        .           .- 180101-020249_bem_d31_elicit/
        |           	    | ...
        . ...
               	    
* train - is the dataset subset name, 
* 01    - is the speaker_id of the reader
* 180101-020249_bem_d31_elicit  - is the recording session of the speakers/reader. 
* *_transcripts.txt files - contain the transcripts for each of the utterances, in the form, <utterance_id> <transcription>. 
* The *_text_script.txt files   -  raw text tokenized by sentences from which the speakers read from into the Lig-Aikuma mobile software.


-----------------
// Prepared By:

Claytone Sikasote, 
17-12-2020 | 03:10PM, 
Lusaka, Zambia

