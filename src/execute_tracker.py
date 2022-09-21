import os
from typing import List, Dict

from src.api.general_api_caller import GenericApiCaller

PORTFOLIO = [
	{'ticker': 'VTI', 'allocation': 0.6},
	{'ticker': 'VXUS', 'allocation': 0.25},
	{'ticker': 'AVUV', 'allocation': 0.1},
	{'ticker': 'AVDV', 'allocation': 0.05}
]


def _get_local_env_vars(env_name: str) -> str:
	msg = f'Environment variable "{env_name}" is not currently set, please set variable in environment'
	try:
		env = os.environ[env_name]
		return env
	except KeyError as e:
		raise KeyError(msg) from e


class ExecuteTracker:
	def __init__(self, portfolio: List[Dict], total_investment: float):
		self.portfolio = portfolio
		self.total_investment = total_investment
		self.api_key = _get_local_env_vars("POLYGON_IO_API_KEY")

	def get_stock_info(self) -> List[Dict]:
		stock_info = []
		for stock in self.portfolio:
			api_obj = GenericApiCaller(url=f'https://api.polygon.io/v2/aggs/ticker/{stock["ticker"]}/prev?',
									   headers={'content-type': 'application/json'})
			rsp = api_obj(method='GET', params={'adjusted': 'true', 'apiKey': self.api_key})
			results = rsp.json()
			stock_info.append(
				{'ticker': stock['ticker'], 'allocation': stock['allocation'], 'close_price': results['results'][0]['c']})
		return stock_info

	def runner(self):
		# Step 1: Load stock information
		stock_data = self.get_stock_info()
		# Step 2: Print Information
		for stock_info in stock_data:
			fraction_shares = self.total_investment * stock_info['allocation'] / stock_info['close_price']
			print(f'{stock_info["ticker"]} shares: {fraction_shares}')


if __name__ == "__main__":
	ExecuteTracker(PORTFOLIO, 10933).runner()
