from hello import hello


def test_default():
    assert hello() == "Hello, world!"


def test_name():
    assert hello("DSC 198") == "Hello, DSC 198!"
