# Wedding Gallery

## Overview
This project is a public gallery for everyone that wants to 
upload their cute photos (but only the superusers can approve to become visible).


## Quickstart
### Requirements:
* Have a docker distribution installed

* For running the backend, it is requeired a mongodb atlas account and an AWS account

### Running:
First, you need to build the images:

**Frontend** (can be execute without backend):
`cd frontend`
`echo "VUE_APP_API_HOST='http://<the backend host without port>'" > .env.production`(use 52.73.128.255 when running without backend)
`docker build -t gallery-frontend .`
`docker run -p 80:8080 gallery-frontend`


**Backend**:
`docker build -t gallery-backend .`
`docker run -e MONGO_HOST=<atlas mongodb host> -e IS_PRODUCTION=True -e S3_BUCKET=<S3 Bucket name> -p 5000:5000 gallery-backend`






