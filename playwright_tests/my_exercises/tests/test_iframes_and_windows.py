import re
from playwright.sync_api import Page, expect, BrowserContext


def test_type_in_iframe_editor(page: Page):
    page.goto("https://the-internet.herokuapp.com/iframe")
    expect(page.get_by_role("heading", name="An iFrame containing the")).to_be_visible()
    editor_frame = page.locator("iframe[title=\"Rich Text Area\"]").content_frame
    editor_frame.get_by_label("Rich Text Area. Press ALT-0").fill("Hello iframe")
    expect(editor_frame.get_by_text("Hello iframe")).to_be_visible()


def test_link_opens_new_window(page: Page, context: BrowserContext):
    page.goto("https://the-internet.herokuapp.com/windows")
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Click Here").click()
    new_page = new_page_info.value
    expect(new_page).to_have_title(re.compile("New Window"))