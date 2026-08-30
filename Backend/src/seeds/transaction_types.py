# ========================================
# Transaction Category & Type Seed
# ========================================

from sqlalchemy.orm import Session

from src.models.transaction_categories import TransactionCategory
from src.models.transaction_type import TransactionType


# ========================================
# Seed Data
# ========================================

TRANSACTION_CATEGORIES = [
    # ============================================================
    # Income
    # ============================================================

    {
        "name": "Income",
        "slug": "income",
        "description": "Money received by the user",
        "types": [
            {
                "name": "Salary",
                "slug": "salary",
                "description": "Regular employment salary",
            },
            {
                "name": "Freelance",
                "slug": "freelance",
                "description": "Freelance or contract income",
            },
            {
                "name": "Business Income",
                "slug": "business-income",
                "description": "Income received from business activities",
            },
            {
                "name": "Interest",
                "slug": "interest",
                "description": "Interest earned from savings or investments",
            },
            {
                "name": "Dividend",
                "slug": "dividend",
                "description": "Dividend income from investments",
            },
            {
                "name": "Bonus",
                "slug": "bonus",
                "description": "Bonus or incentive payment",
            },
            {
                "name": "Gift",
                "slug": "gift",
                "description": "Money received as a gift",
            },
            {
                "name": "Refund",
                "slug": "refund",
                "description": "Refund received from a merchant or service",
            },
            {
                "name": "Other Income",
                "slug": "other-income",
                "description": "Other sources of income",
            },
        ],
    },

    # ============================================================
    # Expense
    # ============================================================

    {
        "name": "Expense",
        "slug": "expense",
        "description": "Money spent by the user",
        "types": [
            # --------------------------------------------------------
            # Food
            # --------------------------------------------------------

            {
                "name": "Groceries",
                "slug": "groceries",
                "description": "Supermarket and grocery purchases",
            },
            {
                "name": "Restaurant",
                "slug": "restaurant",
                "description": "Restaurant and dining expenses",
            },
            {
                "name": "Fast Food",
                "slug": "fast-food",
                "description": "Fast food and takeaway",
            },
            {
                "name": "Coffee",
                "slug": "coffee",
                "description": "Coffee, tea and beverages",
            },

            # --------------------------------------------------------
            # Housing
            # --------------------------------------------------------

            {
                "name": "Rent",
                "slug": "rent",
                "description": "House or apartment rent",
            },
            {
                "name": "Home Maintenance",
                "slug": "home-maintenance",
                "description": "House maintenance and repairs",
            },
            {
                "name": "Property Tax",
                "slug": "property-tax",
                "description": "Property tax payments",
            },

            # --------------------------------------------------------
            # Transportation
            # --------------------------------------------------------

            {
                "name": "Fuel",
                "slug": "fuel",
                "description": "Petrol, diesel or other vehicle fuel",
            },
            {
                "name": "Taxi",
                "slug": "taxi",
                "description": "Taxi and cab expenses",
            },
            {
                "name": "Public Transport",
                "slug": "public-transport",
                "description": "Bus, train and metro expenses",
            },
            {
                "name": "Parking",
                "slug": "parking",
                "description": "Parking fees",
            },
            {
                "name": "Vehicle Maintenance",
                "slug": "vehicle-maintenance",
                "description": "Vehicle servicing and repairs",
            },

            # --------------------------------------------------------
            # Bills & Utilities
            # --------------------------------------------------------

            {
                "name": "Electricity",
                "slug": "electricity",
                "description": "Electricity bill",
            },
            {
                "name": "Water",
                "slug": "water",
                "description": "Water bill",
            },
            {
                "name": "Internet",
                "slug": "internet",
                "description": "Internet bill",
            },
            {
                "name": "Mobile Phone",
                "slug": "mobile-phone",
                "description": "Mobile phone bill",
            },
            {
                "name": "Gas",
                "slug": "gas",
                "description": "Gas bill",
            },

            # --------------------------------------------------------
            # Healthcare
            # --------------------------------------------------------

            {
                "name": "Doctor",
                "slug": "doctor",
                "description": "Doctor consultation expenses",
            },
            {
                "name": "Medicine",
                "slug": "medicine",
                "description": "Medicine and pharmacy expenses",
            },
            {
                "name": "Hospital",
                "slug": "hospital",
                "description": "Hospital expenses",
            },
            {
                "name": "Dental",
                "slug": "dental",
                "description": "Dental care expenses",
            },

            # --------------------------------------------------------
            # Education
            # --------------------------------------------------------

            {
                "name": "Tuition",
                "slug": "tuition",
                "description": "School or college tuition",
            },
            {
                "name": "Books",
                "slug": "books",
                "description": "Books and study materials",
            },
            {
                "name": "Courses",
                "slug": "courses",
                "description": "Online and offline courses",
            },

            # --------------------------------------------------------
            # Shopping
            # --------------------------------------------------------

            {
                "name": "Clothing",
                "slug": "clothing",
                "description": "Clothes and footwear",
            },
            {
                "name": "Electronics",
                "slug": "electronics",
                "description": "Electronic devices and accessories",
            },
            {
                "name": "Home Shopping",
                "slug": "home-shopping",
                "description": "Home and household purchases",
            },

            # --------------------------------------------------------
            # Entertainment
            # --------------------------------------------------------

            {
                "name": "Movies",
                "slug": "movies",
                "description": "Movies and cinema",
            },
            {
                "name": "Games",
                "slug": "games",
                "description": "Video games and gaming",
            },
            {
                "name": "Events",
                "slug": "events",
                "description": "Events and activities",
            },

            # --------------------------------------------------------
            # Subscriptions
            # --------------------------------------------------------

            {
                "name": "Streaming",
                "slug": "streaming",
                "description": "Video and music streaming services",
            },
            {
                "name": "Software",
                "slug": "software",
                "description": "Software subscriptions",
            },
            {
                "name": "Memberships",
                "slug": "memberships",
                "description": "Gym and other memberships",
            },

            # --------------------------------------------------------
            # Travel
            # --------------------------------------------------------

            {
                "name": "Flights",
                "slug": "flights",
                "description": "Flight tickets",
            },
            {
                "name": "Hotels",
                "slug": "hotels",
                "description": "Hotel and accommodation",
            },
            {
                "name": "Travel Food",
                "slug": "travel-food",
                "description": "Food expenses during travel",
            },

            # --------------------------------------------------------
            # Insurance
            # --------------------------------------------------------

            {
                "name": "Health Insurance",
                "slug": "health-insurance",
                "description": "Health insurance premiums",
            },
            {
                "name": "Vehicle Insurance",
                "slug": "vehicle-insurance",
                "description": "Vehicle insurance premiums",
            },
            {
                "name": "Life Insurance",
                "slug": "life-insurance",
                "description": "Life insurance premiums",
            },

            # --------------------------------------------------------
            # Other Expenses
            # --------------------------------------------------------

            {
                "name": "Taxes",
                "slug": "taxes",
                "description": "Tax payments",
            },
            {
                "name": "Bank Fees",
                "slug": "bank-fees",
                "description": "Bank and financial service fees",
            },
            {
                "name": "Personal Care",
                "slug": "personal-care",
                "description": "Personal care expenses",
            },
            {
                "name": "Pets",
                "slug": "pets",
                "description": "Pet-related expenses",
            },
            {
                "name": "Other Expense",
                "slug": "other-expense",
                "description": "Other expenses",
            },
        ],
    },

    # ============================================================
    # Transfer
    # ============================================================

    {
        "name": "Transfer",
        "slug": "transfer",
        "description": "Movement of money between accounts",
        "types": [
            {
                "name": "Bank Transfer",
                "slug": "bank-transfer",
                "description": "Transfer between bank accounts",
            },
            {
                "name": "Cash Withdrawal",
                "slug": "cash-withdrawal",
                "description": "Cash withdrawn from an account",
            },
            {
                "name": "Cash Deposit",
                "slug": "cash-deposit",
                "description": "Cash deposited into an account",
            },
            {
                "name": "Account Transfer",
                "slug": "account-transfer",
                "description": "Transfer between user's own accounts",
            },
        ],
    },
]


