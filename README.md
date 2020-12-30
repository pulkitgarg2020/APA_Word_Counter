# APA_Word_Counter

This program parses over a `.docx` which uses APA citation format and gives you the word count excluding the in-text citations and the bibliography section. A sample APA file has been provided in the repository. If you want to count the number of words in your file, you would first have to clone the repo and then either place your file in the repo or mention the absolute path for your file. 

To run the program, you can use the following command:
```
py APA_word_counter.py <Name of docx file> <Heading for references section>
```
For example to run the code for the sample file provided:
```
py APA_word_counter.py Sample_APA.docx Bibliogrpahy
```

If you don't want to use the command line arguments, you can input when asked in the prompts. Note that this program just works with the docx file. 
