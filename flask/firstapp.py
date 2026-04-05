from flask import Flask
firstapp = Flask(__name__)
@firstapp.route('/')
def intro():
    return 'malik awais ghallu'



if __name__== "__main__":
    firstapp.run(debug=True)