from playwright.sync_api import Page, expect


def test_search_results(page: Page):
    page.goto("https://playwright.dev/python")
    page.get_by_role("button", name="Search").click()
    page.get_by_placeholder("Search docs").fill("locator")
    expect(page.get_by_role("link", name="locator").first).to_contain_text("Locators")