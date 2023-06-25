# url-shortening_service_fastapi_mongodb
The backend for the url shortening service with MongoDB instead of inmemory caching


## Installation Instructions:
   * Create a virutal environment:
     * pip install -r requirements.txt
   * Via Docker installation also possible:
     docker compose up  

## MongoDB:
   * Install MongoDB from here: https://www.mongodb.com/docs/manual/installation/ &&
     use the MongoDB atlas with a free tier cluster: https://www.mongodb.com/atlas/database?tck=docs_server

## Run:
   * uvicorn main:app --reload then on  http://127.0.0.1:8000 you should see the api endpoints with Swagger UI
     Type: http://127.0.0.1:8000/docs# on browser.
     

## Development Philosophy:
    For small projects I avoid deploying on AWS Cloud using stuffs like AWS Elasticbean with Codepipline automation from aws.
    Plus, development clouds like Heroku and Digital Ocean charge 7 USD for just storage and running apps like Django and FastAPI
    so I hacked my way to deploying Django and FastAPI on vercel and it works.

## Preview
   ![](docs/fastapi_swagger_AdobeExpress.gif) 