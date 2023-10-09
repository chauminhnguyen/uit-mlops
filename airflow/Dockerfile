FROM apache/airflow:2.7.0-python3.10

ARG CURRENT_USER=$USER

USER root
# Install Python dependencies to be able to process the wheels from the private PyPI server.
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3-distutils
RUN apt-get install -y python3-dev build-essential
# RUN pip3 install mlops_batch_prediction_pipeline
# RUN pip3 install mlops_training_pipeline
# RUN pip3 install mlops_feature_pipeline

USER ${CURRENT_USER}
