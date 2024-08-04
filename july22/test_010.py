# @pytest.mark.name -- annotations

import pytest
import allure


@allure.title("Smoke Test case 1")
@allure.description("This is a smoke test case where verify wether 2-2 = 0")
@pytest.mark.smoke
def test_sub0():
    assert 2 - 2 == 0


@allure.title("Smoke Test case 2")
@allure.description("This is a smoke test case where verify wether 3-3 = 0")
@pytest.mark.regression
def test_sub1():
    assert 3 - 3 == 0


@pytest.mark.smoke
@pytest.mark.skip
def test_sub2():
    assert 1 - 1 == 1


@pytest.mark.sanity
def test_sub3():
    assert 0 - 0 != 0

@pytest.mark.smoke
@pytest.mark.skip(reason="Not working,Skip it")
def test_sub3():
    assert 0 - 0 != 0
