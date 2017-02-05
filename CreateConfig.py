import configparser

config = configparser.RawConfigParser()

config.read("config.cfg")
config.add_section('twitter_creds')

config.set('twitter_creds','ckey','')
config.set('twitter_creds','csecret','')
config.set('twitter_creds','atoken','')
config.set('twitter_creds','asecret','')

config.add_section('cassandra_creds')

config.set('cassandra_creds','cluster','127.0.0.1')
config.set('cassandra_creds','keyspace','helium')

config.add_section('blue_court')
config.set('blue_court','mlink','http://www.skysports.com/football/tottenham-vs-monaco/live/366860')

with open('config.cfg', 'w') as configfile:
    config.write(configfile)
