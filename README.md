# Automated fact checking
### Automated fact checking exercise from Chequeado's Mozilla Fest 2016 presentation

This repository contains an exercise on automated fact checking, originally created for Mozilla Fest 2016 (https://app.mozillafestival.org/#_session-813).

The 'data.json' file contains already processed sentences from several USA 2016 presidential debates extracted from Politifact Claimbuster site (http://idir-server2.uta.edu/claimbuster/debates). The data was processed using Stanford CoreNLP server (http://stanfordnlp.github.io/CoreNLP/). I didn't include the processing code for the sake of simplicity, if you'd like to see that let me know.

The file 'example.py' contains the exercise code, running this code from the command line will output the results of the application of some custom rules to identify the trueness of each sentence. It already contains some sample rules as a kickstart, but you can modify/remove them and include your own based on what you can observe.

You can explore the data dictionary running something like this in a Python console:

`from example import load_data`

`data = load_data()`

`data.keys()`

`data['ner_pos_count']`


## Goal

The goal of this exercise is to use some basic NLP techniques in order to find patterns about what likely makes a sentence "fact checkable" and what doesn't.

A sentence with the flag **True** is a "fact-checkable" one, and a sentence with the **False** flag isn't-

You will have to tweak and create custom rules awarding or penalizing sentences and then run the test code to see how good they were. **Try to get at least five sentence with the flag True (meaning that the sentence is fact-checkable) with more points than the ones with the flag False.**

Something like this:

(from the command line)
`python example.py`

1. True \- 80 points
2. True \- 60 points
3. True \- 60 points
4. True \- 60 points
5. True \- 55 points
6. True \- 35 points
7. False \- 35 points

Then you can run the following command and check your results against a new dataset to see how well you did:

(from the command line)
`python example.py evaluate`


## Resources

The PoS tagger uses the tags from the Penn Treebank Project. This is the list : https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
