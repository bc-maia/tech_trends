# Docker Commands

## Docker command used to build the application

```shell
docker build -t techtrends:1.0 .
```

## Docker command used to run the application

```shell
docker run -d --rm -p 7111:3111 --name techtrends techtrends:1.0
```

## Docker command used to get the application logs

```terminal
docker logs -f techtrends
```

___

## Logs from the container running the TechTrends application

```shell
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
WARNING:werkzeug: * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
INFO:werkzeug: * Running on http://172.17.0.2:3111/ (Press CTRL+C to quit)
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:38:11] "GET /healthz HTTP/1.1" 200 -
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:38:14] "GET /metrics HTTP/1.1" 200 -
INFO:app:[15/02/2022, 15:38:55] Retrieving `About` Page.
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:38:55] "GET /about HTTP/1.1" 200 -
INFO:app:[15/02/2022, 15:39:02] Article Not Found.
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:39:02] "GET /55 HTTP/1.1" 404 -
INFO:app:[15/02/2022, 15:39:12] Article "CNCF Cloud Native Definition v1.0" retrieved!
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:39:12] "GET /5 HTTP/1.1" 200 -
INFO:app:[15/02/2022, 15:40:11] New Article Added.
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:40:11] "POST /create HTTP/1.1" 302 -
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:40:11] "GET / HTTP/1.1" 200 -
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:40:22] "POST /7 HTTP/1.1" 405 -
INFO:app:[15/02/2022, 15:40:30] Article "test post number one" retrieved!
INFO:werkzeug:172.17.0.1 - - [15/Feb/2022 15:40:30] "GET /7 HTTP/1.1" 200 -
```
