import pytest

from playwright_tests.tutorial_by_Andrew_Knight.pages.result import DuckDuckGoResultPage
from playwright_tests.tutorial_by_Andrew_Knight.pages.search import DuckDuckGoSearchPage
from playwright.sync_api import Page


@pytest.fixture
def result_page(page: Page) -> DuckDuckGoResultPage:
    return DuckDuckGoResultPage(page)

@pytest.fixture
def search_page(page: Page) -> DuckDuckGoSearchPage:
    return DuckDuckGoSearchPage(page)