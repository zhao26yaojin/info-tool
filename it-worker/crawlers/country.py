from crawlers.cus_base import CusCrawlerBase
from models.country import Country
from utils.cus_data_util import CRAWL_DICT


class CountryCrawler(CusCrawlerBase[Country]):
    def crawl(self):
        for match_data in self.match_datas:
            if match_data in CRAWL_DICT:
                self.results.append(Country(match_data.get('id'), match_data.get('name')))