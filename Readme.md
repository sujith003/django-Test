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

## URL Paths:
The following URL paths are available for use in the Product Management System:

- **Home Page**: `/home/`  
  Displays the homepage with basic information like name and role.
  
- **About Page**: `/about/`  
  Displays information about the project.

- **Contact Page**: `/contact/`  
  Displays the contact page.

- **Services Page**: `/services/`  
  Describes the services offered by the application.

- **Add Product**: `/products/add/`  
  Allows the user to add a new product to the inventory.

- **All Products**: `/allproducts/`  
  Displays a list of all products in the inventory.

- **Delete Product**: `/products/delete/<int:id>/`  
  Deletes the specified product by its ID.

- **Update Product**: `/products/update/<int:id>/`  
  Allows the user to update an existing product by its ID.

### Example Usage:
- To add a product: Navigate to `/products/add/`
- To view all products: Navigate to `/allproducts/`
- To update a product: Navigate to `/products/update/<product_id>/`
- To delete a product: Navigate to `/products/delete/<product_id>/`


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



