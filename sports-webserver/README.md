# FastApi:
Run the local server with:
uvicorn main:app --reload
API-Documentation: http://127.0.0.1:8000/docs

# Build & Run Docker images (for deployment)
docker build -t sports-api .
docker run -d -p 8000:80 sports-api

# Docker Compose for development (NO DEPLOYMENT:
docker-compose up --build
