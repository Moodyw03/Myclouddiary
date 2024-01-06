
<h1 align="center">MemoMingle</h1>

[View the live project here.](https://memomingle.vercel.app/)

Welcome to MemoMingle, an intuitive and robust note-taking application designed to streamline the way individuals capture and organize their thoughts. This application serves as a personal and professional aid, allowing users to create, edit, and manage notes with ease. The sleek user interface, tailored for an optimal user experience, incorporates contemporary design principles to ensure that navigation and note management are both seamless and efficient.

Whether you're jotting down quick reminders or compiling detailed research notes, MemoMingle is your go-to solution for storing information efficiently. This document will guide you through every aspect of using MemoMingle, from initial setup to advanced features.

This submission represents Milestone Project 3 for the Code Institute's Diploma in Web Application Development program. My website comprises of a note-taking app and utilizes the HTML, CSS,  Javascript, and Python technologies I have acquired throughout the course.




<div align="center">
<a href="https://ibb.co/T1yzLCd"><img src="https://i.ibb.co/hc0pfqw/memomingle-copy.jpg" alt="memomingle-copy" border="0"></a>
</div>

## Repository

[Find the project repository here:](https://github.com/Moodyw03/MemoMingle)



## User Interface
MemoMingle's user interface (UI) is crafted with a focus on simplicity and ease of use, ensuring that users can navigate the app intuitively. The UI employs a warm, pastel colour palette that creates a welcoming and calming environment, aimed at enhancing user concentration and reducing visual strain during note management tasks.

Key design elements include:

**Minimalistic Layout:** The clean interface avoids clutter, directing user focus to the task at hand.

**Intuitive Controls:** Commonly used actions are prominently placed and easily accessible, promoting a fluid user experience.

**Consistent Visual Elements:** The use of familiar icons and consistent colour coding helps users quickly associate functions with symbols.

**Responsive Design:** The UI adjusts seamlessly across various devices, ensuring functionality and aesthetics are maintained on screens of all sizes.
The choice of colours and layout is informed by psychological principles that associate certain hues with memory and cognitive function, which is essential for a note-taking application. This thoughtful design approach aims to make the note-taking process as effortless and pleasant as possible for the user.


  <div align="center"><a href="https://ibb.co/FY9j5t5"><img src="https://i.ibb.co/vdbK383/memomingle-colors-copy.jpg" alt="memomingle-colors-copy" border="0"></a></div>


## Colour Scheme 

The colour scheme displayed is carefully selected to offer a balance between aesthetic appeal and functional design. The muted tones like 'Moon Mist' and 'Cape Cod' suggest a professional and minimalist interface, while the 'Median Cut' scheme introduces warmer colours like 'Granite Green' and 'Crocodile' to add subtle energy without overwhelming the user. For text, colours like 'Shark' and 'Heavy Metal' offer excellent readability against lighter backgrounds, ensuring that the user interface remains accessible and easy on the eyes. These choices likely contribute to a user-friendly experience that prioritizes clarity and focus.

<div align="center"><a href="https://ibb.co/BVZPvB2"><img src="https://i.ibb.co/4ZTfCpR/color-scheme-memomingle-copy.jpg" alt="color-scheme-memomingle-copy" border="0"></a></div>

## Typography 

MemoMingle employs a thoughtful combination of fonts in its design, prominently featuring 'Inter' as the primary typeface. Inter is a highly legible sans-serif font that was crafted with digital screens in mind, ensuring that text is readable at various sizes and weights. Its clean lines and open shapes contribute to the modern and uncluttered feel of the user interface. As a fallback, the application uses 'Arial', a ubiquitous sans-serif font known for its wide availability and straightforward appearance. The generic 'sans-serif' as the final fallback ensures that, in any environment where the primary fonts are not available, the browser can use a default sans-serif font, maintaining the integrity of the app's design. This font stack not only guarantees a seamless and accessible reading experience but also aligns with MemoMingle's sleek and user-centric design principles.


## Wireframes
Home Page Wireframe - [View](https://pdfhost.io/v/2JUYSOaP4_moodloop_wireframe)





## Code Overview

### App Structure

config/: Contains configuration files, like db.py for database connections.
controllers/: Holds the auth_controller.py and note_controller.py for handling authentication and note operations respectively.
models/: Includes user.py and note.py defining the data models.
static/: Stores static files like CSS, JS, and images for the front end.
templates/: Contains HTML templates for rendering views.
app.py: The main entry point of the Flask application.
.env: Stores environment variables (not to be uploaded to version control).

Database Schema:
Users Collection: Stores username and hashed passwords.
Notes Collection: Stores notes with fields for title, content, tags, creation, and last modified timestamps.

API Endpoints:
Authentication (/auth/sign-in, /auth/sign-up, /auth/sign-out): For user login, registration, and logout.
Note Management (/notes/, /notes/new, /notes/<id>/delete, /notes/<id>/edit): For listing, creating, deleting, and editing notes.


<div align="center"><a href="https://ibb.co/vvSkVMb"><img src="https://i.ibb.co/yBrqdxD/flowchart.jpg" alt="flowchart" border="0"></a></div>

## Functionality
<div align="center"><a href="https://ibb.co/DMP8830"><img src="https://i.ibb.co/X5f33mc/crud1.jpg" alt="crud1" border="0"></a></div>

### Authentication

**Sign-Up:** Users register by providing a username and password. The password is hashed for security and stored in the Users collection.

**Sign-In:** Users log in using their credentials. The system validates the input against the stored hashed password. Upon success, a session is initiated.

**Sign-Out:** Users sign out to end their session, clearing their session data and preventing further access to their notes without re-authentication.

### Notes Management

**Creating Notes:** Users can create notes by entering a title and content, along with optional tags.

**Updating Notes:** Existing notes can be updated. Users can modify the title, content, and tags of their notes.

**Deleting Notes:** Users can delete any of their notes. This action is irreversible.

**Searching Notes:** Users can search through their notes using keywords. The search can match note titles, content, and tags.

### Error Handling

**User Feedback:** Clear messages are displayed to users upon errors, like invalid login attempts or issues in note operations.
**Validation Errors:** Input validation errors, such as short usernames or passwords, prompt the user to correct their input.


## Security

In MemoMingle, security is a top priority, and several measures are implemented to protect user data:

**Password Hashing:** We use Werkzeug's security features to hash passwords before storing them in the database. This means that actual passwords are never stored, only their secure hashes.

**Session Management:** Flask-Session is utilized for secure session management. User sessions are encrypted and managed server-side, mitigating the risks associated with client-side sessions.

**Environment Variables:** Sensitive information, such as database URI and secret keys, are stored in environment variables, not in the codebase, to prevent exposure.

**Secure Transport Layer:** The application is configured to enforce HTTPS to ensure that data transmitted between the client and server is encrypted.

**Input Validation:** All user inputs are validated and sanitized to protect against SQL injection and XSS attacks.

These technologies and strategies form a robust security posture for MemoMingle, ensuring user data integrity and confidentiality.

## Testing 
For more information on testing, [click here](https://github.com/Moodyw03/MemoMingle/blob/main/testing.md).



## Deployment
Set Up Your Local Environment:

Initialize a virtual environment to isolate your project's Python dependencies:
Copy code
python3 -m venv venv
Activate the virtual environment:
bash
Copy code
source venv/bin/activate
Install Dependencies:

Install Flask, along with any other necessary packages from your requirements.txt:
Copy code
pip install flask
Verify the installation of Flask and the Python version:
css
Copy code
python -m flask --version
Generate a requirements.txt file to keep track of your dependencies and their versions:
Copy code
pip freeze > requirements.txt
Prepare the Application for Production:

Make sure all debug features are turned off. In production, you should not use the Flask built-in server, debug mode, or the development environment variable. Instead, set up a production-grade WSGI server like Gunicorn:
Copy code
pip install gunicorn
Configure environment variables to use production settings. For example, set the secret key to a secure random value.
Prepare the Production Server:

Install and configure a web server like Nginx or Apache to forward requests to your WSGI server.
Set up SSL using Certbot for HTTPS.
Deploy Your Application:

Upload your code to the production server, usually through Git or by using SCP/SFTP.
Install your project's dependencies on the production server using the requirements.txt file:
Copy code
pip install -r requirements.txt
Run Gunicorn to serve your Flask application:
arduino
Copy code
gunicorn "app:create_app()"
Configure Nginx or Apache to proxy requests to Gunicorn.
DNS and Environment Variables:

Update your domain's DNS records to point to your server's IP address.
Ensure that environment variables for production are correctly set on your server.
Start the Application:

Use a process manager like systemd or Supervisor to keep your application running.
Monitor Your Deployment:

Create a virtual environment named 'venv' for dependency isolation.
`python3 -m venv env`

Activate the created virtual environment.
`source env/bin/activate`

Install Flask, a lightweight web application framework.
`pip install flask`

Generate a file with all installed packages and their versions.
`pip freeze > requirements.txt`

Check the installed Flask and Python versions.
`python -m flask --version`

Set the environment variable to specify the Flask application entry point.
`export FLASK_APP=app`

Set the Flask environment to development for debugging and auto-reload.
`export FLASK_ENV=development`

Enable debug mode for more detailed error logs and interactive debugging.
`export FLASK_DEBUG=1`

Run the Flask web application on a local development server.
`flask run`

Combined
`export FLASK_APP=app; export FLASK_ENV=development; export FLASK_DEBUG=1; flask run`

Implement monitoring and logging to keep track of your application's performance and errors.
Remember to adapt these commands and steps to fit the specific needs of your production environment and the hosting provider you choose.


## Technologies used 
The MemoMingle app employs a variety of technologies, each serving a specific role within the project:

**Python:** The primary programming language used for server-side logic.

**Flask:** A micro web framework for Python used to handle HTTP requests and serve web pages.

**Jinja2:** Templating engine for rendering HTML templates into dynamic web pages.

**Werkzeug:** Utility library for Python used for password hashing and other HTTP related utilities.

**MongoDB:** NoSQL database used to store user and notes data.

**pymongo:** MongoDB driver for Python, allowing for database interactions.

**dotenv:** Library for loading environment variables from a .env file into os.environ.

**HTML/CSS:** Markup and styling languages used for creating and styling the frontend.

**JavaScript:** Scripting language used for dynamic client-side functionalities.

**Git:** Version control system for tracking changes in source code during development.

**GitHub:** Hosting for software development and version control using Git.

**Gunicorn:** WSGI HTTP Server for UNIX, used to run Python web applications in production.

**Vercel:** Cloud platforms used for deploying, managing, and scaling the app.

**SSL/TLS:** Protocols for secure communication over the internet.

**Let's Encrypt/Certbot:** Tools used to obtain free SSL/TLS certificates for encrypting HTTP traffic.

**Flask-Session:** Flask extension for server-side session management.

**W3C Validator:** Service used to validate HTML and CSS for web standards compliance.

**JSHint:** A static code analysis tool used for detecting errors and potential problems in JavaScript code.

**Flask-Migrate**: An extension that handles SQLAlchemy database migrations for Flask applications.

**Bootstrap:** Front-end framework for designing responsive and mobile-first websites.

**chat GPT** GPT was leveraged for advanced problem resolution.

**VS Code** The application was developed and executed using Visual Studio Code as the preferred Integrated Development Environment (IDE).

**Eraser** for the creation of flowcharts and wireframes during the design process.


## Deployment




