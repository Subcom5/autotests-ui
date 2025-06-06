import pytest


def test_user_login():
    assert 1 == 1


class TestUserAuthentication:
    def test_login(self):
        assert 1 == 1

    def test_pop(self):
        assert 1 == 1


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5
