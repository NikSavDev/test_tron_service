from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.services import get_wallet_info
from app.database import SessionLocal
from app.models import WalletQuery
from app.schemas import WalletInfo, PaginatedQueries

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/wallet", response_model=WalletInfo)
def get_wallet(wallet_address: str = Query(...), db: Session = Depends(get_db)):
    wallet_info = get_wallet_info(wallet_address)
    if "error" in wallet_info:
        raise HTTPException(status_code=404, detail=wallet_info["error"])

    query = WalletQuery(wallet_address=wallet_address)
    db.add(query)
    db.commit()
    db.refresh(query)

    return wallet_info



@router.get("/queries", response_model=PaginatedQueries)
def get_queries(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    total = db.query(WalletQuery).count()
    queries = db.query(WalletQuery).offset(skip).limit(limit).all()

    return {
        "total": total,
        "queries": queries,
    }
