import re
from playwright.sync_api import Page, expect, Browser

URL = "https://demo.playwright.dev/todomvc"


def add_task(page: Page, task: str):
    textbox = page.get_by_role("textbox", name="What needs to be done?")
    textbox.fill(task)
    textbox.press("Enter")


def get_task_checkbox(page: Page, chore: str):
    return page.get_by_role("listitem").filter(has_text=chore).get_by_role("checkbox", name="Toggle Todo")


def get_task(page: Page):
    return page.get_by_test_id("todo-title")


def test_add_task(page: Page):
    page.goto(URL)
    add_task(page, "Buy milk")
    job = get_task(page)
    expect(job).to_have_text("Buy milk")


def test_complete_task(page: Page):
    page.goto(URL)
    add_task(page, "Buy milk")
    add_task(page, "Call mom")
    buy_milk_checkbox = get_task_checkbox(page, "Buy milk")
    buy_milk_checkbox.check()
    call_mom_checkbox = get_task_checkbox(page, "Call mom")
    expect(buy_milk_checkbox).to_be_checked()
    expect(call_mom_checkbox).not_to_be_checked()


def test_task_count_after_adding_three_tasks(page: Page):
    page.goto(URL)
    add_task(page, "Buy bread")
    add_task(page, "Water plants")
    add_task(page, "Wash the dishes")
    expect(get_task(page)).to_have_count(3)


def test_delete_task(page: Page):
    page.goto(URL)
    add_task(page, "Go for a walk")
    add_task(page, "Buy dog's food")
    row = page.get_by_role("listitem").filter(has_text="Go for a walk")
    row.hover()
    row.get_by_role("button", name="Delete").click()
    expect(get_task(page)).to_have_count(1)
    expect(get_task(page)).to_have_text("Buy dog's food")


def test_filter_active_tasks(page: Page):
    page.goto(URL)
    add_task(page, "Learn Playwright")
    add_task(page, "Make dinner")
    learn_playwright_checkbox = get_task_checkbox(page, "Learn Playwright")
    learn_playwright_checkbox.check()
    page.get_by_role("link", name="Active").click()
    expect(page).to_have_url(re.compile(r"active"))
    expect(get_task(page)).to_have_count(1)
    expect(get_task(page)).to_have_text("Make dinner")


def test_edit_task(page: Page):
    page.goto(URL)
    add_task(page, "Make dinner")
    get_task(page).dblclick()
    edit_box = page.get_by_role("textbox", name="Edit")
    edit_box.fill("Make lunch")
    edit_box.press("Enter")
    expect(get_task(page)).to_have_text("Make lunch")


def test_items_left_counter(page: Page):
    page.goto(URL)
    add_task(page, "Eat breakfast")
    add_task(page, "Wash teeth")
    add_task(page, "Take a shower")
    wash_teeth_checkbox = get_task_checkbox(page, "Wash teeth")
    wash_teeth_checkbox.check()
    expect(page.get_by_text("2 items left")).to_be_visible()


def test_contexts_are_isolated(browser: Browser):
    context_a = browser.new_context()
    context_b = browser.new_context()
    page_a = context_a.new_page()
    page_b = context_b.new_page()
    page_a.goto(URL)
    page_b.goto(URL)
    add_task(page_a, "Buy milk")
    expect(get_task(page_a)).to_have_text("Buy milk")
    expect(get_task(page_b)).to_have_count(0)
    context_a.close()
    context_b.close()