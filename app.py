import os
from dotenv import load_dotenv
from flask import Flask, render_template

from markupsafe import escape, Markup
from jinja2 import pass_eval_context

from controllers.auth_controller import auth
from controllers.note_controller import note

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Security headers middleware
@app.after_request
def add_security_headers(response):
    # Content Security Policy
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' unpkg.com; style-src 'self' fonts.googleapis.com; font-src 'self' fonts.googleapis.com fonts.gstatic.com; img-src 'self' i.ibb.co unpkg.com data:; connect-src 'self'"
    # Prevent MIME type sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    # XSS Protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    # Strict Transport Security
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    # Referrer Policy
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    return response


@pass_eval_context
def nl2br(eval_ctx, value):
    result = escape(value).replace("\n", Markup("<br>\n"))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result


app.jinja_env.filters["nl2br"] = nl2br


app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(note, url_prefix="/notes")


@app.route("/")
def index():
    return render_template("index.html")
