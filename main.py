## Intergrate HTML With Flask
## HHTP verb GET And POST 

## jinja2 template engine

''' 
{%...%}  condition,for loop
{{ }} expression to print
{#...#} this is for comment
'''
from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return 'Hello All'

# Success link
@app.route('/success/<int:score>')
def success(score): 
    res=""
    if score>=50:
        res="Pass"
    else:
        res="fail"
    exp={'score':score,'res':res}          
    return render_template('result.html',result=exp)

# Failed link
@app.route('/failed/<int:score>')
def fail(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

# Result link
@app.route('/result/<int:marks>')
def result(marks):
    if marks < 40:
        return "<h1>redirect(url_for('fail', score=marks))</h1>"  # Redirect to 'fail' route
    else:
        return "<h2>redirect(url_for('success', score=marks))</h2>"  # Redirect to 'success' route
    
## Result Checker for html page

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        math=float(request.form['math'])
        english=float(request.form['english'])
        total_score=(science+math+english)/4
    res=""
    if total_score>50:
        res="success"
    else:
        res="fail"
    return redirect(url_for('success',score=total_score))
        
    
    
    
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
