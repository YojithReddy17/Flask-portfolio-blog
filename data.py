import datetime

_posts = [
    {
        'id': 1,
        'title': 'My First Post',
        'content': 'This is the full content of my very first blog post. It is exciting to use Flask!',
        'author': 'Yojit',
        'date': '2025-07-25'
    },
    {
        'id': 2,
        'title': 'Learning Web Development',
        'content': 'Web development has many parts: Python for the backend, HTML for structure, and CSS for styling. It all comes together with a framework like Flask.',
        'author': 'Yojit',
        'date': '2025-07-26'
    }
]


def get_posts():
    """Returns the list of all posts."""
    return _posts


def add_post(new_post_data):
    """Adds a new post to the list."""
    new_id = len(_posts) + 1
    today = datetime.date.today().strftime("%Y-%m-%d")

    new_post = {
        'id': new_id,
        'title': new_post_data['title'],
        'content': new_post_data['content'],
        'author': 'Yojit',
        'date': today
    }
    _posts.append(new_post)
