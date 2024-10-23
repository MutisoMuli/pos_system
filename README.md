# POS System (Point of Sale)

A comprehensive Point of Sale system built with Django, featuring inventory management, sales processing, and reporting capabilities.

## 🚀 Features

### Core Functionality
- **Product Management**
  - Product catalog with categories
  - SKU and barcode support
  - Inventory tracking
  - Price management
  - Product variants (size, color)
  - Low stock alerts

- **User Management**
  - Multiple user roles (Admin, Cashier, Manager)
  - Secure login system
  - Role-based access control
  - User activity logging

- **Sales Processing**
  - Fast checkout process
  - Barcode scanner support
  - Multiple payment methods (Mpesa, Visa)
  - Receipt generation
  - Order modification/cancellation

- **Inventory Management**
  - Real-time stock tracking
  - Stock adjustments
  - Purchase orders
  - Supplier management
  - Stock alerts and notifications

### Additional Features
- Customer profiles and loyalty program
- Sales and inventory reporting
- Revenue analysis
- Employee performance tracking

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment
- Git

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [repository-url]
   cd pos_system
   ```

2. **Create and activate virtual environment**
   ```bash
   # Create virtual environment
   python3 -m venv pos_env

   # Activate virtual environment
   # On Windows:
   pos_env\Scripts\activate
   # On Unix or MacOS:
   source pos_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create .env file in project root
   touch .env

   # Add following variables to .env:
   SECRET_KEY=your_secret_key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```

5. **Run migrations**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python3 manage.py createsuperuser
   ```

7. **Start development server**
   ```bash
   python3 manage.py runserver
   ```

## 🏗️ Project Structure
```
pos_system/
├── inventory/              # Inventory management app
├── media/                  # User uploaded files
│   └── products/          # Product images
├── pos_system/            # Main project directory
├── products/              # Products app
├── static/                # Static files
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # Project-wide templates
│   ├── base.html
│   └── includes/
└── users/                 # User management app
```

## 🔑 Usage

1. **Access admin panel**
   - Go to `http://localhost:8000/admin`
   - Login with superuser credentials

2. **Product Management**
   - Add/Edit products at `http://localhost:8000/products/`
   - Manage categories
   - Monitor stock levels

3. **Sales Processing**
   - Process sales at `http://localhost:8000/sales/`
   - Generate receipts
   - Handle returns

## 🔒 Security

- Implements Django's built-in security features
- Role-based access control
- Password hashing
- CSRF protection
- XSS protection

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add: some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - *Initial work* - [MutisoMuli](https://github.com/MutisoMuli)
- Your Name - *Initial work* - [anto-muli](https://github.com/anto-muli)