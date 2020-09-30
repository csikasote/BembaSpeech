# bemba-language-corpus


	1. UPDATES AS OF [30-SEP-2020]
	   ===========================
	
	DATASET		TARGET		RECORDED	UTTERANCES			
	-------		------		--------	----------
	- Train		20Hrs		16:11:02	10, 298			
	- Valid		02Hrs		TBU		TBU
	- Test		01Hrs		TBU		TBU
	
	2. FILE ORGANIZATION
	   =================
	
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
