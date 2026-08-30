# ========================================
# FastAPI Imports
# ========================================

from fastapi import APIRouter


# ========================================
# Route Imports
# ========================================

from routes.health import router as health_router

from modules.auth.router import router as auth_router
from modules.users.router import router as users_router
from modules.categories.router import router as category_router
from modules.transactions.router import router as transaction_router
from modules.budgets.router import router as budget_router
from modules.accounts.router import router as account_router


# ========================================
# API Router
# ========================================

api_router = APIRouter(
    prefix="/api/v1",
)


# ========================================
# Application Routers
# ========================================

routers = [
    health_router,
    auth_router,
    users_router,
    category_router,
    transaction_router,
    budget_router,
    account_router,
]


# ========================================
# Register Routers
# ========================================

for router in routers:
    api_router.include_router(router)
