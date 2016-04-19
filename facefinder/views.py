
from django.shortcuts import render

import tweepy

def home(request):

    urls = []

    image_urls = search(urls)

    # print(len(image_urls))
    return render(request, 'home.html', {'image_urls': image_urls})

def search(url_list):
    consumer_key = 'gqdtIop6EyPtU0kWRb5sqehhd'
    consumer_secret = '9gGJOsfmCaFt5RpxYIy1YTyb7UKBO5sL1qc8Leopa3oaYi3ZPn'
    access_token = '1564127736-UGHvrFKk6XUIh2tSrDW4FtKS5fLj4qxZpguwWHM'
    access_token_secret = '3z4ou7BFQN23lf1Y7YuHqyp3iIETVoU8tNXmimxjGBWFU'

    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    search_results = api.search("q='#desaparecidosEC'")

    for result in search_results:

        url_list.append(result.entities['media'][0]['media_url'])
        # if result.entities['media'] is not None:
            # url_list.append(result.entities['media'][0]['media_url'])

    return url_list
