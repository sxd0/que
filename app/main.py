from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from sqladmin import Admin
from app.database import engine
from app.admin.auth import authentication_backend
from app.admin.views import BookmarkAdmin, NotificationAdmin, QuestionTagsAdmin, SubscriptionAdmin, TagsAdmin, UserAdmin, PostAdmin, RoleAdmin, VotesAdmin




app = FastAPI()


# origins = [
#     "http://localhost/5173"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
#                     "Access-Control-Allow-Origin", "Authorization"]
# )


admin = Admin(app, engine, authentication_backend=authentication_backend)

admin.add_view(UserAdmin)
admin.add_view(PostAdmin)
admin.add_view(RoleAdmin)
admin.add_view(TagsAdmin)
admin.add_view(QuestionTagsAdmin)
admin.add_view(VotesAdmin)
admin.add_view(NotificationAdmin)
admin.add_view(BookmarkAdmin)
admin.add_view(SubscriptionAdmin)



@app.get("/")
async def root():
    return {"message": "QueStudio is running!"}


# База данных разворачивается только через докер

# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head

# Создание миграций
# docker exec -it app alembic revision --autogenerate -m "Initial migration"

# Применение миграций
# docker exec -it app alembic upgrade head

# Удаление (откат) миграций
# docker exec -it app alembic downgrade -1
# Или для отката до определенной версии
# docker exec -it app alembic downgrade <revision_id>

# Выполните скрипт
# docker exec -it db psql -U postgres -d QueStudio_db -f /app/seed.sql

# Быстрая проверка данных
# docker exec -it db psql -U postgres -d QueStudio_db -c "SELECT * FROM roles;"
# docker exec -it db psql -U postgres -d QueStudio_db -c "\dt"

# Зайти в контейнер
# docker exec -it db psql -U postgres -d QueStudio_db


# Примечание
# При запуске проверять папку migrations/versions там обычно лежит миграция
# Далее команды только на принятие миграций и заполнения бд и все