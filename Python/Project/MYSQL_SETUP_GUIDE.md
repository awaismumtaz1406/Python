# 🏋️ Awais Fitness App - MySQL Setup Guide

## 📋 Prerequisites

1. **Install MySQL Server**
   - Download from: https://dev.mysql.com/downloads/mysql/
   - During installation, set a root password (remember this!)

2. **Install MySQL Connector for Python**
   ```bash
   pip install mysql-connector-python
   ```

## 🔧 Configuration Steps

### Step 1: Update Database Configuration

Open `fitness_app_mysql.py` and modify the DB_CONFIG section:

```python
DB_CONFIG = {
    'host': 'localhost',      # Keep as localhost
    'user': 'root',           # Your MySQL username (usually 'root')
    'password': 'your_password_here',  # ⚠️ CHANGE THIS to your MySQL password
    'database': 'fitness_app_db'
}
```

### Step 2: Run the Application

```bash
python fitness_app_mysql.py
```

The app will automatically:
- Create the database `fitness_app_db`
- Create all required tables
- Start the login screen

## 📊 Database Structure

### Tables Created:

1. **users** - Stores user accounts
   ```sql
   - id (Primary Key)
   - username (Unique)
   - password (Hashed)
   - email
   - created_at (Timestamp)
   ```

2. **user_data** - Stores fitness data
   ```sql
   - id (Primary Key)
   - user_id (Foreign Key → users.id)
   - weight
   - height
   - age
   - calories
   - updated_at (Timestamp)
   ```

3. **workout_logs** - For future workout tracking
   ```sql
   - id (Primary Key)
   - user_id (Foreign Key → users.id)
   - workout_date
   - workout_type
   - notes
   - created_at (Timestamp)
   ```

## 🔍 Testing Your Connection

### Method 1: Using MySQL Command Line
```sql
-- Login to MySQL
mysql -u root -p

-- View all databases
SHOW DATABASES;

-- Use the fitness database
USE fitness_app_db;

-- View all tables
SHOW TABLES;

-- View users data
SELECT * FROM users;

-- View user fitness data
SELECT * FROM user_data;
```

### Method 2: Using MySQL Workbench
1. Download MySQL Workbench
2. Connect using your credentials
3. Browse the `fitness_app_db` database

## 🚀 Features

- ✅ User Registration & Login
- ✅ Password Hashing (SHA-256)
- ✅ Save Weight, Height, Age, Calories to MySQL
- ✅ Retrieve user data from database
- ✅ Multiple user support with isolated data
- ✅ Auto-create database and tables

## 🛠️ Troubleshooting

### Error: "Access denied for user 'root'@'localhost'"
**Solution:** Update the password in DB_CONFIG

### Error: "Can't connect to MySQL server"
**Solution:** Make sure MySQL service is running
- Windows: Check Services → MySQL
- Mac: `brew services start mysql`
- Linux: `sudo systemctl start mysql`

### Error: "No module named 'mysql'"
**Solution:** Install the connector
```bash
pip install mysql-connector-python
```

## 📝 Usage Flow

1. **First Time User:**
   - Click "Sign Up"
   - Enter username, email, password
   - Account saved to MySQL `users` table

2. **Existing User:**
   - Click "Login"
   - Enter credentials
   - Data retrieved from database

3. **Save Fitness Data:**
   - Enter weight, height, age
   - Click "Calculate & Save"
   - Data saved to MySQL `user_data` table

4. **Load Saved Data:**
   - Click "Load My Data"
   - Retrieves from MySQL database

## 🔐 Security Notes

- Passwords are hashed using SHA-256
- Never share your MySQL root password
- For production, use environment variables for DB credentials

## 📚 Learning Resources

This project covers:
- Python + MySQL integration
- CRUD operations (Create, Read, Update, Delete)
- Database connections and queries
- Foreign key relationships
- Parameterized queries (SQL injection prevention)
- User authentication systems

Good luck with your MySQL practice! 💪🔥
