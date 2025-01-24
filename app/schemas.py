from datetime import datetime

from pydantic import BaseModel
from typing import List

class WalletInfo(BaseModel):
    wallet_address: str
    trx_balance: float
    bandwidth: float
    energy: float

class WalletQueryResponse(BaseModel):
    id: int
    wallet_address: str
    requested_at: datetime

class PaginatedQueries(BaseModel):
    total: int
    queries: List[WalletQueryResponse]