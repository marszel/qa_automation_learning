from playwright.sync_api import expect, Playwright

URL = "https://jsonplaceholder.typicode.com"


def test_get_post_returns_id_1(playwright: Playwright):
    api = playwright.request.new_context(base_url=URL)
    response = api.get("/posts/1")
    expect(response).to_be_ok()
    assert response.json()["id"] == 1
    api.dispose()