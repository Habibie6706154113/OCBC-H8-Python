from flask import Flask
from markupsafe import escape
from flask import render_template
from book import author_book
from flask import request

app = Flask(__name__)

@app.route('/') #will invoke the func if we hit 127.0.0.1/
def hello_world():
    sum = a = 10
    page_content = f'<h1>Hello, World!</h1> <p>{sum}</p> <p><b> lorem ipsom fdfkjfsk</b></p> {a}'
    page_content += '<p><i>Hello Italyc</i></p>'
    return page_content

@app.route('/<name>') #will invoke the func if we hit 127.0.0.1/<name>
def hello(name):
    return f'Hello, {escape(name)}'

@app.route('/bio') 
def bio():
    return f'<h2> Author BIO </h2> <a href="/"> Home Page</a>'

@app.route('/author', methods=['GET', 'POST']) 
def author():
    if 'author_id' in request.form:
        author_book[request.form['author_id']] = []
    #html = f'List of Books authored by {author_id}:'
    #html += '<ul> <li>intro to lyfe</li> <li>intro to lyfe</li></ul>'
    return render_template('author.html', author_book = author_book)

@app.route('/books/<int:author_id>') 
def books(author_id):
    if author_id not in author_book.keys():
        return render_template('book.html', author_id = author_id)
    elif len(author_book[author_id]) == 0:
        return render_template('book.html', author_id = author_id)
    else:
        return render_template('book.html', author_id = author_id, book_list = author_book[author_id])

@app.route('/hello/')
@app.route('/hello/<name>')
def template(name=None):
    return render_template('template.html', name=name)

#apakah dijalankan sebagai standalon script
if __name__ == '__main__':
    app.run(debug=True)

    
