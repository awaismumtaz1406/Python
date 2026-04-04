import tkinter as tk
from tkinter import messagebox, scrolledtext
import mysql.connector
from mysql.connector import Error
import hashlib
from datetime import datetime

# ---------- Database Configuration ----------
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',          # Change to your MySQL username
    'password': 'Awais1406.',          # Change to your MySQL password
    'database': 'fitness_app_db'
}

# ---------- Database Connection ----------
def create_connection():
    """Create a database connection to MySQL server"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
        return None

def init_database():
    """Initialize database and create tables if they don't exist"""
    try:
        # First connect without database to create it
        temp_config = DB_CONFIG.copy()
        database_name = temp_config.pop('database')
        
        connection = mysql.connector.connect(**temp_config)
        cursor = connection.cursor()
        
        # Create database if not exists
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        cursor.execute(f"USE {database_name}")
        
        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                email VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create user_data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                weight DECIMAL(5,2),
                height DECIMAL(5,2),
                age INT,
                calories DECIMAL(7,2),
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')
        
        # Create workout_logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workout_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                workout_date DATE,
                workout_type VARCHAR(100),
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )
        ''')
        
        connection.commit()
        print("Database and tables created successfully!")
        
    except Error as e:
        messagebox.showerror("Database Error", f"Error initializing database: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- User Authentication ----------
class AuthWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Awais Fitness - Login")
        self.window.geometry("400x500")
        self.window.config(bg="#1e1e1e")
        self.current_user_id = None
        
        # Title
        title = tk.Label(self.window, text="🏋️ Awais Fitness", 
                        font=("Arial", 28, "bold"),
                        fg="#00ff88", bg="#1e1e1e")
        title.pack(pady=20)
        
        subtitle = tk.Label(self.window, text="Your Personal Fitness Coach", 
                           font=("Arial", 12),
                           fg="white", bg="#1e1e1e")
        subtitle.pack(pady=5)
        
        # Login/Signup Toggle
        self.is_login = True
        self.toggle_frame = tk.Frame(self.window, bg="#1e1e1e")
        self.toggle_frame.pack(pady=20)
        
        self.mode_label = tk.Label(self.toggle_frame, text="Login", 
                                   font=("Arial", 18, "bold"),
                                   fg="white", bg="#1e1e1e")
        self.mode_label.pack()
        
        # Form Frame
        form_frame = tk.Frame(self.window, bg="#2e2e2e", padx=30, pady=30)
        form_frame.pack(pady=10, padx=40, fill="both", expand=True)
        
        # Username
        tk.Label(form_frame, text="Username:", fg="white", bg="#2e2e2e",
                font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
        self.username_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
        self.username_entry.grid(row=1, column=0, pady=5)
        
        # Email (for signup)
        self.email_label = tk.Label(form_frame, text="Email:", fg="white", 
                                    bg="#2e2e2e", font=("Arial", 11))
        self.email_entry = tk.Entry(form_frame, width=25, font=("Arial", 11))
        
        # Password
        tk.Label(form_frame, text="Password:", fg="white", bg="#2e2e2e",
                font=("Arial", 11)).grid(row=4, column=0, sticky="w", pady=5)
        self.password_entry = tk.Entry(form_frame, width=25, show="*", 
                                       font=("Arial", 11))
        self.password_entry.grid(row=5, column=0, pady=5)
        
        # Buttons
        self.action_btn = tk.Button(form_frame, text="Login", 
                                    command=self.handle_auth,
                                    bg="#00ff88", fg="black",
                                    font=("Arial", 12, "bold"),
                                    width=20, height=2)
        self.action_btn.grid(row=6, column=0, pady=15)
        
        self.toggle_btn = tk.Button(form_frame, text="Don't have an account? Sign Up",
                                    command=self.toggle_mode,
                                    bg="#1e1e1e", fg="white",
                                    font=("Arial", 10),
                                    relief="flat")
        self.toggle_btn.grid(row=7, column=0, pady=5)
        
        self.window.mainloop()
    
    def toggle_mode(self):
        self.is_login = not self.is_login
        if self.is_login:
            self.mode_label.config(text="Login")
            self.action_btn.config(text="Login")
            self.toggle_btn.config(text="Don't have an account? Sign Up")
            # Hide email field
            self.email_label.grid_forget()
            self.email_entry.grid_forget()
        else:
            self.mode_label.config(text="Sign Up")
            self.action_btn.config(text="Sign Up")
            self.toggle_btn.config(text="Already have an account? Login")
            # Show email field
            self.email_label.grid(row=2, column=0, sticky="w", pady=5)
            self.email_entry.grid(row=3, column=0, pady=5)
    
    def handle_auth(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        if self.is_login:
            self.login(username, password)
        else:
            email = self.email_entry.get().strip()
            self.signup(username, password, email)
    
    def signup(self, username, password, email):
        connection = create_connection()
        if connection is None:
            return
        
        try:
            cursor = connection.cursor()
            hashed_pw = hash_password(password)
            
            query = "INSERT INTO users (username, password, email) VALUES (%s, %s, %s)"
            cursor.execute(query, (username, hashed_pw, email))
            connection.commit()
            
            messagebox.showinfo("Success", "Account created successfully! Please login.")
            self.toggle_mode()
            
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error", "Username already exists!")
        except Error as e:
            messagebox.showerror("Error", f"Signup failed: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def login(self, username, password):
        connection = create_connection()
        if connection is None:
            return
        
        try:
            cursor = connection.cursor()
            hashed_pw = hash_password(password)
            
            query = "SELECT id FROM users WHERE username = %s AND password = %s"
            cursor.execute(query, (username, hashed_pw))
            result = cursor.fetchone()
            
            if result:
                self.current_user_id = result[0]
                messagebox.showinfo("Success", f"Welcome back, {username}!")
                self.window.destroy()
                FitnessApp(self.current_user_id, username)
            else:
                messagebox.showerror("Error", "Invalid username or password!")
                
        except Error as e:
            messagebox.showerror("Error", f"Login failed: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

# ---------- Main Fitness App ----------
class FitnessApp:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        
        self.root = tk.Tk()
        self.root.title("Awais Fitness Coaching")
        self.root.geometry("900x650")
        self.root.config(bg="#1e1e1e")
        
        # User info at top
        user_frame = tk.Frame(self.root, bg="#2e2e2e")
        user_frame.pack(fill="x", pady=5)
        
        tk.Label(user_frame, text=f"👤 Logged in as: {username}", 
                fg="#00ff88", bg="#2e2e2e",
                font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        
        tk.Button(user_frame, text="Logout", command=self.logout,
                 bg="#ff4444", fg="white", font=("Arial", 10)).pack(side="right", padx=10)
        
        # Title
        title = tk.Label(self.root, text="🏋️ Awais Fitness Coaching",
                        font=("Arial", 24, "bold"),
                        fg="white", bg="#1e1e1e")
        title.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(self.root, bg="#1e1e1e")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Fitness Terms", width=20, 
                 command=self.show_terms, bg="#4a90e2", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Diet: Weight Gain", width=20, 
                 command=self.diet_weight_gain, bg="#4a90e2", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Diet: Weight Loss", width=20, 
                 command=self.diet_weight_loss, bg="#4a90e2", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Workout Plan", width=20, 
                 command=self.workout_plan, bg="#4a90e2", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=3, padx=5)
        
        # Calorie Calculator Frame
        calc_frame = tk.Frame(self.root, bg="#2e2e2e", padx=10, pady=10)
        calc_frame.pack(pady=10, fill="x", padx=20)
        
        tk.Label(calc_frame, text="Weight (kg)", fg="white", 
                bg="#2e2e2e", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.weight_entry = tk.Entry(calc_frame, width=10)
        self.weight_entry.grid(row=0, column=1, padx=5)
        
        tk.Label(calc_frame, text="Height (cm)", fg="white", 
                bg="#2e2e2e", font=("Arial", 10)).grid(row=0, column=2, padx=5)
        self.height_entry = tk.Entry(calc_frame, width=10)
        self.height_entry.grid(row=0, column=3, padx=5)
        
        tk.Label(calc_frame, text="Age", fg="white", 
                bg="#2e2e2e", font=("Arial", 10)).grid(row=0, column=4, padx=5)
        self.age_entry = tk.Entry(calc_frame, width=10)
        self.age_entry.grid(row=0, column=5, padx=5)
        
        tk.Button(calc_frame, text="Calculate & Save", 
                 command=self.calorie_calculator,
                 bg="#00ff88", fg="black",
                 font=("Arial", 10, "bold")).grid(row=0, column=6, padx=10)
        
        tk.Button(calc_frame, text="Load My Data", 
                 command=self.load_user_data,
                 bg="#ff9500", fg="white",
                 font=("Arial", 10, "bold")).grid(row=0, column=7, padx=5)
        
        # Output Area
        self.output = scrolledtext.ScrolledText(self.root, width=100, height=18,
                                               font=("Arial", 10), bg="#f5f5f5")
        self.output.pack(pady=10, padx=20)
        
        # Load user data on start
        self.load_user_data()
        
        self.root.mainloop()
    
    def logout(self):
        self.root.destroy()
        AuthWindow()
    
    def show_terms(self):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END,
        "═══════════════════════════════════════════════════════════\n"
        "                    FITNESS TERMINOLOGY\n"
        "═══════════════════════════════════════════════════════════\n\n"
        "🔹 BULKING:\n"
        "   Bulking is eating in a calorie surplus to gain muscle mass.\n"
        "   You consume more calories than you burn to support muscle growth.\n\n"
        "🔹 CUTTING:\n"
        "   Cutting is eating in a calorie deficit to lose body fat.\n"
        "   You consume fewer calories than you burn to reduce fat.\n\n"
        "🔹 GAIN MUSCLE:\n"
        "   Progressive training + surplus calories + adequate recovery\n"
        "   = Muscle growth and strength gains.\n\n"
        "═══════════════════════════════════════════════════════════\n"
        )
    
    def diet_weight_gain(self):
        self.output.delete(1.0, tk.END)
        foods = [
            "Eggs", "Banana", "Avocado", "Dates", "Rice",
            "Oats", "Chicken Breast", "Peanut Butter",
            "Nuts", "Dark Chocolate", "Seeds", "Cheese"
        ]
        self.output.insert(tk.END, 
        "═══════════════════════════════════════════════════════════\n"
        "                  WEIGHT GAIN DIET PLAN\n"
        "═══════════════════════════════════════════════════════════\n\n"
        "🍽️ High-Calorie Foods for Bulking:\n\n")
        for food in foods:
            self.output.insert(tk.END, f"   ✓ {food}\n")
        self.output.insert(tk.END, 
        "\n💡 Tip: Eat 4-6 meals per day with protein in every meal!\n"
        "═══════════════════════════════════════════════════════════\n")
    
    def diet_weight_loss(self):
        self.output.delete(1.0, tk.END)
        foods = [
            "Apple", "Chia Seeds", "Brown Rice", "Broccoli",
            "Oats", "Green Vegetables", "Greek Yogurt",
            "Beans", "Avocado", "Cucumber", "Carrot", "Orange"
        ]
        self.output.insert(tk.END,
        "═══════════════════════════════════════════════════════════\n"
        "                  WEIGHT LOSS DIET PLAN\n"
        "═══════════════════════════════════════════════════════════\n\n"
        "🥗 Low-Calorie, High-Nutrient Foods:\n\n")
        for food in foods:
            self.output.insert(tk.END, f"   ✓ {food}\n")
        self.output.insert(tk.END,
        "\n💡 Tip: Stay hydrated and eat fiber-rich foods!\n"
        "═══════════════════════════════════════════════════════════\n")
    
    def calorie_calculator(self):
        connection = create_connection()
        if connection is None:
            return
        
        try:
            w = float(self.weight_entry.get())
            h = float(self.height_entry.get())
            a = int(self.age_entry.get())
            calories = 10 * w + 6.25 * h - 5 * a - 161
            
            cursor = connection.cursor()
            
            # Check if user data exists
            check_query = "SELECT id FROM user_data WHERE user_id = %s"
            cursor.execute(check_query, (self.user_id,))
            existing = cursor.fetchone()
            
            if existing:
                update_query = '''UPDATE user_data 
                                 SET weight = %s, height = %s, age = %s, 
                                     calories = %s, updated_at = NOW()
                                 WHERE user_id = %s'''
                cursor.execute(update_query, (w, h, a, calories, self.user_id))
            else:
                insert_query = '''INSERT INTO user_data (user_id, weight, height, age, calories)
                                 VALUES (%s, %s, %s, %s, %s)'''
                cursor.execute(insert_query, (self.user_id, w, h, a, calories))
            
            connection.commit()
            
            messagebox.showinfo("Success",
                              f"💪 Daily Calories Needed: {round(calories, 2)} kcal\n\n"
                              f"✅ Data saved to MySQL database successfully!")
            
            # Reload data to show updated info
            self.load_user_data()
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to save data: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def load_user_data(self):
        connection = create_connection()
        if connection is None:
            return
        
        try:
            cursor = connection.cursor()
            
            query = '''SELECT weight, height, age, calories, updated_at 
                      FROM user_data WHERE user_id = %s'''
            cursor.execute(query, (self.user_id,))
            result = cursor.fetchone()
            
            if result:
                weight, height, age, calories, updated = result
                
                # Populate entry fields
                self.weight_entry.delete(0, tk.END)
                self.weight_entry.insert(0, str(weight))
                
                self.height_entry.delete(0, tk.END)
                self.height_entry.insert(0, str(height))
                
                self.age_entry.delete(0, tk.END)
                self.age_entry.insert(0, str(age))
                
                # Display in output area
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, 
                    "═══════════════════════════════════════════════════════════\n"
                    "                   YOUR PROFILE DATA\n"
                    "═══════════════════════════════════════════════════════════\n\n"
                    f"📊 Weight:          {weight} kg\n"
                    f"📏 Height:          {height} cm\n"
                    f"🎂 Age:             {age} years\n"
                    f"🔥 Daily Calories:  {round(calories, 2)} kcal\n"
                    f"🕐 Last Updated:    {updated}\n\n"
                    f"✅ Data loaded from MySQL database successfully!\n"
                    "═══════════════════════════════════════════════════════════\n"
                )
            else:
                self.output.delete(1.0, tk.END)
                self.output.insert(tk.END, 
                    "═══════════════════════════════════════════════════════════\n"
                    "                   WELCOME TO AWAIS FITNESS!\n"
                    "═══════════════════════════════════════════════════════════\n\n"
                    "📝 No saved data found for your account.\n\n"
                    "To get started:\n"
                    "1. Enter your Weight (kg)\n"
                    "2. Enter your Height (cm)\n"
                    "3. Enter your Age\n"
                    "4. Click 'Calculate & Save'\n\n"
                    "Your data will be securely stored in MySQL database! 💪\n"
                    "═══════════════════════════════════════════════════════════\n"
                )
                
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to load data: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    
    def workout_plan(self):
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END,
        "═══════════════════════════════════════════════════════════\n"
        "                  6 DAY WORKOUT PLAN\n"
        "═══════════════════════════════════════════════════════════\n\n"
        "💪 DAY 1: CHEST\n"
        "   • Bench Press (4 sets x 8-10 reps)\n"
        "   • Incline Dumbbell Press (4 sets x 10-12 reps)\n"
        "   • Cable Fly (3 sets x 12-15 reps)\n\n"
        "🏋️ DAY 2: BACK\n"
        "   • Pull-ups (4 sets x max reps)\n"
        "   • Barbell Rows (4 sets x 8-10 reps)\n"
        "   • Lat Pulldown (3 sets x 10-12 reps)\n\n"
        "🦾 DAY 3: SHOULDERS\n"
        "   • Overhead Press (4 sets x 8-10 reps)\n"
        "   • Lateral Raises (4 sets x 12-15 reps)\n"
        "   • Face Pulls (3 sets x 15-20 reps)\n\n"
        "💪 DAY 4: ARMS\n"
        "   • Biceps Curls (4 sets x 10-12 reps)\n"
        "   • Triceps Pushdown (4 sets x 10-12 reps)\n"
        "   • Hammer Curls (3 sets x 12-15 reps)\n\n"
        "🦵 DAY 5: LEGS\n"
        "   • Squats (4 sets x 8-10 reps)\n"
        "   • Lunges (3 sets x 12 reps each leg)\n"
        "   • Leg Press (4 sets x 10-12 reps)\n\n"
        "🔥 DAY 6: ABS & CORE\n"
        "   • Crunches (4 sets x 20 reps)\n"
        "   • Planks (4 sets x 60 seconds)\n"
        "   • Russian Twists (3 sets x 20 reps)\n\n"
        "🌟 DAY 7: REST & RECOVERY\n\n"
        "═══════════════════════════════════════════════════════════\n"
        )

# ---------- Main Execution ----------
if __name__ == "__main__":
    init_database()
    AuthWindow()
