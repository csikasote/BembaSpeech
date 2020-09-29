# bemba-language-corpus

	In this Bemba language data collection project, the target hours of this ASR dataset per set is as follows:
		- train set: 20hrs
		- dev set: 2hrs:
		- test set: 1hr
	At the moment, there are 16hrs: 11 minutes of recorded speech.

	<bemba_language_corpus>
		|
		.-- README.md
		|
		.-- TRACKER.txt
		|
		.-- audio/
		|    |
		|    .-- fold*/
		|	  |
		|	  .-- *_elict/
		|		 |
		|		 .-- *.wav
		|		 |
		|		 .-- *-metadata.json
		|		 |
		|	      	 .-- *_linker.txt
		|		 |
		|		 .-- Session**.txt
		|        
		.-- text/
		|    |
		|    .-- fold*/
		|    |    |
		|    |    .-- AllFiles.txt
		|    |    |
		|    |    .-- Session*.txt
		|    | 
		|    .-- BEEN CORPUS.ods
		|    |    
		|    .-- MAIN_TEXT.txt
		|
		.-- text_source_docs/
			|
			.-- **_fold_**
