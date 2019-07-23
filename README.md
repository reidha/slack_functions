# slack_functions

```
docker build -t sf .
docker run --name sf -e SLACK_USER_TOKEN=XXX -e SLACK_USER_ID=XXX -it sf
docker run --name sf -e SLACK_USER_TOKEN=XXX -e SLACK_USER_ID=XXX -dit sf sh
docker ps -a
docker rm -f sf

docker start sf
docker exec -it sf sh
```

# Reference

https://qiita.com/pottava/items/452bf80e334bc1fee69a  
https://qiita.com/tanan/items/e79a5dc1b54ca830ac21  

