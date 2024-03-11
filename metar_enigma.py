import pandas as pd
import re

# Sample METARS DataFrame
# data = {'METAR': ['METAR COR EGLL 141450Z AUTO 10006KT 9000 BKN018 BKN023 BKN029 14/12 Q1006 NOSIG=']}
# METARS = pd.DataFrame(data)

# Define a function to extract wind velocity from METAR string
def extract_wind(metar_str):
    wind_regex = r'\b(\d{2})KT\b'  # Regular expression pattern to match wind speed
    wind_match = re.search(wind_regex, metar_str)
    if wind_match:
        return wind_match.group()
    else:
        return None


# Define a function to extract visibility from METAR string
def extract_visibility(metar_str):
    visibility_regex = r' (\d{4}) '  # Regular expression pattern to match visibility
    visibility_match = re.search(visibility_regex, metar_str)
    if visibility_match:
        return visibility_match.group()  # Return the matched group (visibility value)
    else:
        return None