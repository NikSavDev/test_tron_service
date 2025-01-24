import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import WalletQuery, Base


SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

def test_create_wallet_query(test_db):
    query = WalletQuery(wallet_address="TXXXXXXX")
    test_db.add(query)
    test_db.commit()

    assert test_db.query(WalletQuery).count() == 1
