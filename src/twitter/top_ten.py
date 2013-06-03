import sys, json

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


'''
    calculates max value in the dictionary ten times.
    sorting was not used because it takes NLogN time
'''    
def printTopTen(tagCount):
    if not tagCount: return # if tagCount is empty
    if len(tagCount) < 10:
        print 'Not enough entries in the dictionary, exitting ...'
        return
    
    for i in range(10):
        maxtag = ''
        maxcount = -1
        for htag in tagCount:
            if tagCount[htag] > maxcount:
                maxcount = tagCount[htag]
                maxtag = htag
        
        print '%s %.1f' % (maxtag, maxcount)
        tagCount[maxtag] = 0
                
        
    
def main():        
    tweet_file = open(sys.argv[1])
    tagCount = countTags(tweet_file)
    printTopTen(tagCount)
    

if __name__ == '__main__':
    main()
