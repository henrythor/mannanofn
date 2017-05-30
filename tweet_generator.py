# -*- coding: utf-8 -*-
import random
import datetime


class TweetGenerator(object):
    tweets = [
        {
            'tweet_templ': 'Vér höfum ákveðið að hleypa nafninu „{}“ í notkun. Góðar stundir.',
            'time_tags': ['any']
        }
    ]

    def _get_tweet(self, tag):
        lentweets = len(self.tweets)
        proposed_tweet = self.tweets[random.randint(0, lentweets)]
        if tag in proposed_tweet['time_tags'] or 'all' in proposed_tweet['timetags']:
            return proposed_tweet['tweet_templ']
        return self._get_tweet(tag)

    def _get_tag(self):
        now = datetime.datetime.now()
        hour = now.hour

        if hour in range(0, 6):
            return 'night'
        elif hour in range(6, 11):
            return 'morning'
        elif hour in range(11, 14):
            return 'lunch'
        elif hour in range(14, 18):
            return 'afternoon'
        else:
            return 'evening'

    def get_tweet(self):
        return self._get_tweet(self._get_tag())

