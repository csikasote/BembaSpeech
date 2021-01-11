1. General information
======================

BembaSpeech is a corpus of read speech in Bemba language of Zambia, based on publicly available Bemba literature books. Its purpose is to enable the training and testing of automatic speech recognition(ASR) systems. The corpus has 14, 438 utterances culminating into over 24 hours.

2. Structure
============

The corpus is split into three parts; train, dev, test. The subsets are disjoint, i.e. the audio of each speaker is assigned to exactly one subset. The allocation of each speaker is as follows:

---------------------------------------------------------------------------------------------------------
| NAME  |	DURATION	| UNITS  | 		SPEAKERS		| GENDER PROPORTIONALITY |
---------------------------------------------------------------------------------------------------------
| Train |	~ 20:05:09 	| 11,906 | 01, 03, 04, 05, 07, 08, 09, 10	| Male {5}, Female {3}   |
.--------------------------------------------------------------------------------------------------------
| Dev	|	~ 2:27:20	| 1,555  | 02, 11, 13, 14, 15, 16, 17		| Male {3}, Female {3}   | 
.--------------------------------------------------------------------------------------------------------
| Test	|	~ 2:03:03	| 977    | 06, 12				| Male {1}, Female {1}   |
---------------------------------------------------------------------------------------------------------


2.1 Organization of dataset subsets
-------------------------------------------------

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
               	    
where 01 is the speaker_id of the reader, and 180101-020137_bem_d31_elicit and 180101-020249_bem_d31_elicit are recording session chapters of the speakers. The *_transcript.txt files contain the transcripts for each of the utterances, in the form, <utterance_id> <transcription>. The *_text_script.txt files contains raw text tokenized by sentences from which the speakers read from into the Lig-Aikuma mobile software.


//Prepared By:

Claytone Sikasote
17-12-2020; 03:10PM
Lusaka, Zambia

