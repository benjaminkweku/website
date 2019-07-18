from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('hp.html')

#step2
@app.route('/whereami')
def whereami():
    return 'Ghana'

#step3
@app.route('/foo')
def foo(name):
    return render_template('foo.html')



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')