# [START setup]
import datetime
import os
import subprocess
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from google.cloud import storage
import cloudstorage as gcs
import xgboost as xgb
# TODO: REPLACE 'BUCKET_CREATED_ABOVE' with your GCS BUCKET_ID
BUCKET_ID = 'spatial-range-235523-mlengine'
# [END setup]

# ---------------------------------------
# 1. Add code to download the data from GCS (in this case, using the publicly hosted data).
# AI Platform will then be able to use the data when training your model.
# ---------------------------------------

"""
# [START download-data]
earthquake_data_filename = 'train_all_columns_wo_boolean.csv'
# "Public" bucket holding the earthquake data
bucket = storage.Client().bucket('dataprep-staging-2a3e2ace-5f3b-4ea7-8329-25547cdcd64b')
# Path to the data inside the public bucket
data_dir = '/starcraft2@protonmail.com/clean_slate/'
# Download the data
blob = bucket.blob(''.join([data_dir, earthquake_data_filename]))
blob.download_to_filename(earthquake_data_filename)
# [END download-data]
"""

gcs_file = gcs.open('gs://dataprep-staging-2a3e2ace-5f3b-4ea7-8329-25547cdcd64b/starcraft2@protonmail.com/clean_slate/train_all_columns_wo_boolean.csv')
contents = gcs_file.read()


# [START define-and-load-data]
# these are the column labels from the census data files
COLUMNS = {
        'damage_grade',
        'building_id',
        'geo_level_1_id', 'geo_level_2_id', 'geo_level_3_id',
        'count_floors_pre_eq',
        'age',
        'area_percentage',
        'height_percentage',
        'land_surface_condition',
        'foundation_type',
        'roof_type',
        'ground_floor_type',
        'other_floor_type',
        'position',
        'plan_configuration',
        'has_superstructure_adobe_mud',
        'has_superstructure_mud_mortar_stone',
        'has_superstructure_stone_flag',
        'has_superstructure_cement_mortar_stone',
        'has_superstructure_mud_mortar_brick',
        'has_superstructure_cement_mortar_brick',
        'has_superstructure_timber',
        'has_superstructure_bamboo',
        'has_superstructure_rc_non_engineered',
        'has_superstructure_rc_engineered',
        'has_superstructure_other',
        'legal_ownership_status',
        'count_families',
        'has_secondary_use',
        'has_secondary_use_agriculture',
        'has_secondary_use_hotel',
        'has_secondary_use_rental',
        'has_secondary_use_institution',
        'has_secondary_use_school',
        'has_secondary_use_industry',
        'has_secondary_use_health_post',
        'has_secondary_use_gov_office',
        'has_secondary_use_use_police',
        'has_secondary_use_other'
}

# categorical columns contain data that need to be turned into numerical values before being used by XGBoost
NUMERICAL_COLUMNS = {
        'geo_level_1_id',
        'geo_level_2_id',
        'geo_level_3_id',
        'count_floors_pre_eq',
        'age',
        'area_percentage',
        'height_percentage',
        'count_families'
}

CATEGORICAL_COLUMNS = COLUMNS - NUMERICAL_COLUMNS - {'damage_grade'}


# Load the training quake datasets
with open(contents, 'r') as train_data:
    raw_training_data = pd.read_csv(train_data, header=None, names=COLUMNS)
# remove column we are trying to predict ('income-level') from features list
train_features = raw_training_data.drop('damage_grade', axis=1)
# create training labels list
train_labels = raw_training_data['damage_grade']
# [END define-and-load-data]

gcs_file.close()

# [START categorical-feature-conversion]
# Since the census data set has categorical features, we need to convert them to numerical values.
# convert data in categorical columns to numerical values
encoders = {col: LabelEncoder() for col in CATEGORICAL_COLUMNS}

for col in CATEGORICAL_COLUMNS:
    train_features[col] = encoders[col].fit_transform(train_features[col])
# [END categorical-feature-conversion]


# [START load-into-dmatrix-and-train]
# load data into DMatrix object
dtrain = xgb.DMatrix(train_features, train_labels)
# train model
bst = xgb.train({}, dtrain, 20)
# [END load-into-dmatrix-and-train]

# ---------------------------------------
# 2. Train and save the model to GCS
# ---------------------------------------

# [START export-to-gcs]
# Export the model to a file
model = 'model.bst'
bst.save_model(model)
# Upload the model to GCS
bucket = storage.Client().bucket(BUCKET_ID)
blob = bucket.blob('{}/{}'.format(
		datetime.datetime.now().strftime('census_%Y%m%d_%H%M%S'), model))
blob.upload_from_filename(model)
# [END export-to-gcs]


# Django meetup: mvt (model, view, template)

