from playwright.sync_api import sync_playwright
import json
import csv

def scrape_js_quotes():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto("https://quotes.toscrape.com/js")

        all_quotes = []
        page_num = 1
        while True: 

            page.wait_for_selector(".quote", timeout=10000)
            quotes = page.locator(".quote").all()

            for quote in quotes:
                text = quote.locator(".text").inner_text()
                author = quote.locator(".author").inner_text()
                tags = [tag.inner_text() for tag in quote.locator(".tags a").all()]
                formatted_tags = ", ".join(tags) if tags else "No tags"

                all_quotes.append({"text": text, "author": author, "tags": formatted_tags})
                print(f"Quote: {text}\nAuthor: {author}\nTags: {formatted_tags}\n")

            next_button = page.locator("li.next a")
            if not next_button.is_visible():
                print("No more pages to scrape. Exiting the loop.")
                break
            print('\nClicking the "Next" button to load more quotes...\n')
            next_button.click()
            page.wait_for_load_state("networkidle")

            print(f"Scraped page {page_num}. Total quotes collected so far: {len(all_quotes)}")
            page_num += 1


        print(f"Total quotes collected: {len(all_quotes)}")
        browser.close()


        with open("quotes.json", "w", encoding="utf-8") as json_file:
            json.dump(all_quotes, json_file, ensure_ascii=False, indent=4)  

        if all_quotes:
            with open("quotes.csv", "w", newline="", encoding="utf-8") as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["text", "author", "tags"])
                writer.writeheader()
                writer.writerows(all_quotes)

        print("Quotes have been saved to quotes.json and quotes.csv.")  

if __name__ == "__main__":
    scrape_js_quotes()  

