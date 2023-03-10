Introduction
Text sentiment analyzer

Docker Image Build
docker image build -t text-sentiment-analyzer .

Docker Run
docker container run -d --rm --name text-sentiment -p 9005:9005 text-sentiment-analyzer
