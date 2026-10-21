from playwright.sync_api import expect

def test_antoogle_search(page):
    test_phrase = "Test"
    page.goto("https://antoogle.testoneo.com/")
    page.get_by_role("textbox", name="Recipient's username").click()
    page.get_by_role("textbox", name="Recipient's username").fill(test_phrase)
    page.get_by_role("button", name="Search!").click()

    expect(page.locator("#item0")).to_have_text(test_phrase)
