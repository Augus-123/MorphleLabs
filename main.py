from flask import Flask, render_template_string
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.environ.get('USER', 'Unknown User')

    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30))).strftime(
        '%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], universal_newlines=True)
    except Exception as e:
        top_output = str(e)

    html_content = f"""
    <!doctype html>
    <html>
    <head><title>System Info</title></head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> Augustine Ullas</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run(port=5000)  
