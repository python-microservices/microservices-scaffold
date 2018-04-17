import opentracing
import requests
from flask_opentracing import FlaskTracer

from pyms.healthcheck import healthcheck_blueprint


@healthcheck_blueprint.route('/healthcheck', methods=['GET'])
def healthcheck(tracer: FlaskTracer):
    span = tracer.get_span()
    headers = {}
    tracer._tracer.inject(span, opentracing.Format.HTTP_HEADERS, headers)
    result = requests.post(url="http://localhost:8081/oauth/login", data={
        "username": "test",
        "password": "1234"
    }, headers=headers)
    return result.content
