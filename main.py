from flask import Flask, render_template_string
import os
import datetime
import subprocess

app = Flask(__name__)


@app.route('/htop')
def htop():
    # Get the system username
    username = os.getlogin()

    # Get server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime(
        '%Y-%m-%d %H:%M:%S')

    # Get tasklist command output (for Windows)
    try:
        tasklist_output = subprocess.check_output(['tasklist'], universal_newlines=True)
    except Exception as e:
        tasklist_output = str(e)

    # Define the HTML template
    html_content = f"""
    <!doctype html>
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Augutine Ullas</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre>{tasklist_output}</pre>
    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Public visibility
