from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.exceptions import AddressNotFound

client = Tron(provider=HTTPProvider(api_key='bc8c5982-6d18-4ff9-b3d3-4b9ff50e8947'))


def get_wallet_info(addr: str):
    try:
        account = client.get_account(addr)
        bandwidth = client.get_bandwidth(addr)
        energy = client.get_account_resource(addr).get('EnergyLimit', 0)

        trx_balance = account.get("balance", 0) / 1_000_000

        return {
            "wallet_address": addr,
            "trx_balance": trx_balance,
            "bandwidth": bandwidth,
            "energy": energy,
        }
    except AddressNotFound:
        return {'error': 'Wallet not found'}