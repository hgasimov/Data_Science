import sys, json
import Queue

def countTags(tweet_file):
    tagCount = {}
    for tweet in tweet_file.readlines():
        jtweet = json.loads(tweet)
        if 'text' in jtweet:
            hashtags = jtweet['entities']['hashtags']
            if len(hashtags) > 0:
                for hashtag in hashtags:
                    htag = hashtag['text'] 
                    if htag in tagCount:
                        tagCount[htag] += 1
                    else:
                        tagCount[htag] = 1    
    return tagCount


def printTags(tagCount):
    if not tagCount: return # if tagCount is empty   
    for htag in tagCount:
        print '%s : %f' % (htag, tagCount[htag]) 

    
def printTopTen(tagCount):
    if not tagCount: return # if tagCount is empty
    if len(tagCount) < 10:
        print 'Not enough entries in the dictionary, exiting ...'
        return
    
    pqueue = Queue.PriorityQueue(10)
    for htag in tagCount:
        if not pqueue.full():
            pqueue.put((tagCount[htag], htag))
        elif tagCount[htag] > pqueue.queue[0][0]:
            pqueue.get()
            pqueue.put((tagCount[htag], htag))
    
    while not pqueue.empty():
        count, htag = pqueue.get()
        print '%s %.1f' % (htag, count)
    
    
def main():        
    tweet_file = open(sys.argv[1])
    tagCount = countTags(tweet_file)
    printTopTen(tagCount)
    

if __name__ == '__main__':
    main()
