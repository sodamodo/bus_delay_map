# project ID: bus-delay-208318


# login to gcloud
# gcloud auth login
gcloud config set project bus-delay-208318
gcloud container clusters get-credentials bus-cluster --zone us-west1-a --project bus-delay-208318


# docker build -t database -f database/Dockerfile .
# docker tag database gcr.io/bus-delay-208318/database:v2
# docker push gcr.io/bus-delay-208318/database:v2

docker build -t database -f backend/Dockerfile .
docker tag database gcr.io/bus-delay-208318/backend:v2
docker push gcr.io/bus-delay-208318/backend:v2
