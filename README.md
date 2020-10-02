# bemba-language-corpus


	UPDATES AS OF [02-OCT-2020]
	===========================
	
	DATASET		TARGET		RECORDED	UTTERANCES			
	-------		------		--------	----------
	- Train		20Hrs		18:31:53	11, 448			
	- Valid		02Hrs		TBU		TBU
	- Test		01Hrs		TBU		TBU
	
	
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
