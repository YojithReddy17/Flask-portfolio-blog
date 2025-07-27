Dynamic Portfolio & Blog Website
This is a fully functional, dynamic personal portfolio and blog website built with Python and the Flask web framework. It was created as a resume project to demonstrate core web development concepts without relying on complex front-end JavaScript.

The site allows a user to showcase their personal information and projects, and includes a blog where they can read and create new posts in real-time.

Features
Dynamic Content: All pages are rendered dynamically using Flask and Jinja2 templates.

Multi-Page Structure: A clean, multi-page layout with a consistent navigation bar using template inheritance (base.html).

Styled Frontend: A clean and modern user interface styled with a single CSS stylesheet.

Functional Blog:

Read: View a list of all blog posts.

View Single Post: Click on any post title to see its full content on a dedicated page.

Create: A simple form allows users to add new posts to the blog.

In-Memory Data: Uses a simple Python list of dictionaries as an in-memory "database" to manage blog posts, demonstrating data handling without database setup overhead.

Technologies Used
Backend: Python 3, Flask

Frontend: HTML5, CSS3, Jinja2 (for templating)

Development Environment: Visual Studio Code

Package Management: pip and venv for managing dependencies.

Setup and Installation
To run this project on your local machine, please follow these steps:

Clone the repository (or download the source code):

git clone (https://github.com/YojithReddy17/Flask-portfolio-blog.git)
cd Flask-portfolio-blog

Create and activate a Python virtual environment:

# Create the environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

Install the required dependencies:

pip install Flask

How to Run the Application
With the virtual environment activated and dependencies installed, run the application using the following command:

python app.py

The server will start in debug mode. You can view the application by navigating to the following URL in your web browser:

http://127.0.0.1:5000
