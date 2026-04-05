# from flask import Flask
# app1=Flask(__name__)


# @app1.route('/')
# def home():
#     return """<h1>
# welcome to home    </>
#  <p>
#   malik aq weht uhqw awaejkhgw</p>
#    <a href="/">Home</a>
# """


# @app1.route('/awais')
# def awais():
#     return 'malik awais ghallu' \
#     ' i ama student of computer science' \
#     ' i am learning flask framework and i am loving it'

# @app1.route('/ahmad')
# def ahmad():
#     return 'malik ahmad ghallu' \
#     ' i ama student of computer science' \
#     ' i am learning flask framework and i am loving it'





# if __name__=="__main__":
#      app1.run(debug=True, port =8000)
    

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """<h1>Welcome to home</h1>
    <p>malik aq weht uhqw awaejkhgw</p>
    <a href="/awais">Awais</a><br>
    <a href="/ahmad">Ahmad</a>
    """

@app.route('/awais')
def awais():
    return 'malik awais ghallu - student of computer science learning flask'

@app.route('/ahmad')
def ahmad():
    return 'malik ahmad ghallu - student of computer science learning flask'

if __name__ == "__main__":
    app.run(debug=True, port=1000)














