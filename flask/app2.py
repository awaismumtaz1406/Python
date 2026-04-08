from flask import Flask, render_template, request,jsonify, render,  flash, redirect, url_for
app2 = Flask(__name__)
app2.secret_key = 'cyber_secret_key'  # needed for flash messages
profile_data = {
    "name": "Awais Mumtaz",
    "email": "awais@example.com",
    "phone": "+92-300-1234567",
    "city": "Lodhran",
    "profession": "Software Engineering Student",
    "skills": ["Python", "Flask", "Java", "SQL"],
    "bio": "Passionate about AI and web development"
}




@app2.route('/')
def home():
    return render_template('home.html',data=profile_data)

@app2.route('/contact',methods=['POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
            name = request.form.get('name')
            email = request.form.get('email')
            message = request.form.get('message')
            # Here you can add code to save the data to a database or send an email
            flash('Your message has been sent successfully!', 'success')
            return redirect(url_for('hone'))
print(f"Flask app2 is running...\nName:{name} \nEmail:{email} \n{message}")
return redirect(f"{url_for('home')}#contact")




