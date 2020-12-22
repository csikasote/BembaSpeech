## Bemba ASR Corpus

1. INTRODUCTION

----------------------

BembaSpeech is a corpus of read speech in Bemba language of Zambia, based on publicly available Bemba literature books. Its purpose is to enable the training and testing of automatic speech recognition(ASR) systems in Bemba language. The corpus has 14, 438 utterances culminating into over 24 hours of speech.

All signal files are encoded in Waveform Audio File Format (WAVE) from a mono recording with a sample rate of 16K Hz.

2. STRUCTURE

-------------

The corpus is split into three parts:

* [train](BembaSpeech/train) - training set, of approximately 20 hours of speech 
* [dev](BembaSpeech/dev)   - development set, of approximately 2.5 hours of speech
* [test](BembaSpeech/test)  - testing set, of approximately 2 hours of speech

These subsets are disjointed, i.e. the audio of each speaker is assigned to exactly one subset. The allocation of each speaker contribution is as follows:

    ----------------------------------------------------------------
    | DATASET NAME  | 	SPEAKER ID                | DURATION   |
    ----------------------------------------------------------------
    | Train         | 01, 03, 04, 05, 07, 08, 09, 10  | ~ 20:05:09 |
    .---------------------------------------------------------------
    | Dev           | 02, 11, 13, 14, 15, 16, 17      | ~ 2:27:20  | 
    .---------------------------------------------------------------
    | Test	        | 06, 12                          | ~ 2:03:03  |
    ----------------------------------------------------------------
    

3. FILE ORGANIZATION

----------------
The corpus file organization is as follows:

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
               	    

------------------
* [train](BembaSpeech/train) - is the train dataset subset name
* **01**    - is the speaker_id of the speaker
* **180101-020249_bem_d31_elicit** is the recording session of the speaker. 
* **_transcripts.txt** files contains the transcripts for each of the utterances [<utterance_id transcript>]. 
* [SPEAKERS.TXT](SPEAKERS.TXT) contains information about speaker's gender and total amount of audio in the corpus.
* [DATASTATEMENT.md](DATASTATEMENT.docx) has contextual information to the creation of this dataset in detail
* [README.TXT](README.TXT) is the text version of the README.md.


-----------------
Prepared By:

Claytone Sikasote, 
17-12-2020 | 03:10PM, 
Lusaka, Zambia

