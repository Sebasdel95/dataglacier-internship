import os
import logging
import pandas as pd
import yaml

################
# File Reading #
################

def read_config_file(filepath):
    with open(filepath, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)


def col_header_val(df,table_config):
    '''
    replace whitespaces
    in column names 
    '''
    df.columns = list(map(lambda x: x.replace(' ',''), list(df.columns)))
    expected_col = list(table_config['columns'])
    expected_col.sort()
    cols = df.columns.tolist()
    cols.sort()
    if len(df.columns) == len(expected_col) and list(expected_col)  == list(cols):
        print("column name and column length validation passed")
        return 1
    else:
        print("column name and column length validation failed")
        mismatched_columns_file = list(set(cols).difference(expected_col))
        print("Following File columns are not in the YAML file",mismatched_columns_file)
        missing_YAML_file = list(set(expected_col).difference(cols))
        print("Following YAML columns are not in the file uploaded",missing_YAML_file)
        logging.info(f'df columns: {cols}')
        logging.info(f'expected columns: {expected_col}')
        return 0
