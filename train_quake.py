import googleapiclient.discovery
import json
import numpy as np
import os
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
from sklearn.feature_selection import SelectKBest
from sklearn.pipeline import FeatureUnion
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelBinarizer

# Define the format of your input data including unused columns (These are the columns from the census data files)
# The first column is the LABEL which is n/a in the values.csv
columns = ('damage_grade',
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
)

# Categorical columns need to be turned into a numerical value to be used by scikit-learn

numeric_columns = (
    'geo_level_1_id',
    'geo_level_2_id',
    'geo_level_3_id',
    'count_floors_pre_eq',
    'age',
    'area_percentage',
    'height_percentage',
    'count_families'
)


# Load the training census dataset
with open('./earthquake_data/train_values.csv', 'r') as train_feature:
    raw_training_values = pd.read_csv(train_feature, header=None, names=columns[1:])
train_values = raw_training_values.to_numpy().tolist()

with open('./earthquake_data/train_labels.csv', 'r') as train_label:
    raw_training_labels = pd.read_csv(train_label, header=None, names=('building_id', 'damage_grade'))
train_labels = raw_training_labels['damage_grade'].to_numpy().tolist()


# Load the test census dataset
with open('./earthquake_data//test_values.csv', 'r') as test_value:
    raw_test_values = pd.read_csv(test_value, header=None, names=columns[1:])
test_values = raw_test_values.to_numpy().tolist()


# Since the census data set has categorical features, we need to convert them to numerical values.
# We'll use a list of pipelines to convert each categorical column and then
# use FeatureUnion to combine them before calling the RandomForestClassifier.
categorical_pipelines = []

# Each categorical column needs to be extracted individually and converted to a numerical value.
# To do this, each categorical column will use a pipeline that extracts one feature column via
# SelectKBest(k=1) and a LabelBinarizer() to convert the categorical value to a numerical one.
# A scores array (created below) will select and extract the feature column. The scores array is
# created by iterating over the COLUMNS and checking if it is a CATEGORICAL_COLUMN.
for i, col in enumerate(columns[1:]):
    if col not in numeric_columns:
        # Create a scores array to get the individual categorical column.
        # Example:
        #  data = [39, 'State-gov', 77516, 'Bachelors', 13, 'Never-married', 'Adm-clerical',
        #         'Not-in-family', 'White', 'Male', 2174, 0, 40, 'United-States']
        #  scores = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        #
        # Returns: [['Sate-gov']]
        scores = []
        # Build the scores array
        for j in range(len(columns[1:])):
            if i == j:              # This column is the categorical column we want to extract.
                scores.append(1)    # Set to 1 to select this column
            else:                   # Every other column should be ignored.
                scores.append(0)
        skb = SelectKBest(k=1)
        skb.scores_ = scores
        # Convert the categorical column to a numerical value
        lbn = LabelBinarizer()
        r = skb.transform(train_values[1:])
        lbn.fit(r)
        # Create the pipeline to extract the categorical feature
        categorical_pipelines.append(
            ('categorical-{}'.format(i), Pipeline([
                ('SKB-{}'.format(i), skb),
                ('LBN-{}'.format(i), lbn)])))


# Create pipeline to extract the numerical features
skb = SelectKBest(k=len(numeric_columns))

# From COLUMNS use the features that are numerical
skb.scores_ = [0, 1, 1, 1, 1, 1, 1, 1, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
               0, 0, 0, 0, 0, 0, 0, 0, 0
               ]
categorical_pipelines.append(('numerical', skb))

# Combine all the features using FeatureUnion
preprocess = FeatureUnion(categorical_pipelines)

# Create the classifier
classifier = RandomForestClassifier()

# Transform the features and fit them to the classifier
classifier.fit(preprocess.transform(train_values[1:]), train_labels[1:])

# Create the overall model as a single pipeline
pipeline = Pipeline([
    ('union', preprocess),
    ('classifier', classifier)
])

# Export the model to a file
joblib.dump(pipeline, 'model_quake.joblib')

print('Model trained and saved')

