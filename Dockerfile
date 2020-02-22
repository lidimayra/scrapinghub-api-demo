FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR scrapingapp
COPY scrapingapp/ .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
