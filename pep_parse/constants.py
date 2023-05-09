from pathlib import Path


# urls
MAIN_PEPS_URL = 'https://peps.python.org/'

# formats
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
ENCODING_FORMAT = 'utf-8'
DIALECT_FORMAT = 'unix'

# dirs & files
BASE_DIR = Path(__file__).parents[1]
RESULTS_DIR = BASE_DIR / 'results'

# settings
PIPELINE_TURN = 300
