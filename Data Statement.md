# Data Statement for BembaSpeech Dataset

> Dataset name: **BembaSpeech**

> Citation (if available):

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

> Data set developer(s): **Claytone Sikasote, Antonios Anastasopoulos**

> Data statement author(s): **Claytone Sikasote, Antonios Anastasopoulos**

> Others who contributed to this document: **N/A**

> Link to the dataset:  **https://github.com/csikasote/BembaSpeech** 

> Dataset license:  **Creative Commons BY-NC-ND 4.0** 

> Total Number of hours: **24 hours**

## A. CURATION RATIONALE 

> The BembaSpeech is an automatic speech recognition(ASR) dataset consisting of over 24 hours of read speech for the Bemba language spoken by over 30% of the population of Zambia.  The motivation for building the BembaSpeech is to create a speech recognition dataset for Bemba language that can be used to train and test speech recognition systems.

## B. LANGUAGE VARIETY/VARIETIES

> The language considered in this corpus is Bemba (ISO 639-3 bem). Bemba is a bantu language predominatly spoken in the northen part of Zambia. The language is also spoken in some parts of Democratic Republic of Congo, Tanzania as well as Botswana. 

## C. SPEAKER DEMOGRAPHIC

> Speakers were directly approached to create audio utterances by eliciting text scripts in the Lig-Aikuma mobile application. The speakers were selected based on their fluency to speak and read Bemba and not necessarily native language speakers. It is, however, expected that some, but not all, of the speakers speak Bemba as a native language. Based on information extracted from metadata as supplied by speakers on recording, seventeen (17) speakers were involved in recording audio, of which eight (8) are female and nine (9) male. The age range of speakers is between 22 and 28 years and, all of them are identified to be black. In terms of occupation, all the speakers are university students. 
 
## D. ANNOTATOR DEMOGRAPHIC
> Annotator demographic information is not available as the dataset does not contain any annotations.

## E. SPEECH SITUATION

> The corpus comprises of the speech utterances that were recorded from text scripts using the Lig-Aikuma application using the text elicitation mode. The recordings were done in Zambia at the University of Zambia between 20th August, 2020 and 12th October, 2020.

## F. TEXT CHARACTERISTICS

>  The phrases and sentences contained in this dataset were obtained from diverse text sources in Bemba language. No criteria was used in the selection of the text sources. Texts were obtained based on their public availability.

## G. RECORDING QUALITY

> The audio utterances were recorded using the Lig-Aikuma mobile application by eliciting texts that are tokenized at sentence level. Almost all recordings were not done in closed and soundproof environment. Therefore, It is expected that there would be some background noise.

## H. OTHER

> N/A 

## I. PROVENANCE APPENDIX

> Nothing contained in this dataset has been gotten from an already existing dataset. Therfore, provenance appendix does not exist.
