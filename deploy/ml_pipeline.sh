#!/bin/bash

# Build and publish the feature-pipeline, training-pipeline, and batch-prediction-pipeline packages.
# This is done so that the pipelines can be run from the CLI.
# The pipelines are executed in the feature-pipeline, training-pipeline, and batch-prediction-pipeline
# directories, so we must change directories before building and publishing the packages.
# The my-pypi repository must be defined in the project's poetry.toml file.

cd mlops_feature_pipeline
poetry build
poetry publish -r my-pypi

cd ../mlops_training_pipeline
poetry build
poetry publish -r my-pypi

cd ../mlops_batch_prediction_pipeline
poetry build
poetry publish -r my-pypi