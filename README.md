TaskBoard — коротко про проект на Django с JWT и задачами.

## Запуск
```bash
python -m venv venv
source venv/bin/activate  # на Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API
- `/api/users/` — регистрация и список (для админов);
- `/api/users/me/` — ваш профиль;
- `/api/tasks/` — CRUD по задачам, есть фильтры `status`, `assignee`, `search`;
- `/api/login/` и `/api/login/refresh/` — токены.
