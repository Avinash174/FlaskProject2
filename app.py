from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my project !'

@app.route('/hello')
def hello():
    return 'Hello All'

# Building Url Dynamically

# success link

@app.route('/success/<int:score>')
def success(score):
    return 'The person is passed the marks is :'+str(score)

#failed link

@app.route('/failed/<int:score>')
def fail(score):
    return 'The person is failed the marks is :'+str(score)

#result link 

@app.route('/result/<int:score>')
def result(score):
    result=''
    if score<40:
        result="Failed with marks "+ str(score)
    else:
         result="Pass with marks "+ str(score)
    return result
        
   

# variable rule & URL Building



if __name__=='__main__':
    app.run(debug=True)