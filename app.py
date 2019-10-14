"""Serve linked data profile."""

import os

from flask import Flask, send_file
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

SENTRY_SDK = os.getenv("SENTRY_SDK")

if SENTRY_SDK:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(SENTRY_SDK, integrations=[FlaskIntegration()])


@app.route("/")
@app.route("/jiri/")
@cross_origin()
def index():
    return send_file('profile.ttl', mimetype='text/turle')
