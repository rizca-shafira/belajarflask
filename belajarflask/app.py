from flask import render_template, Flask, request
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        #Tangkap data dari form
        name = request.form['name']
        email = request.form['email']
        return f"Nama: {name}, Email:{email}"
    return render_template('form.html')
if __name__ == '__main__':
    app.run(debug=True)