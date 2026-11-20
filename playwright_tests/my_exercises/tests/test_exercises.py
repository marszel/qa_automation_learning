import re
from playwright.sync_api import Page, expect

URL = "https://playwright.dev/python"


def search_for(page: Page, phrase: str):
    page.get_by_role("button", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill(phrase)


def test_page_title(page: Page):
    page.goto(URL)
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started(page: Page):
    page.goto(URL)
    start = page.get_by_role("link", name="Get started")
    start.click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()


def test_no_results(page: Page):
    page.goto(URL)
    search_for(page, "zzzzqqqq")
    expect(page.get_by_text("No results found for")).to_be_visible()


def test_diagnosis(page: Page):
    page.goto(URL)
    search_for(page, "expect")
    links = page.get_by_role("link", name="expect")
    expect(links.first).to_be_visible()
    print(links.count())
    print(links.first.inner_text())