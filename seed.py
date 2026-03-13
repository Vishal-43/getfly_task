from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import sys
import os

load_dotenv()

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from api.app.models import User, RoleEnum
from api.app.database import Base
from api.app.auth import hash_password

DB_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(DB_URL)
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
   
    Base.metadata.create_all(bind=engine)
    seed_admin()
    print("Database seeding complete.")
