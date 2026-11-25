from playwright.sync_api import Page, Route, expect

URL = "https://demo.playwright.dev/api-mocking"


def fulfill_with_mango(route: Route):
    route.fulfill(json=[{"name": "Mango", "id": 1}])


def get_fruit(page: Page, fruit: str):
    return page.get_by_text(fruit, exact=True)


def add_extra_fruit(route: Route):
    response = route.fetch()
    fruits = response.json()
    fruits.append({"name": "Playwright", "id": 100})
    route.fulfill(response=response, json=fruits)


def test_page_shows_mocked_fruit(page: Page):
    page.route("*/**/api/v1/fruits", fulfill_with_mango)
    page.goto(URL)
    expect(get_fruit(page, "Mango")).to_be_visible()
    expect(get_fruit(page, "Banana")).not_to_be_visible()


def test_extra_fruit_is_added_to_real_list(page: Page):
    page.route("*/**/api/v1/fruits", add_extra_fruit)
    page.goto(URL)
    expect(get_fruit(page, "Playwright")).to_be_visible()
    expect(get_fruit(page, "Banana")).to_be_visible()