# Task 1

await page.get_by_role("button", name="Wyślij").click()

# Task 2

await page.get_by_placeholder("Wpisz swój e-mail").fill("test@example.com")

# Task 3

await page.get_by_role("link", name="Regulamin sklepu").click()

# Task 4

await page.get_by_placeholder("Hasło").fill("TajneHaslo123")

# Task 5

page.get_by_role("heading", name="Witamy na pokładzie")

# Task 6

await page.get_by_role("checkbox", name="Akceptuję warunki").click()

# Task 7

await page.get_by_role("button", name="Szukaj").click()

# Task 8

await page.get_by_placeholder("Szukaj produktów...").fill("Laptop")

# Task 9

await page.get_by_role("radio", name="Karta kredytowa").click()

# Task 10

await page.get_by_role("link", name="Wyloguj").click()