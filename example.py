import json
import sys


def load_data(fname='data.json'):
    #loading pre processed data from data.json file
    with open(fname) as data_file:    
        data = json.load(data_file)

    return data


def run_test(fname):
    data = load_data(fname)
    sentences = data['test_tagged_sents']

    #debug statement
    #import pdb; pdb.set_trace()

    #looping over sentences
    for sent in sentences:
        points = 0

        #getting the different NER tags from the sentence 
        sent_ner = set([e['ner'] for e in sent['tokens']])
        sent_pos = set([e['pos'] for e in sent['tokens']])
        sent_words = set([e['word'] for e in sent['tokens']])
        sent_lemma = set([e['lemma'] for e in sent['tokens']])

        #awards
        if 'PERCENT' in sent_ner:
            points += 60

        if 'than' in sent_words:
            points += 20

        #penalizations
        if 'VB' in sent_pos:
            points -= 25

        if 'want' in sent_lemma:
            points -= 35

        sent['points'] = points


    #sorting sentences by points (reverse order)
    for sorted_sent in sorted(sentences, key=lambda x: (x['points']), reverse=True):
        sent_words = set([e['word'] for e in sorted_sent['tokens']])
        print "%s - %d points" % (sorted_sent['checkable'], sorted_sent['points'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'evaluate':
            try:
                run_test('data_eval.json')
            except:
                print "Couldn't find the json file, maybe you don't have it"
    else:
        print 'running test case'
        run_test('data.json')
