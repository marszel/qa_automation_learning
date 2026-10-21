from playwright.sync_api import expect

def test_demobank_valid_login(page):
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    page.locator("#login_id").fill("12345678")
    page.locator("#login_id").press("Enter")
    page.locator("#login_password").fill("12345678")
    page.locator("#login_password").press("Enter")

    expect(page.locator("#user_name")).to_have_text("Jan Demobankowy")

def test_demobank_invalid_login_id_too_short(page):
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    page.locator("#login_id").fill("1234")
    page.locator("#login_id").press("Enter")

    expect(page.locator("#error_login_id")).to_contain_text(r"identyfikator ma min. 8 znaków")