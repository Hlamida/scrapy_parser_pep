from pep_parse.constants import PIPELINE_TURN

from pep_parse.constants import RESULTS_DIR

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': PIPELINE_TURN,
}
