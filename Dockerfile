# استفاده از ایمیج رسمی Python به عنوان base image
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# تنظیم کردن یک دایرکتوری کاری در کانتینر
WORKDIR /app

# کپی کردن فایل‌های `requirements.txt` و نصب وابستگی‌ها
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# کپی کردن کل پروژه به دایرکتوری کاری
COPY . /app/

# باز کردن پورت ۸۰۰۰ برای دسترسی به جنگو در مرورگر
EXPOSE 8000

#ENV DJANGO_SUPERUSER_PASSWORD=admin
#CMD python manage.py makemigrations --noinput && \
#    python manage.py migrate --noinput && \
#    python manage.py createsuperuser --user admin --email admin@localhost --noinput; \
#    gunicorn -b 0.0.0.0:8000 config.wsgi

# دستور پیش‌فرض برای اجرای سرور جنگو
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
