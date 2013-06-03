import sys, json

def main():
    total = 0
    termfreq = {}
        
    tweet_file = open(sys.argv[1])
    tweets = tweet_file.readlines()
    for tweet in tweets:
        jtweet = json.loads(tweet)
        if 'text' in jtweet: 
            for term in jtweet['text'].strip().split(' '):
                term = term.strip().replace('(', '').replace(')', '').replace('\n', '').strip()
                if len(term) == 0: continue
                if term in termfreq: 
                    termfreq[term] += 1
                else:
                    termfreq[term] = 1.0
                total += 1
    
    for term in termfreq:
        print "%s %f" % (term.strip(), termfreq[term]/total)    

if __name__ == '__main__':
    main()
