import sys
import json

def readScores(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores

def main():
    sent_file = open(sys.argv[1])        
    scores = readScores(sent_file)
    
    tweet_file = open(sys.argv[2])
    tweets = tweet_file.readlines()
    for tweet in tweets:
        jtweet = json.loads(tweet)
        if 'text' in jtweet: 
            for term in jtweet['text'].split(' '):
                if term not in scores:
                    term_sent = calcScore(jtweet['text'], scores)
                    print term + ' ' + str(term_sent)
            
def calcScore(s, scores):
     n = .0 # score
     words = s.strip().split(' ')
     for word in words:
         if word in scores:
             n+= scores[word]
     return n
                

if __name__ == '__main__':
    main()
