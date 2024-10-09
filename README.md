

# Virtual library

یک کتابحانه مجازی کامل

## پیش‌نیازها

برای اجرای این پروژه، ابتدا باید موارد زیر را بر روی سیستم خود نصب داشته باشید:

- [Docker](https://www.docker.com/get-started)

## مراحل اجرای پروژه

### 1. کلون کردن مخزن (Repository)
ابتدا مخزن پروژه را کلون کنید:

```bash
git clone https://github.com/pooladpoor/Virtual-library.git
```
به دایرکتوری پروژه بروید:
```bash
cd Virtual-library
```

### 2. اجرای پروژه 
ابتدا کانتینر را بسازید :
```bash
docker build -t virtual-library-pooladpoor:latest .   
```
بعد آن را اجرا کنید :
```bash
docker run -p 8000:8000 virtual-library-pooladpoor 
```
## 3.استفاده کنید

- [صفحهه اصلی](http://localhost:8000/)
- [پنل ادمین](http://localhost:8000/admin)
  - National code : 123456789
    - password : 1234

