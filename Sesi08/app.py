from flask import render_template
import connexion

app = connexion.App(__name__, specification_dir='./')

app.add_api('swagger.yml')

@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)