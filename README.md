## Demo app that consumes Scrapinghub API
Quite simple app to demonstrate Scrapinghub API basic features.

## Pre-requisites
- Python 3.6

## Installing
```
$ git clone git@github.com:lidimayra/scrapinghub-api-demo.git && cd scrapinghub-api-demo
$ pip install -r requirements.txt
```

## Setup
Export required environment variables:

```
$ export FLASK_ENV=development
$ export APIKEY=<Scrapinghub API key>
$ export JOB_ID=<Scrapinghub Job ID>
```

## To run application
```
$ flask run
```
