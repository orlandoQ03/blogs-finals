# CS321 Finals - Blogging Site
**By Orlando Quintana**

This is a blogging site that would allow the author to grow his brand. End-users would also be able to interact with the content uploaded and share them with other peers across the internet.

## - Overview -
This is a simple website consisting of blog posts listed on the user's feed. Users are able to read, write and edit their posts.

## - Back-End -
This website utlizies Django to process HTTP requests, and SQlite database as its back-end solution.

#### Routes:
* `POST /blog_index`: Renders the main page.
* `DELETE /delete/<int:id>/`: Delete posts to the user's discretion.

### Database Schema
- **Blog Posts**: Stores the user's blog content, which are displayed in the main oage.
- **Blog Users**: Contains the users registered.
- **Comments**: Stores comments left by users on blog posts.

## How to open
1. Clone repository to your local machine.
   `git clone https://github.com/orlandoQ03/blogs-finals.git`
2. Locate the project directory
   _e.g._ `cd path/to/CSC321-final`
3. create virtual environment
   `python -m venv env`
4. To activate the virtual environment, use:
* On Windows:
  `env\Scripts\activate`
* On Unix or MacOS:
  `source env/bin/activate`
5. Change directory to _/blog_
  `cd blog`
6. Run server
  `python manage.py runserver`
7. Access this URL to view website
  `http://127.0.0.1:8000/`
