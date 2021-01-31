import os
from spotimend import create_app

app = create_app()

production = os.environ.get('PRODUCTION', False)

if __name__ == '__main__':
    if production:
        app.run(debug=True)
    else:
        app.run(host='127.0.0.1', port=5000, debug=True)
