from flask import Flask, url_for, render_template, request, redirect
app = Flask(__name__)

page_id = 0
bookmarks = []

@app.route("/")
def hello():
    return render_template('index.html', bookmarks=bookmarks, page_id=page_id)

@app.route("/<int:page_id>/edit_bookmark/<int:bookmark_id>/", methods=['POST'])
def edit_bookmark(page_id, bookmark_id):
    print(request.form)
    for i in request.form:
        print(i, request.form[i])
    if request.method == 'POST':
        new_bm = {}
        new_bm['name'] = request.form['name']
        new_bm['url'] = request.form['link']
        new_bm['page_id'] = page_id
        bookmarks[bookmark_id] = new_bm
    return redirect(url_for('hello'))

@app.route("/<int:page_id>/add_bookmark/", methods=['POST'])
def add_bookmark(page_id):
    print(request.form)
    for i in request.form:
        print(i, request.form[i])
    if request.method == 'POST':
        new_bm = {}
        new_bm['name'] = request.form['name']
        new_bm['url'] = request.form['link']
        new_bm['page_id'] = page_id
        bookmarks.append(new_bm)
    return redirect(url_for('hello'))

@app.route("/<int:page_id>/delete_bookmark/<int:bookmark_id>/")
def delete_bookmark(page_id, bookmark_id):
    bookmarks.pop(bookmark_id)
    return redirect(url_for('hello'))

@app.route("/move/<int:moving_bookmark_id>/<int:reference_bookmark_id>/")
def move_bookmark(moving_bookmark_id, reference_bookmark_id):
    if moving_bookmark_id < reference_bookmark_id:
        reference_bookmark_id -= 1
    bookmarks.insert(reference_bookmark_id, bookmarks.pop(moving_bookmark_id))
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
