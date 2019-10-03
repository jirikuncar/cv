"""Serve linked data profile."""

import os

from flask import Flask, Response, url_for

app = Flask(__name__)

SENTRY_SDK = os.getenv("SENTRY_SDK")

if SENTRY_SDK:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(SENTRY_SDK, integrations=[FlaskIntegration()])


@app.route("/")
def index():
    base_url = url_for('.index', _external=True, _anchor='')
    return Response(f'@prefix : <{base_url}>.', mimetype='text/turle')
