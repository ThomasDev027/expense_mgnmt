from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models import Categories


class CategoryService:

    def get_categories(
        self,
        db: Session,
    ) -> list[Categories]:

        return list(
            db.scalars(
                select(Categories)
                .where(Categories.is_active.is_(True))
                .order_by(Categories.id.asc())
            ).all()
        )


category_service = CategoryService()
