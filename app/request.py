import urllib.request,json
from .models import News

api_key=None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key=app.config["NEWS_API_KEY"]
    base_url=app.config["NEWS_API_BASE_URL"]
def news(headlines):
    get_news_url=base_url.format(headlines,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)

        news_results=None

        if get_news_response['articles']:
            news_result_list=get_news_response["articles"]
            news_results=process_results(news_result_list)

    return news_results

def process_results(news_list):
    news_results=[]
    for news in news_list:
        title=news.get("title")
        description=news.get("description")
        urltoImage=news.get("urlToImage")

        news_object=News(title,description,urltoImage)

        news_results.append(news_object)
        news_results=news_results[:6]
    return news_results
