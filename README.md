## App demo que consome a API do Scrapinghub
App bem simples para demonstrar as funcionalidades básicas da
API do Scrapinghub

### Pré-requisitos
- [Python](https://www.python.org/) >= 3.6


## Instalação
```
$ git clone git@github.com:lidimayra/scrapinghub-api-demo.git && cd scrapinghub-api-demo
$ pip install -r requirements.txt
```

## Configurações
Exporte as variáveis de ambiente necessárias:

```
$ export FLASK_ENV=development
$ export APIKEY=<Scrapinghub API key>
$ export JOB_ID=<Scrapinghub Job ID>
```

## Para rodar a aplicação
```
$ flask run
```
