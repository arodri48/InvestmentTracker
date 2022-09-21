import requests
from requests.exceptions import Timeout
from typing import Dict, Optional
from urllib.parse import urljoin


# from logger import get_logger

# api_obj = GenericApiCaller(url='base/<stuff>?', headers={'content-type': 'application/json'})
	# rsp = api_obj(method='GET', params={'chr': 'some_chr_num'})
	# for elem in rsp.json():
	#	elem[key]
class GenericApiCaller:
	def __init__(self, url: str, headers: Dict = None, is_base: bool = False):
		# self.logger = get_logger(__class__.__name__, tar_lims_dir)
		self.is_base = is_base
		if self.is_base and not url.endswith('/'):
			url += '/'
		self.url = url
		if headers is not None:
			self.headers = headers
		else:
			self.headers = {}

	def __call__(self, method: str, route: str = '', session: Optional[requests.Session] = None, **kwargs):
		# in case of flask routes
		if route.startswith('/'):
			route = route[1:]
		url = self.url
		if self.is_base:
			url = urljoin(url, route, allow_fragments=False)

		headers = kwargs.pop('headers', {})
		headers.update(self.headers)

		try:
			if session:
				rsp = session.post(url, headers=headers, timeout=200, **kwargs)
			else:
				rsp = requests.request(method=method, url=url, headers=headers, timeout=200, **kwargs)
		except requests.exceptions.ConnectionError:
			return Timeout
		except Timeout:
			return Timeout
		except requests.exceptions.RequestException as e:
			raise e

		# if rsp.status_code != 200:
		# 	self.logger.info(f'Response: status={rsp.status_code}\treason={rsp.reason}')
		try:
			rsp.raise_for_status()
		except requests.exceptions.HTTPError:
			return Timeout

		return rsp
