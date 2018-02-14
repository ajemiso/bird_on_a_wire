from .private import consumer_key, consumer_secret, access_token, access_token_secret
from .wire_quotes import WIRE_QUOTES

import os
from random import randint
from tweepy import OAuthHandler, API


class Session:

    def __init__(self,
                 consumer_key=consumer_key,
                 consumer_secret=consumer_secret,
                 access_token=access_token,
                 access_token_secret=access_token_secret
    ):
        self.api = self.get_tweepy_api()
        self.current_quote = None

    def __str__(self):
        return ""

    def __repr__(self):
        pass

    # tweepy object
    def get_tweepy_api(self):
        """ returns tweepy api object """
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = API(auth)
        return api

    @staticmethod
    def get_quote():
        """ returns formatted quote """
        quote_len = len(WIRE_QUOTES)-1
        i = randint(0, quote_len)

        sentence = WIRE_QUOTES[i][0]
        person = WIRE_QUOTES[i][1]

        quote = '"{}" - {}'.format(sentence, person)
        return quote

    def update_quote(self):
        """ uses Tweepy API object to update User profile with new quote """
        quote = self.get_quote()
        self.api.update_profile(description=quote)
        self.current_quote = quote

        return True
