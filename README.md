# Sample app to demo Scrapinghub API usage
A very simple flask app created to demo basic funcionality when working with Scrapinghub API

## Setup
Clone the repository and navigate to its directory:

```
git clone git@github.com:lidimayra/scrapinghub-api-demo.git && cd scrapinghub-api-demo
```

Copy the `scrapingapp/.env.sample` file and name it as `scrapingapp/.env`.

```
cp scrapingapp/.env.sample scrapingapp/.env
```

Update the `APIKEY` and `PROJECT_ID` values on it to match the ones provided to you on Scrapinghub dashboard.

## Run it on docker
Build the docker imagine and spin up a container:

```
docker build -t scrapingapp .
docker run -p 5000:5000 scrapingapp
```

## Run it locally

**Pre-requisite**: [Python](https://www.python.org/) >= 3.13.1

```
cd scrapingapp
pip install -r requirements.txt
flask run
```
