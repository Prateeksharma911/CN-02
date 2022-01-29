import requests
import re
inputmoviename=input("Enter Movie name:")
url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":inputmoviename}

headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': "da27635acemsh1b711f00b50d60ap151737jsn1127a9f4ec73"
    }

try:
    response = requests.request("GET", url, headers=headers, params=querystring)
    if response.status_code==200:
        movielist=(response.json())
        movielist=movielist['d'][0]['id']

        url = "https://www.imdb.com/title/{mname}/".format(mname=movielist)

        from bs4 import BeautifulSoup as Soup

        movierating = requests.request("GET",url)
        # Converting url output in text
        outputimdb=movierating.text
        print("Getting you data")
        # parsing html data
        soup_data=Soup(outputimdb,'html.parser')
        # Find imdb rating in our html
        movies = soup_data.findAll('span',{'class':'AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV'})

        imdbrating=str(movies[0])
        print("Movie rating is :",imdbrating[69:72])
    else:
        print("Sorry your movie was not found")

except requests.exceptions.RequestException as e:
    print("Something went wrong")
    raise SystemExit(e)