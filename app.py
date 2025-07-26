# Import the new functions we need
from flask import Flask, abort, redirect, render_template, request, url_for

# Import both functions from our data file
from data import add_post, get_posts

app = Flask(__name__)


@app.route('/')
def home():
    my_message = "Flask is amazing!"
    return render_template('home.html', message=my_message)


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@app.route('/blog')
def blog():
    all_posts = get_posts()
    return render_template('blog.html', posts=all_posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    all_posts = get_posts()
    single_post = next(
        (post for post in all_posts if post['id'] == post_id), None)
    if single_post is None:
        abort(404)
    return render_template('post.html', post=single_post)

# This is the new route for creating posts


@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        # Get data from the form
        title = request.form['title']
        content = request.form['content']

        # Create a dictionary for the new post data
        new_post_data = {'title': title, 'content': content}

        # Add the new post to our data
        add_post(new_post_data)

        # Redirect the user to the main blog page to see their new post
        return redirect(url_for('blog'))

    # If it's a GET request, just show the form
    return render_template('create.html')


if __name__ == '__main__':
    app.run(debug=True)
