from playwright.sync_api import Playwright, expect

def test_google_search(playwright: Playwright) -> None:
    context = playwright.chromium.launch_persistent_context(
        user_data_dir="./user_data",
        headless=False,
        slow_mo=500,
        args=["--disable-blink-features=AutomationControlled"]
    )
    page = context.pages[0]
    page.goto("https://google.com")
    #page.get_by_role("button", name="Zaakceptuj wszystko").click()
    page.get_by_role("combobox", name="Szukaj").click()
    page.get_by_role("combobox", name="Szukaj").fill("instagram jaktestować.pl")
    page.keyboard.press("Escape")
    page.get_by_role("button", name="Szukaj w Google").first.click()

    expect(page.locator('h3:has-text("jaktestowac.pl • Instagram")'),"Test Failed").to_contain_text("jaktestowac.pl")