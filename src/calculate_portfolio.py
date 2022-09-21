import argparse
import csv
from typing import List, Dict


class CalculatePortfolio:
	def __init__(self, portfolio_inpath: str):
		self.portfolio_inpath = portfolio_inpath
		self.investment_portfolio: List[Dict] = []

	def load_portfolio(self) -> None:
		with open(self.portfolio_inpath, 'r') as f:
			portfolio_reader = csv.DictReader(f, fieldnames=['asset_name', 'num_units'], delimiter='\t')
			self.investment_portfolio = [row for row in portfolio_reader]

	def query_price(self) -> None:
		for investment in self.investment_portfolio:
			# query price
			# TODO: implement this using API
			investment_price = 15
			# save price in dictionary
			investment['price'] = investment_price

	def print_investment_summary(self) -> None:
		print("Name\tNum_Units\tPrice\tTotal_Value")
		for investment in self.investment_portfolio:
			total_val = float(investment['num_units']) * investment['price']
			# TODO: add formatting of price and total value
			output_str = f"{investment['asset_name']}\t{investment['num_units']}\t${investment['price']}\t${total_val}"
			print(output_str)

	def calculate_portfolio(self) -> None:
		# Step 1: Load investment name, type, and quantity of investment
		self.load_portfolio()

		# Step 2: Load the price for each investment from database
		self.query_price()

		# Step 3: Print summary statistics
		self.print_investment_summary()


if __name__ == "__main__":
	# parser = argparse.ArgumentParser(description="CLI for InvestmentTracker")
	# parser.add_argument('-i', '--portfolio_inpath', required=True)
	# CalculatePortfolio(**vars(parser.parse_args())).calculate_portfolio()
	CalculatePortfolio("/Users/arodriguez/Desktop/InvestmentTracker/test_input.txt").calculate_portfolio()
