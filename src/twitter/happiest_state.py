import sys
import json

DEBUG = False

def readScores(sent_file):
    scores = {}
    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)
    return scores

def main():
    maxstate = ''
    maxscore = float("-inf")
    
    sent_file = open(sys.argv[1])        
    scores = readScores(sent_file)
    
    tweet_file = open(sys.argv[2])
    for tweet in tweet_file.readlines():
        jtweet = json.loads(tweet)
        if 'text' in jtweet:
            score = calcScore(jtweet['text'], scores)
            if score > maxscore:
                username = jtweet['user']['name'].strip()
                maxstate = username[0] + username[-1]
                maxscore = score 
                if DEBUG: print "%s : %s : %s %f" % (jtweet['text'], username, maxstate, score)
    
    if DEBUG: print '\nMax state is %s with score %f' %(maxstate, maxscore)
    print maxstate
        

def calcScore(s, scores):    
    n = .0 # score
    words = s.strip().split(' ')
    for word in words:
        if word in scores:
            n+= scores[word]
    return n

    

if __name__ == '__main__':
    main()

