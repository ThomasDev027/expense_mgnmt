from sqlalchemy import select

from src.core.database import SessionLocal
from src.models.role import Role
from sqlalchemy.orm import Session


def seed_roles(session: Session) -> None:
    # db = SessionLocal()

    try:
        roles = [
            {
                "name": "admin",
                "description": "Administrator with full system access",
            },
            {
                "name": "user",
                "description": "Standard user with normal system access",
            },
        ]

        for role_data in roles:
            role = session.scalar(
                select(Role).where(
                    Role.name == role_data["name"]
                )
            )

            if role:
                role.description = role_data["description"]
            else:
                session.add(
                    Role(
                        name=role_data["name"],
                        description=role_data["description"],
                    )
                )

        session.commit()

    finally:
        session.close()


if __name__ == "__main__":
    seed_roles()
