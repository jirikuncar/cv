"""Serve linked data profile."""

import functools
import os

from flask import Flask, Response, send_file, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

SENTRY_SDK = os.getenv("SENTRY_SDK")

if SENTRY_SDK:
    import sentry_sdk
    from sentry_sdk.integrations.flask import FlaskIntegration

    sentry_sdk.init(SENTRY_SDK, integrations=[FlaskIntegration()])


def handle_text_turtle(filename='profile.ttl', **kwargs):
    return send_file(filename, mimetype='text/turtle')


def handle_other(filename='profile.ttl', format='trig',
                 mimetype='application/trig'):
    import rdflib

    g = rdflib.Graph()
    g.parse(source=filename, format='text/turtle')
    return Response(g.serialize(format=format), mimetype=mimetype)


accept_handlers = {
    'application/trig': functools.partial(handle_other, format='trig'),
    'text/turtle': handle_text_turtle,
}


@app.route("/")
@app.route("/jiri/")
@cross_origin()
def index():
    default = 'text/turtle'
    mimetypes = request.accept_mimetypes
    best = mimetypes.best_match(accept_handlers.keys(), default)

    if best != default and mimetypes[best] == mimetypes[default]:
        best = default

    return accept_handlers[best](mimetype=best)
