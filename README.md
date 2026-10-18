# 💊 Pharmacy Tracker System | نظام إدارة ومتابعة الصيدليات

[English](#english-version) | [العربية](#النسخة-العربية)

---

## English Version

### 📝 Description

**Pharmacy Tracker** is a robust Backend RESTful API built using **Python**, **Django**, and **Django REST Framework (DRF)**. It simplifies pharmacy management by tracking medicine inventory, stock levels, categories, and supply logs.

### ✨ Key Features

- **Medicine & Stock Management:** CRUD operations for pharmaceuticals.
- **Categorization:** Organize items by categories, suppliers, and expiration dates.
- **RESTful API:** Clean API endpoints built with Django REST Framework.
- **Admin Dashboard:** Built-in Django Admin portal for full system control.

### 🚀 Getting Started

#### Prerequisites

- Python 3.10+
- `pip` (Python package installer)

#### Installation & Setup

1. **Create and Activate Virtual Environment:**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate

   Install Dependencies:
   ```

Bash
pip install -r requirements.txt
Apply Database Migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Create Superuser (Admin Access):

Bash
python manage.py createsuperuser
Run the Server:

Bash
python manage.py runserver
Access the application at http://127.0.0.1:8000/

النسخة العربية
📝 وصف المشروع
Pharmacy Tracker هو تطبيق باك إند (Backend RESTful API) لبناء نظام إدارة ومتابعة مخزون الصيدليات والأدوية باستخدام Python و Django و Django REST Framework (DRF). يهدف النظام لتسهيل عمليات التتبع والتسجيل اليومي للأدوية والأصناف والكميات المتاحة.

✨ مميزات النظام
إدارة الأدوية والمخزون: عمليات الإضافة والتعديل والحذف والاستعراض (CRUD Operations).

التصنيف والمتابعة: تنظيم الأدوية حسب الفئات، الموردين، وتواريخ الصلاحية.

واجهات برمجة التطبيقات (RESTful API): مسارات API منظمة واحترافية باستخدام DRF.

لوحة تحكم مشرفة: لوحة تحكم Django Admin مدمجة لإدارة النظام بالكامل.

🚀 كيفية تشغيل المشروع
المتطلبات الأساسية
تثبيت Python الإصدار 3.10 أو أحدث.

خطوات التشغيل
إنشاء وتفعيل البيئة الافتراضية (Virtual Environment):

Bash
python -m venv venv

# على نظام ويندوز:

venv\Scripts\activate

# على نظام ماك أو لينكس:

source venv/bin/activate
تثبيت المكتبات المطلوبة:

Bash
pip install -r requirements.txt
إنشاء وجداول قاعدة البيانات (Migrations):

Bash
python manage.py makemigrations
python manage.py migrate
إنشاء حساب مسؤول النظام (Superuser):

Bash
python manage.py createsuperuser
تشغيل السيرفر:

Bash
python manage.py runserver
يمكنك التصفح ودخول النظام عبر الرابط: http://127.0.0.1:8000/
