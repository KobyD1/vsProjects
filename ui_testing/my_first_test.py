from playwright.sync_api import Page, expect


from playwright.sync_api import expect, sync_playwright


    # 1. Start Playwright runtime
with sync_playwright() as p:
    # 2. Launch browser
    browser = p.chromium.launch(headless=False)  # set True for headless mode

        # 3. Create an isolated browser context
    context = browser.new_context(viewport={"width": 1280, "height": 720})

        # 4. Create a new page (tab) inside the context
    page = context.new_page()

        # 5. Navigate to URL and assert
    page.goto("https://parcel-pulse-and-pilots.lovable.app/", wait_until="domcontentloaded")
    delivery = page.locator("[id=nav-deliveries]")
    delivery.click()
    buttons = page.query_selector_all("[class*='px-3 py-1.5']")
    # add= page.get_by_text("Add delivery")
    add = page.get_by_role("button",name="Add delivery")
    add.click()
    print ("test end")