from flask_opentracing import FlaskTracer
from injector import Module
from jaeger_client import Config


def init_jaeger_tracer(service_name='your-app-name'):
    """This scaffold is configured whith `Jeager <https://github.com/jaegertracing/jaeger>`_ but you can use
    one of the `opentracing tracers <http://opentracing.io/documentation/pages/supported-tracers.html>`_
    :param service_name: the name of your application to register in the tracer
    :return: opentracing.Tracer
    """
    config = Config(config={
        # 'propagation': 'b3',
        'sampler': {'type': 'const', 'param': 1}, 'logging': True,
    }, service_name=service_name)
    return config.initialize_tracer()


class TracerModule(Module):
    tracer = ""

    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        self.tracer = FlaskTracer(init_jaeger_tracer(self.app.config["APP_NAME"]), True, self.app)
        binder.bind(FlaskTracer, to=self.tracer)
