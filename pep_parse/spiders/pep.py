import re
import scrapy

from urllib.parse import urljoin

from pep_parse.constants import MAIN_PEPS_URL
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Паук для парсинга PEP."""

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Собирает ссылки на PEP с главной страницы."""

        all_peps = response.css(
            '#numerical-index a[href^="pep"]::attr(href)'
        ).getall()
        for short_link in all_peps[:10]:
            pep_link = urljoin(MAIN_PEPS_URL, short_link)
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает данные по каждому PEP для дальнейшей обработки."""

        page_title = response.css('h1.page-title::text').get()
        parsed_number = int(re.findall(r'\d+', page_title)[0])
        parsed_name = re.sub(r'PEP \d+ \S', ' ', page_title).strip()
        parsed_status = response.css('abbr::text').get()
        data = {
            'number': parsed_number,
            'name': parsed_name,
            'status': parsed_status,
        }
        yield PepParseItem(data)
