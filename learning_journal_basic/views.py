from pyramid.response import Response
import os
import io

THIS_DIR = os.path.dirname(__file__)

def home_page(request):
    file_path = os.path.join(THIS_DIR, "data", "sample.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    config.add_view(home_page, route_name="home")
