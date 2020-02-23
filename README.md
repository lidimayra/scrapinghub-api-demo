# App demo que consome a API do Scrapinghub
App bem simples para demonstrar as funcionalidades básicas da
API do Scrapinghub

## Configurações
Faça uma cópia do arquivo `scrapingapp/.env.sample` chamada `scrapingapp/.env`
atualizando com os seus dados a chave do Scrapinghub e o Job ID.

## Rodando a aplicação com o Docker
```
$ git clone git@github.com:lidimayra/scrapinghub-api-demo.git && cd scrapinghub-api-demo
$ docker build -t scrapingapp .
$ docker run -p 5000:5000 scrapingapp
```

## Rodando a aplicação localmente

**Pré-requisito**: [Python](https://www.python.org/) >= 3.6

```
$ git clone git@github.com:lidimayra/scrapinghub-api-demo.git && cd scrapinghub-api-demo
$ pip install -r requirements.txt
$ flask run
```
