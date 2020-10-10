# bemba-language-corpus


	UPDATES AS OF [10-OCT-2020]
	===========================
	
	DATASET		TARGET		RECORDED	UTTERANCES	STATUS			
	-------		------		-------		----------	------
	- Train		20Hrs		20:35:51	12, 500		100.0%		
	- Valid		02Hrs		02:52:52	01, 555		100.0%
	- Test		01Hrs		01:24:48	600		100.0%
	
	
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
		|    .-- test/	
		|    |    |
		|    |    .-- fold**/
		|    |	        |
		|    |    	.-- *_elict/
		|    |    		 |
		|    |  		 .-- *.wav
		|    |  		 |
		|    |  		 .-- *-metadata.json
		|    |  		 |
		|    |  	      	 .-- *_linker.txt
		|    |  		 |
		|    |  		 .-- Session**.txt
		|    .-- train/	
		|    |    |
		|    |    .-- fold**/
		|    |	        |
		|    |    	.-- *_elict/
		|    |    		 |
		|    |  		 .-- *.wav
		|    |  		 |
		|    |  		 .-- *-metadata.json
		|    |  		 |
		|    |  	      	 .-- *_linker.txt
		|    |  		 |
		|    |  		 .-- Session**.txt
		|    .-- valid/	
		|    	    |
		|    	    .-- fold**/
		|	        |
		|        	.-- *_elict/
		|        		 |
		|    	  		 .-- *.wav
		|    	  		 |
		|    	  		 .-- *-metadata.json
		|    	  		 |
		|    	  	      	 .-- *_linker.txt
		|    	  		 |
		|    	  		 .-- Session**.txt
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

