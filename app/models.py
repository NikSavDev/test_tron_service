from sqlalchemy import Column, Integer, String, DateTime, func
from app.database import Base

class WalletQuery(Base):
    __tablename__: str = 'wallet_queries'

    id = Column(Integer, primary_key=True)
    wallet_address = Column(String, index=True)
    requested_at = Column(DateTime, server_default=func.now())