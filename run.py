import os
from spotimend import create_app

app = create_app()

production = os.environ.get('PRODUCTION', False)

if __name__ == '__main__':
    if production:
        app.jinja_env.cache = {}
        app.run(debug=False, port=None)
    else:
        app.jinja_env.cache = {}
        app.run(host='127.0.0.1', port=5000, debug=True)
