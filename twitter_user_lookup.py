# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:20:28 2021

@author: blinker_dev
"""

import requests

# for bearer token
import yaml
import json

# load the yaml file
def process_yaml():
    with open("c:\\users\\unknown\\blinker_dev\\config.yaml") as file:
        return yaml.safe_load(file)

def twitter_user_lookup(user_value):
    url = ''
    if(user_value.isnumeric() == True):
        url = "https://api.twitter.com/2/users?ids={}".format(
            user_value
            )
    else:
        url = "https://api.twitter.com/2/users/by/username/{}".format(
            user_value
            )
    return url

def create_bearer_token(data):
    return data["twitter_api"]["bearer_token"]

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    url = twitter_user_lookup('blinker_dev')
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    
    #need to call the JSON process
    #print(twitter_auth_and_connect(bearer_token, url))
    # {'data': {'id': '1440753652403040261', 'name': 'developer blinker', 'username': 'blinker_dev'}}
    zy = twitter_auth_and_connect(bearer_token, url)
    print(zy)

    #print(data_list)

if __name__ == '__main__':
    main()
