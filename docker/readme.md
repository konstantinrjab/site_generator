```console
docker build -t site site/
docker run --name site -d -v ${PWD}/site:/usr/share/nginx/html -p 8080:80 site
```
