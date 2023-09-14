Start Docker
Change directory to airflow/
Run 
docker compose up airflow-init
docker compose --env-file .env up --build -d
