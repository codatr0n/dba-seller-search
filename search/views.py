from django.shortcuts import render
from django.http import HttpResponse

import requests
import json


def home(request):
    return render(request, 'base.html')


def get_listings(request):
    seller_url = request.POST.get('seller_url')

    headers = {
        'Host': 'www.dba.dk',
        'User-Agent':
        'Mozilla/5.0 (Macintosh Intel Mac OS X 10.15 rv: 71.0) Gecko/20100101 Firefox/71.0',
        'Accept': 'text/html, application/xhtml+xml, application/xml'
    }

    start_url = seller_url

    api_url = 'https://www.dba.dk/api/dba-soi-bff/saelger/privat/dba/{seller_id}?page='.format(
        seller_id=start_url.split('/')[-1])

    nextPage = '1'

    while nextPage:
        response = requests.get(api_url + str(nextPage), headers=headers)
        listings = response.json()

        for listing in listings['listings']['listings']:
            # print(listing)
            first_line = listing['text'].split('\n')[0]
            category = first_line.split(',')[0]
            if category in ['LP', 'EP', 'Maxi-single 12"', 'Single']:
                item = {}
                item['price'] = listing['price']['value']
                item['image'] = listing['pictureUrl']
                item['url'] = listing['url']
                item['category'] = first_line.split(',')[0]
                item['artist'] = first_line.split(',')[1].strip()
                item['title'] = first_line.split(',')[2].strip()

                # print(listing['text'].split('\n')[0])
                print(json.dumps(item, indent=4))

        # nextPage = listings['listings']['nextPage']
        nextPage = 0

    return HttpResponse('Listings')
