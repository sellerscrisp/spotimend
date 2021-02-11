#!/bin/sh
source venv/bin/activate
export CLIENT_ID=a3999509c0044ce189b66e4fa042a998
export CLIENT_SECRET=c49bbc50128240c08bdf30e3d865c289
export SECRET_KEY=secretkey
export FLASK_APP=run
export FLASK_ENV=development
flask run
