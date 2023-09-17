Based on https://github.com/iusztinpaul/energy-forecasting

Start Docker
Change directory to airflow/

# Run docker to extract features, train and predict

docker compose up airflow-init
docker compose --env-file .env up --build -d

# Run docker to deploy app

docker compose -f deploy/app-docker-compose.yml --project-directory . up --build