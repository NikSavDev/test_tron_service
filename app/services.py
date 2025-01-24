from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.exceptions import AddressNotFound
from app.config import settings


client = Tron(provider=HTTPProvider(api_key=settings.api_key))


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