from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)

page_id = 0
bookmarks = []

@app.route("/")
def hello():
    return render_template('index.html', bookmarks=bookmarks, page_id=page_id)

@app.route("/<int:page_id>/add_bookmark/", methods=['POST'])
def add_bookmark(page_id):
    if request.method == 'POST':
        new_bm = {}
        new_bm['name'] = request.form['name']
        new_bm['url'] = request.form['link']
        new_bm['page_id'] = page_id
        bookmarks.append(new_bm)
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
