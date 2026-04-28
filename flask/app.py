from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
import os

def create_app():
    app = Flask(__name__)

    # 🔐 Secure config (never hardcode secrets in real apps)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')

    # Sample data
    profile_data = {
        "name": "Awais Mumtaz",
        "email": "awais@example.com",
        "phone": "+92-300-1234567",
        "city": "Lodhran",
        "profession": "Software Engineering Student",
        "skills": ["Python", "Flask", "Java", "SQL"],
        "bio": "Passionate about AI and web development",
        "experience": "Passionate developer with 2 years of experience building web apps using Flask and Django."
    }

    # ----------------python app.py ROUTES ---------------- #

    @app.route('/')
    def home():
        return render_template('home.html', data=profile_data)

    @app.route('/contact', methods=['POST'])
    def contact():
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # ✅ Basic validation
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect(url_for('home') + '#contact')

        # Simulate processing (DB/email)
        print(f"\nContact Form:\nName: {name}\nEmail: {email}\nMessage: {message}")

        flash('Your message has been sent successfully!', 'success')
        return redirect(url_for('home'))

    # ---------------- API ROUTES ---------------- #

    @app.route('/api/profile')
    def api_profile():
        return jsonify(profile_data)

    @app.route('/api/profile/<field>')
    def api_profile_field(field):
        value = profile_data.get(field)
        if value is None:
            return jsonify({"error": "Field not found"}), 404
        return jsonify({field: value})

    # ---------------- ERROR HANDLER ---------------- #

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("404.html"), 404

    return app


# Run app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)