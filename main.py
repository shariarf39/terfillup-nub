import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://182.160.97.196:8088/studentportal/authorise/login")
    #page.get_by_role("link", name="NUB Student Portal - Login").click()
    page.get_by_placeholder("Student ID").click()
    #studemtn id
    page.get_by_placeholder("Student ID").fill("41220300364")
    page.get_by_placeholder("Password").click()
    #password
    page.get_by_placeholder("Password").fill("99809062")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("link", name="TER Fill Up").click()
    # course code
    page.get_by_label("Select Course And Section *").select_option("31625012")
    page.locator("select[name=\"answerValueId\\[0\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[1\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[2\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[3\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[4\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[5\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[6\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[7\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[8\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[9\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[10\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[11\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[12\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[13\\]\"]").select_option("1269664")
    page.locator("select[name=\"answerValueId\\[14\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[15\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[16\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[17\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[18\\]\"]").select_option("1269663")
    page.get_by_role("row", name="20 Professional Behavior").get_by_role("cell").nth(3).click()
    page.locator("select[name=\"answerValueId\\[19\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[20\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[21\\]\"]").select_option("1269663")
    page.locator("select[name=\"answerValueId\\[22\\]\"]").select_option("1269663")
    page.get_by_label("What did you like about this").click()
    page.get_by_label("What did you like about this").fill("behaviour is good . teaching style also good")
    page.get_by_label("What did you dislike about").click()
    page.get_by_label("What did you dislike about").fill("i don't dislike")
    page.get_by_role("button", name="Submit").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)