import os

from flask import Flask
from flask import render_template

from scrapinghub import ScrapinghubClient

app = Flask(__name__)

@app.route('/')
def index():
    apikey = os.environ.get("APIKEY")
    job_id = os.environ.get("JOB_ID")

    client = ScrapinghubClient(apikey)
    job = client.get_job(job_id)

    data = []

    for item in job.items.iter():
        dict = {
            'title': item['title'][0],
            'director': item['director'][0],
            'summary': item['summary'][0]
        }
        data.append(dict)

    return render_template('index.html', data=data)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
