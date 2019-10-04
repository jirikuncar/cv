"""Serve linked data profile."""

import os

from flask import Flask, Response, send_file

app = Flask(__name__)

SENTRY_SDK = os.getenv("SENTRY_SDK")

if SENTRY_SDK:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(SENTRY_SDK, integrations=[FlaskIntegration()])


@app.route("/")
@app.route("/jiri/")
def index():
    return send_file('profile.ttl', mimetype='text/turle')
