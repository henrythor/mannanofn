#!/usr/bin/env python
# -*- coding: utf-8 -*-
from config import config
from name_generator import NameGenerator
from tweet_generator import TweetGenerator
import tweepy
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--print', help="Only print the tweet, don't send it.", action='store_true')
args = parser.parse_args()


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    api = get_api(config)

    name_gen = NameGenerator()
    tweet_gen = TweetGenerator()

    name = name_gen.get_name()
    tweet_templ = tweet_gen.get_tweet()
    tweet_status = tweet_templ.format(name)
    if args.print:
        print(tweet_status)
    else:
        api.update_status(status=tweet_status)


if __name__ == "__main__":
    main()
