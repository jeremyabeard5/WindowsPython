import requests
import json
import pandas as pd

def get_reddit(subreddit,listing,limit,timeframe): # returns json file with title, link, score, # comments
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
    except:
        print('An Error Occured')
    return request.json()
 
def get_post_titles(r): # print top posts for subreddit
    '''
    Get a List of post titles
    '''
    posts = []
    for post in r['data']['children']:
        x = post['data']['title']
        posts.append(x)
    return posts

def get_results(r): # extract all top 100 posts on subreddit
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments']}
    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df
 

        
if __name__ == "__main__":
    subreddit = 'python'
    limit = 100
    timeframe = 'all' #hour, day, week, month, year, all
    listing = 'top' # controversial, best, hot, new, random, rising, top
    
    r = get_reddit(subreddit,listing,limit,timeframe)
    print(r)
    jsonString = json.dumps(r)
    with open('data.json', 'w') as f:
        json.dump(r, f)
    #jsonFile = open("data.json", "w")
    #jsonFile.write(jsonString)
    #jsonFile.close()
    
    posts = get_post_titles(r)
    print('')
    print('')
    print(posts)

    df = get_results(r)
    print('')
    print('')

    print(df)

    print('')
    print('')
    for post in r['data']['children']:
        for k in post['data'].keys():
            print(k)