# Automating fact checking
Automating fact checking exercise from Chequeado's Mozilla Fest 2016 presentation

This repository container an exercise on automated fact checking, originally created for Mozilla Fest 2016 (https://app.mozillafestival.org/#_session-813).

The 'data.json' file contains already processed sentences from several USA 2016 presidential debates extracted from Politifact Claimbuster site (http://idir-server2.uta.edu/claimbuster/debates). The data was processed using Stanford CoreNLP server (http://stanfordnlp.github.io/CoreNLP/).

The file '.py' contains the exercise code, running this code from the command line will output the results of the application of some custom rules to identify the trueness of each sentence.

***Goal***

The goal in this exercise is to use basic NLP techniques, in order to find patterns about what likely makes a sentence "fact checkable" and what doesn't.

You will have to tweak and create custom rules awarding or penalizing sentences.


***Resources***

The PoS tagger uses the tags from the Penn Treebank Project. This is the list : https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
