# bemba-language-corpus


	UPDATES AS OF [10-OCT-2020]
	===========================
	
	DATASET		TARGET DURATION		HOURS RECORDED		NUMBER OF UTTERANCES	STATUS			
	-------		---------------		--------------		--------------------	------
	- Train		20H:00M:00S		20H:35M:51S		~ 12, 500		100.0%		
	- Valid		02H:00M:00S		02H:52M:52S		~ 01, 555		100.0%
	- Test		01H:00M:00S		01H:24M:48S		~ 600			100.0%
	
	
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

