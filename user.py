from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/shortenurl',methods=['GET','POST'])
def shortenurl():
    return render_template('shortenurl.html',shortcode=request.args['shortcode'])    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)    