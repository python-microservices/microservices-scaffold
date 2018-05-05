from pyms.healthcheck import healthcheck_blueprint


@healthcheck_blueprint.route('/healthcheck', methods=['GET'])
def healthcheck():
    return "OK"
