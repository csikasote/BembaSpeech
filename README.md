# bemba-language-corpus


	UPDATES AS OF [02-OCT-2020]
	===========================
	
	DATASET		TARGET		RECORDED	UTTERANCES	STATUS			
	-------		------		--------	----------	------
	- Train		20Hrs		19:06:15	11, 814		95.0%		
	- Valid		02Hrs		TBU		TBU		00.0%
	- Test		01Hrs		TBU		TBU		00.0%
	
	
	FILE ORGANIZATION
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
