#  My Blogsite Application

### MyBlog is a blogging website where a user can create and share their blogs. Users can interact with the system. Additionally, the website has a feature that displays random quotes to inspire users.
#### By **Joy Machuka**

+ [Description](#Description)
+ [How to run the code](#Setup)
+ [Live Site](#Live-Site)
+ [Technologies](#Technologies-and-Languages-Used)
+ [Authors Info](#Author)
+ [Licence](#Licence)

# Description
A personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, add a feature that displays random quotes to inspire your users.

## Live-Site
[View Site](https://machukablogsite.herokuapp.com/)


## BDD
* Users should like to view the blog posts on the site.
* Users should be able to comment on blog posts
* Users should see random quotes on the site
* Writers should be able to sign in to the blog.
* Writers should be able to create blogs.
* Writers should be able to delete comments they find unpleasant.

## Setup

1. Clone the repository:
HTTPS: `git clone https://github.com/MachukaJoy/my-blog.git`<br>
SSH: `git clone git@github.com:MachukaJoy/my-blog.git`<br>
2. Move to the folder and install requirements
  ```bash
  cd my-blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python manage.py server
  ```
5. Testing the application
  ```bash
  python manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Known Bugs
There are not any known bugs as at now. But feel free to let us know should you find any.

## Technologies-and-Languages-Used
* Python
* Visualstudio
* Flask
* postgress sql

## Support and contact details
Should you have any issues or questions, ideas or concerns feel free to reach out to me. Also feel free to make contribution to the code and can contact me at machukajoy@gmail.com
## Author

- [Joy Machuka](https://github.com/MachukaJoy)
### Licence
[MIT LICENSE](https://github.com/MachukaJoy/my-blog/blob/main/LICENSE)<br>


** <br>
Copyright (c) {2022} [Joy Machuka ](https://github.com/MachukaJoy)