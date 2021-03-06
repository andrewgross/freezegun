import datetime
from freezegun import freeze_time


def test_simple_api():
    freezer = freeze_time("2012-01-14")
    freezer.start()
    assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)
    assert datetime.datetime.utcnow() == datetime.datetime(2012, 01, 14)
    assert datetime.date.today() == datetime.date(2012, 01, 14)
    freezer.stop()
    assert datetime.datetime.now() != datetime.datetime(2012, 01, 14)
    freezer = freeze_time("2012-01-10")
    freezer.start()
    assert datetime.datetime.now() == datetime.datetime(2012, 01, 10)
    freezer.stop()


@freeze_time("2012-01-14")
def test_decorator():
    assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)


@freeze_time("2012-01-14")
class Tester(object):
    def test_the_class(self):
        assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)


# Mock.patch can be used as decorator or context manager
def test_context_manager():
    with freeze_time("2012-01-14"):
        assert datetime.datetime.now() == datetime.datetime(2012, 01, 14)
    assert datetime.datetime.now() != datetime.datetime(2012, 01, 14)

# @current_time(*args)
# def test_foo_bar():
#     pass
# @static_time - clock always returns same thing
# @start_time - clock runs while test runs
