import requests, json

def getBearer():
    authURL = "https://api.twitter.com/oauth2/token"
    consumerKey = '<consumer key>'
    consumerSecret = '<consumer secret>'
    data = {'grant_type': 'client_credentials'}
    response = requests.post(authURL, data=data, auth=(consumerKey, consumerSecret))

    def makeToken(response):
        tokenType = json.loads(response.text)['token_type']
        accessToken = json.loads(response.text)['access_token']
        token = tokenType + ' ' + accessToken
        return token

    return makeToken(response)

def getLatestTweet(user):
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=" + user + "&count=1&exclude_replies=true&include_rts=false"
    headers = {
        'Authorization': getBearer()
    }
    response = requests.request("GET", url, headers=headers)

    return(json.loads(response.text)[0]['text'])

def stringByUser(str, user):
    find = str in getLatestTweet(user)
    return find

# test with:        print(stringByUser('Vegan', 'isitvegan'))