# MarketFastApi

## Overview
MarketFastApi is a project designed to facilitate the creation of market-related functionalities using FastAPI. This project includes core features such as user authentication, product management, and transaction processing.

## Features
- **User Authentication**: Secure user registration and login.
- **Product Management**: Add, update, and delete products.
- **Transaction Processing**: Handle purchase transactions efficiently.
- **Database Migrations**: Managed using Alembic.
- **Testing**: Comprehensive tests to ensure functionality.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/AlLixAI/MarketFastApi.git

2. Navigate to the project directory:
   ```sh
   cd MarketFastApi
   
3. Install dependencies:
   ```sh
   pip install -r requirements.txt

## Usage
1. Run the application:
   ```sh
   uvicorn src.main:app --reload
2. Access the API documentation at 'http://127.0.0.1:8000/docs'.

## Project Structure

```plaintext
MarketFastApi/
│
├── src/
│   ├── main.py          # Main application entry point
│   ├── config.py        # config .env
│   ├── database.py      # Connection to database and creat async session
│   ├── auth/            # authorization route
│   └── operations/      # Business logic (market product + tasks (redis+selery))
│ 
│
├── tests/
│   ├── conftest.py         # Pytest async options
│   ├── test_auth.py        # Tests for auth
│   └── test_operations.py  # Tests for another functional
│
├── migrations/          # Database migration files
│
├── requirements.txt     # Project dependencies
│
└── README.md            # Project documentation
