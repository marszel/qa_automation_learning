from playwright.async_api import expect

# Task 1

await expect(page.get_by_role("button", name="Zaloguj się")).to_be_visible()

# Task 2

await expect(page.get_by_placeholder("Wpisz swój e-mail")).to_have_value("user@example.com")

# Task 3

await expect(page.get_by_role("checkbox", name="Akceptuję warunki")).to_be_checked()

# Task 4

await expect(page.get_by_role("heading", name="Panel użytkownika")).to_have_text("Panel użytkownika")

# Task 5

await expect(page.get_by_role("button", name="Zapisz zmiany")).to_be_disabled()

# Task 6

await expect(page.get_by_placeholder("Wpisz komentarz")).to_be_enabled()

# Task 7

await expect(page.get_by_role("link", name="Pobierz fakturę PDF")).to_have_attribute("href", "download")

# Task 8

await expect(page.get_by_role("textbox", name="Opis produktu")).to_be_empty()

# Task 9

await expect(page.get_by_role("button", name="Usuń konto")).not_.to_be_visible()

# Task 10

await expect(page.get_by_placeholder("Kod rabatowy")).not_.to_be_disabled()