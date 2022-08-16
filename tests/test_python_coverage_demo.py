from python_coverage_demo import __version__
from python_coverage_demo.demo import demo_one, demo_two


def test_version():
    assert __version__ == '0.1.0'

def test_demo_one():
    assert demo_one() == 1

def test_demo_two():
    assert True
