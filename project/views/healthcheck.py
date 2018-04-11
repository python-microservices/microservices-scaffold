from project.views import views_hc


@views_hc.route('/healthcheck', methods=['GET'])
def healthcheck():
    return "OK"
