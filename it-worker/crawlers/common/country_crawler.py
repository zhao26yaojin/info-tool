from crawlers.cus_base import CusCrawlerBase
from models.common.country import Country
from storage.storage_handle import StorageHandle

class CountryCrawler(CusCrawlerBase[Country]):
	def __init__(self):
		super().__init__('country')

	def crawl(self):
		self.handle_storage()

		self.handle_rel_id()

	def handle_storage(self):
		storage = StorageHandle()

		logos = [r.logo for r in self.results]

		# 一次性拉取已存在的 key, 避免每个 logo 都发一次 head_object
		key_prefix = f'logo/{self.table}/'

		existing_keys = storage.get_exist_keys(key_prefix)
		logo_refs = storage.save_files(set(logos), existing_keys, key_prefix)

		# 上传失败的丢弃; 成功的把原始 URL 替换为 s3://bucket/key 引用
		self.results = [r for r in self.results if r.logo in logo_refs]
		for r in self.results:
			r.logo = logo_refs[r.logo]

	def handle_rel_id(self):
		pass


