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

    ------------------------------------------------------------------------------------------------------
    | NAME  |	DURATION	| 		SPEAKER ID		|   GENDER PROPORTIONALITY   |
    ------------------------------------------------------------------------------------------------------
    | Train |	~ 20:05:09 	| 01, 03, 04, 05, 07, 08, 09, 10	|   Male {5}, Female {3}     |
    .-----------------------------------------------------------------------------------------------------
    | Dev	|	~ 2:27:20	| 02, 11, 13, 14, 15, 16, 17		|   Male {3}, Female {3}     | 
    .-----------------------------------------------------------------------------------------------------
    | Test	|	~ 2:03:03	| 06, 12				|   Male {1}, Female {1}     |
    ------------------------------------------------------------------------------------------------------
    

3. FILE ORGANIZATION

----------------
The corpus file organization is as follows:

    <corpus root>
        |
        .- DATASTATEMENT.docx
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
        |           	    |
        . ...               .- ...
               	    

------------------
* [train](BembaSpeech/train) - is the train dataset subset name
* **01**    - is the speaker_id of the speaker
* **180101-020249_bem_d31_elicit** is the recording session of the speaker. 
* **_transcripts.txt** files contains the transcripts for each of the utterances [<utterance_id transcript>]. 
* **_raw_script.txt** files contains the text from which readers read from to create audio. [<transcripts>]
* [SPEAKERS.TXT](BembaSpeech/SPEAKERS.TXT) contains information about speaker's gender and total amount of audio in the corpus.
* [DATASTATEMENT](BembaSpeech/DATASTATEMENT.docx) has contextual information to the creation of this dataset in detail
* [README.TXT](BembaSpeech/README.TXT) is the text version of the [README.md](README.md).


-----------------
Prepared By:

Claytone Sikasote, 
17-12-2020 | 03:10PM, 
Lusaka, Zambia

