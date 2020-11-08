import requests
import json

API_KEY = "27bd1bb9af0b4379852de8226697827d"


country = "in"
source = "bbc-news"
category = "technology"
search = "politics"
fromDate = ""
toDate = ""
domains = ""
language = "en"
top_headlines_country = "https://newsapi.org/v2/top-headlines?country=" + country + "&apiKey=" + API_KEY
top_headlines_src = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + API_KEY
top_headlines_category = "https://newsapi.org/v2/top-headlines?country=" + country + "&category=" + category + "&apiKey=" + API_KEY
top_headlines_search = "https://newsapi.org/v2/top-headlines?q=" + search + "&apiKey=" + API_KEY

everything_search = "https://newsapi.org/v2/everything?q="+search+"&apiKey="+API_KEY
everything_search_from_to = "https://newsapi.org/v2/everything?q="+search+"&from="+fromDate+"&to="+toDate+"&sortBy" \
                                                                                                          "=popularity&apiKey="+API_KEY
everything_from_domain = "https://newsapi.org/v2/everything?domains="+domains+"&apiKey="+API_KEY


all_available_sources = "https://newsapi.org/v2/sources?apiKey="+API_KEY
all_sources_with_language = "https://newsapi.org/v2/sources?language="+language+"&apiKey="+API_KEY
all_sources_with_language_with_country = "https://newsapi.org/v2/sources?language="+language+"&country="+country+"&apiKey="+API_KEY
data = requests.get(top_headlines_category)
diction_load = json.loads(data.content)
print(json.dumps(diction_load,indent=2))
# json_decoded is a dictionary

dictionary = {}
dictList = []
if diction_load['status'] == "error":
    print("error")
articles = diction_load['articles']
for item in articles:
    dictionary['author'] = item['author']
    dictionary['title'] = item['title']
    dictionary['url'] = item['url']
    dictionary['imageSrc'] = item['urlToImage']
    dictionary['time'] = item['publishedAt']
    dictList.append(dictionary)
print(dictList)




def return_list(url):
    data = requests.get(url)
    diction_load = json.loads(data.content)

    List = []
    if diction_load['status'] == "error":
        print("error")
    articles = diction_load['articles']
    for item in articles:
        dictionary = {}
        dictionary['author'] = item['author']
        dictionary['title'] = item['title']
        dictionary['url'] = item['url']
        dictionary['imageSrc'] = item['urlToImage']
        dictionary['time'] = item['publishedAt']
        List.append(dictionary)
    return List


def top_headlines_search(search):
    search_top_headlines = "https://newsapi.org/v2/top-headlines?q=" + search + "&apiKey=" + API_KEY
    List = return_list(search_top_headlines)
    print(List)
    return List


def get_top_headlines_category(category):
    country = "in"
    top_headlines_category = "https://newsapi.org/v2/top-headlines?country=" + country + "&category=" + category + "&apiKey=" + API_KEY
    List = return_list(top_headlines_category)
    print(List)


def get_news_from_source(source):
    top_headlines_src = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + API_KEY
    List = return_list(top_headlines_src)
    print(List)


def get_top_headlines_country(country):
    country = country
    top_headlines_country = "https://newsapi.org/v2/top-headlines?country=" + country + "&apiKey=" + API_KEY
    List = return_list(top_headlines_country)
    print(List)
