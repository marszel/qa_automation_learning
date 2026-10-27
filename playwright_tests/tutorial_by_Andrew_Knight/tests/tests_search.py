import pytest

from playwright_tests.tutorial_by_Andrew_Knight.pages.search import DuckDuckGoSearchPage
from playwright_tests.tutorial_by_Andrew_Knight.pages.result import DuckDuckGoResultPage
from playwright.sync_api import expect, Page

ANIMALS = [
    "panda",
    "python",
    "polar bear",
    "parrot",
    "dog",
    "cat",
    "panther",
    "platypus",
    "peacock"
]

@pytest.mark.parametrize("phrase", ANIMALS)
def test_basic_duckduckgo_search(
        phrase: str,
        page: Page,
        search_page: DuckDuckGoSearchPage,
        result_page: DuckDuckGoResultPage) -> None:

    #Given the DuckDuckGo home page is displayed
    search_page.load()

    #When the user searches for a phrase
    search_page.search(phrase)

    #Then the search result contains the phrase
    expect(page).to_have_title(f"{phrase} at DuckDuckGo")

    #And the search result query is the phrase
    expect(result_page.result_input).to_have_value(phrase)

    #And the search result links pertain to the phrase
    assert result_page.result_link_titles_contain_phrase(phrase)

