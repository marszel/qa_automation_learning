from playwright.async_api import expect

# Task 1

async def test_task_1(page):
    await expect(page.get_by_role("button", name="Zaloguj się")).to_be_visible()

# Task 2

async def test_task_2(page):
    await expect(page.get_by_placeholder("Wpisz swój e-mail")).to_have_value("user@example.com")

# Task 3

async def test_task_3(page):
    await expect(page.get_by_role("checkbox", name="Akceptuję warunki")).to_be_checked()

# Task 4

async def test_task_4(page):
    await expect(page.get_by_role("heading", name="Panel użytkownika")).to_have_text("Panel użytkownika")

# Task 5

async def test_task_5(page):
    await expect(page.get_by_role("button", name="Zapisz zmiany")).to_be_disabled()

# Task 6

async def test_task_6(page):
    await expect(page.get_by_placeholder("Wpisz komentarz")).to_be_enabled()

# Task 7

async def test_task_7(page):
    await expect(page.get_by_role("link", name="Pobierz fakturę PDF")).to_have_attribute("href", "download")

# Task 8

async def test_task_8(page):
    await expect(page.get_by_role("textbox", name="Opis produktu")).to_be_empty()

# Task 9

async def test_task_9(page):
    await expect(page.get_by_role("button", name="Usuń konto")).not_.to_be_visible()

# Task 10

async def test_task_10(page):
    await expect(page.get_by_placeholder("Kod rabatowy")).not_.to_be_disabled()

# Task 11

async def test_assert_success_visible(page):
    await expect(page.get_by_text("Dane zostały zapisane")).to_be_visible()

# Task 12

async def test_assert_error_visible(page):
    await expect(page.get_by_text("Błędny format adresu e-mail")).to_be_visible()

# Task 13

async def test_assert_loading_hidden(page):
    await expect(page.get_by_text("Wczytywanie danych...")).not_.to_be_visible()

# Task 14

async def test_add_todo_and_verify(page):
    await page.goto("https://demo.playwright.dev/todomvc/")
    await page.get_by_placeholder("What needs to be done?").fill("Nauczyć się Playwrighta").press("Enter")
    await expect(page.get_by_text("Nauczyć się Playwrighta")).to_be_visible()

# Task 15

async def test_todo_counter_is_hodden_on_start(page):
    await page.goto("https://demo.playwright.dev/todomvc/")
    await expect(page.get_by_text("0 items left")).not_.to_be_visible()

# Task 16

async def test_todo_counter_shows_one_item(page):
    await page.goto("https://demo.playwright.dev/todomvc/")
    await page.get_by_placeholder("What needs to be done?").fill("Zrobić zakupy").press("Enter")
    await expect(page.get_by_text("1 item left")).to_be_visible()
