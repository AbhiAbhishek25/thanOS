from app import app
@app.route('/')
@app.route('/index')
def index():
    return """
            <html>
            <head><title>bheem</title>
            </head>
            <body>jkasghv
            </body>
            </html>
            """
