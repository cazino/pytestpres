import pytest


@pytest.fixture(scope="module")
def fixture_one(request):
    print "\nFixture 1"

    def fin():
        print ("Finalizing Fixture 1")

    request.addfinalizer(fin)
    return 1


@pytest.fixture
def fixture_two(fixture_one, request):
    print "\nFixture 2"

    def fin():
        print ("Finalizing Fixture 2")

    request.addfinalizer(fin)
    return 1


def test_one(fixture_two):
    print "Test one"
    assert True


def test_two(fixture_two):
    print "Test two"
    assert False
