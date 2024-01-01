# First Steps

1. `python -m venv myenv`
2. `pip install django`
3. `django-admin startproject project_name`
4. `python manage.py runserver`
5. git init
6. `python manage.py startapp app_name`
7. add app_name to settings.py -> INSTALLED_APPS = ["app_name"]
8. create folder at project level templates and static
9. `TEMPLATES = { DIRS = [BASE_DIR / "templates"] }`
10. `STATICFILES_DIRS = [ BASE_DIR / "static", ]`
11. change database to postgreSQL
12. `python manage.py makemigrations`
13. `python manage.py magirate`
14. after changing in models.py again run 11 and 12 commands
15. `python manage.py showmigrations`
16. `python manage.py sqlmigrate app_name file-like(0001)`
