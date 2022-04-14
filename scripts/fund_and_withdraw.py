from brownie import FundMe
from scripts.helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"The entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": get_account(), "value": entrance_fee})


def main():
    fund()
