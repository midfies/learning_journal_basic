"""Views page for learning_journal_basics."""
from pyramid.response import Response
import os
import io

THIS_DIR = os.path.dirname(__file__)


def list_home(request):
    """View for home pafe/list view."""
    file_path = os.path.join(THIS_DIR, "templates", "index.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def detail_view(request):
    """View for individual post."""
    file_path = os.path.join(THIS_DIR, "data", "lj11.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def create_view(request):
    """View for creating a new post."""
    file_path = os.path.join(THIS_DIR, "templates", "newpost.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def update_view(request):
    """View for updating a existing post."""
    file_path = os.path.join(THIS_DIR, "templates", "editpost.html")
    file_data = io.open(file_path).read()
    return Response(file_data)


def includeme(config):
    """All the views to include."""
    config.add_view(list_home, route_name="list")
    config.add_view(detail_view, route_name="detail")
    config.add_view(create_view, route_name="create")
    config.add_view(update_view, route_name="update")
