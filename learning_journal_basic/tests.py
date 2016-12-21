import pytest
from pyramid import testing


@pytest.fixture
def req():
    """Dummy request."""
    the_request = testing.DummyRequest()
    return the_request


@pytest.fixture
def testapp():
    """Test app fixture."""
    from webtest import TestApp
    from learning_journal_basic import main
    app = main({})
    return TestApp(app)


def test_home_page_renders_file_date(req):
    """My home page view returns some data."""
    from .views import list_home
    response = list_home(req)
    assert "Most Recent Posts" in response

def test_home_page_has_thing(testapp):
    response = testapp.get("/", status=200)
    html = response.html    