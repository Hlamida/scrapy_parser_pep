import csv
import datetime as dt

from collections import defaultdict
from itemadapter import ItemAdapter
from pathlib import Path

from pep_parse.constants import (
    DATETIME_FORMAT, DIALECT_FORMAT, ENCODING_FORMAT,
    OUTPUT_FORMS,
)


BASE_DIR = Path(__file__).parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.total = 0
        self.pre_results = defaultdict(int)
        self.pre_results['Статус'] = 'Количество'

    def process_item(self, item, spider):

        self.pre_results[item['status']] += 1
        self.total += 1

        return item

    def close_spider(self, spider):
        self.pre_results['Total'] = self.total
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formated = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formated}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding=ENCODING_FORMAT) as f:
            writer = csv.writer(f, dialect=DIALECT_FORMAT)
            writer.writerows(
                [(key, value) for key, value in self.pre_results.items()]
            )
