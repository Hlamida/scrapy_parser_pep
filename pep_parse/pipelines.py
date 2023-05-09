import csv
import datetime as dt

from collections import defaultdict
from pathlib import Path

from pep_parse.constants import (
    DATETIME_FORMAT, DIALECT_FORMAT, ENCODING_FORMAT, RESULTS_DIR,
)


BASE_DIR = Path(__file__).parents[1]

class PepParsePipeline:

    def open_spider(self, spider):
        self.pre_results = defaultdict(int)

    def process_item(self, item, spider):

        self.pre_results[item['status']] += 1

        return item

    def close_spider(self, spider):
        total = sum(self.pre_results.values())
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formated = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formated}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding=ENCODING_FORMAT) as f:
            writer = csv.writer(
                f, quoting=csv.QUOTE_MINIMAL, dialect=DIALECT_FORMAT,
            )
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(
                [(key, value) for key, value in self.pre_results.items()]
            )
            writer.writerow(['Total', f'{total}'])
