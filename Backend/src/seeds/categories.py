# ========================================
# Category Seeds
# ========================================

from sqlalchemy import select

from sqlalchemy.orm import Session
from src.models.categories import Categories


# ========================================
# Category Seed Data
# ========================================

categories = [
    {
        "name": "Food",
        "description": "Food and groceries",
    },
    {
        "name": "Transport",
        "description": "Transport and fuel",
    },
    {
        "name": "Shopping",
        "description": "Shopping and purchases",
    },
    {
        "name": "Bills",
        "description": "Utilities and bills",
    },
    {
        "name": "Entertainment",
        "description": "Movies, games, and entertainment",
    },
    {
        "name": "Health",
        "description": "Medical and healthcare",
    },
    {
        "name": "Education",
        "description": "Education and learning",
    },
    {
        "name": "Salary",
        "description": "Salary and income",
    },
    {
        "name": "Other",
        "description": "Other transactions",
    },
]


# ========================================
# Seed Categories
# ========================================

def seed_categories(session: Session) -> None:

    try:
        for category_data in categories:

            existing_category = session.scalar(
                select(Categories).where(
                    Categories.name == category_data["name"]
                )
            )

            if not existing_category:
                session.add(
                    Categories(
                        name=category_data["name"],
                        description=category_data["description"],
                    )
                )

        session.commit()

    finally:
        session.close()