# ========================================
# Seed Function
# ========================================

def seed_transaction_categories(
    session: Session,
) -> None:
    """
    Seed transaction categories and transaction types.

    Safe to run multiple times.
    Existing records are not duplicated.
    """

    for category_data in TRANSACTION_CATEGORIES:

        # ========================================================
        # Find Existing Category
        # ========================================================

        category = (
            session.query(TransactionCategory)
            .filter(
                TransactionCategory.slug == category_data["slug"]
            )
            .first()
        )

        # ========================================================
        # Create Category
        # ========================================================

        if category is None:
            category = TransactionCategory(
                name=category_data["name"],
                slug=category_data["slug"],
                description=category_data.get("description"),
                is_active=True,
            )

            session.add(category)
            session.flush()

        # ========================================================
        # Create Transaction Types
        # ========================================================

        for type_data in category_data["types"]:

            transaction_type = (
                session.query(TransactionType)
                .filter(
                    TransactionType.slug == type_data["slug"]
                )
                .first()
            )

            if transaction_type is not None:
                continue

            transaction_type = TransactionType(
                category_id=category.id,
                name=type_data["name"],
                slug=type_data["slug"],
                description=type_data.get("description"),
                is_active=True,
            )

            session.add(transaction_type)

    # ============================================================
    # Commit
    # ============================================================

    session.commit()
