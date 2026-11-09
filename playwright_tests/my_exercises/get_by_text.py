# Task 1

async def test_click_success_message(page):
    await page.get_by_text("Konto zostało utworzone pomyślnie").click()

# Task 2

async def test_click_error_alert(page):
    await page.get_by_text("Nieprawidłowe hasło, spróbuj ponownie").click()

# Task 3

async def test_click_cookie_text(page):
    await page.get_by_text("Ta strona używa plików cookies").click()

# Task 4

async def test_click_logout_warning(page):
    await page.get_by_text("Zostaniesz wylogowany za 5 minut").click()

# Task 5

async def test_click_newsletter_info(page):
    await page.get_by_text("Zapisując się, akceptujesz politykę prywatności").click()

# Task 6

async def test_click_promo_code(page):
    await page.get_by_text("Twój kod rabatowy to: WITAJ").click()

# Task 7

async def test_click_welcome_back(page):
    await page.get_by_text("Witaj ponownie w panelu").click()

# Task 8

async def test_click_payment_failed(page):
    await page.get_by_text("Płatność odrzucona. Spróbuj inną kartą").click()

# Task 9

async def test_click_terms_update(page):
    await page.get_by_text("Zaktualizowaliśmy nasz regulamin").click()

# Task 10

async def test_click_no_results(page):
    await page.get_by_text("Nie znaleziono produktów spełniających kryteria").click()