import asyncio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.app.models import User, RoleEnum
from api.app.database import Base
from api.app.auth import hash_password

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def seed_admin():
    """
    Seeds the database with an admin user if one does not already exist.
    """
    db = SessionLocal()
    try:
        admin_exists = db.query(User).filter(User.email == "admin@example.com").first()
        if not admin_exists:
            print("Admin user not found, creating one...")
            admin = User(
                name="Admin User",
                email="admin@example.com",
                password_hash=hash_password("admin123"),
                role=RoleEnum.admin,
            )
            db.add(admin)
            db.commit()
            print("Admin user created successfully.")
        else:
            print("Admin user already exists.")
    finally:
        db.close()

if __name__ == "__main__":
    print("Seeding database...")
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    seed_admin()
    print("Database seeding complete.")
