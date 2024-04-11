# E-Shopping Website

## Introduction

The E-Shopping Website is a Django-based web application that provides users with an online shopping experience. It features an add-to-cart functionality, online shopping capabilities, and Razorpay integration for secure payment processing. Additionally, the application includes user login authentication to protect user data and manage orders.

## Features

- **User Authentication**: Secure user login and registration.
- **Product Catalog**: Browse and search products available for purchase.
- **Add to Cart**: Add and manage products in the shopping cart.
- **Online Shopping**: Checkout process with Razorpay payment integration.
- **Order Management**: Track order history and status.
- **Secure Payments**: Integration with Razorpay for safe and secure online transactions.
- **Responsive Design**: Optimized for different devices, including mobile and desktop.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:

    ```shell
    git clone 
    ```

2. **Navigate to the project directory**:

    ```shell
    cd e-shopping-website
    ```

3. **Create a virtual environment**:

    ```shell
    python -m venv venv
    ```

4. **Activate the virtual environment**:

    ```shell
    # For Windows
    venv\Scripts\activate

    # For macOS/Linux
    source venv/bin/activate
    ```

5. **Install the project dependencies**:

    ```shell
    pip install -r requirements.txt
    ```


7. **Apply database migrations**:

    ```shell
    python manage.py migrate
    ```

8. **Create a superuser**:

    ```shell
    python manage.py createsuperuser
    ```

## Usage

To start the development server, run the following command:

```shell
python manage.py runserver
