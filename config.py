import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost:5432/stock_watchlist_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "e7c58edd548d67b150b66f9bb47b302a410f347fba11ce0e84e3a2804a943e9c")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "67485f42ac9c63c7c538c159b6600f9fc346b3bfd5500cd929b7c6d17126ad8b")

