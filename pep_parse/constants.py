from pathlib import Path


# urls
WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'
MAIN_DOC_URL = 'https://docs.python.org/3/'
DOWNLOADS_URL = 'https://docs.python.org/3/download.html'
MAIN_PEPS_URL = 'https://peps.python.org/'

# formats
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
LOG_FORMAT = '"%(asctime)s - [%(levelname)s] - %(message)s"'
DT_FORMAT = '%d.%m.%Y %H:%M:%S'
ENCODING_FORMAT = 'utf-8'
DIALECT_FORMAT = 'unix'

# dirs & files
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / 'logs'
LOG_FILE = LOG_DIR / 'parser.log'
RESULTS_DIR = BASE_DIR / 'results'
DOWNLOADS_DIR = BASE_DIR / 'downloads'

# choises
OUTPUT_FORMS = ('pretty', 'file')
EXPECTED_STATUS = {
    'A': ('Active', 'Accepted'),
    'D': ('Deferred',),
    'F': ('Final',),
    'P': ('Provisional',),
    'R': ('Rejected',),
    'S': ('Superseded',),
    'W': ('Withdrawn',),
    '': ('Draft', 'Active'),
}
