# Product Management System

## Description:
This is a Django-based Product Management System. It allows users to add, update, delete, and view products. The system supports the management of product details like name, code, price, GST, and whether the product is a food item.

## Features:
- **Home Page**: Displays basic information like name and role.
- **About Page**: Contains information about the project.
- **Contact Page**: Includes a contact form or details.
- **Services Page**: Describes the services offered by the application.
- **Product Management**: Users can view, add, update, and delete products from the inventory.
  - **Add Product**: Add new products.
  - **Update Product**: Modify existing product details.
  - **Delete Product**: Remove a product from the inventory.
  - **View All Products**: Display all products in a table with pagination.

## Technologies Used:
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: SQLite (or PostgreSQL, MySQL)
- **Version Control**: Git

## Setup Instructions:
To get this project up and running locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/sujith003/django-Test.git
cd django-Test
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



