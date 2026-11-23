from playwright.sync_api import Page, expect

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


def test_task_count(page: Page):
    page.goto(URL)
    add_task(page, "Buy bread")
    add_task(page, "Water plants")
    add_task(page, "Wash the dishes")
    expect(get_task(page)).to_have_count(3)