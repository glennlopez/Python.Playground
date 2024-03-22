import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# Base URL for the airport data
BASE_URL = "https://trueairport.cae.com/Home/DownloadLatestAirport?insetId={}&imageGeneratorId=3"
MAX_INSET_ID = 500

def login_and_get_cookies():
    # Open a browser window and manually log in to the website.
    # Once logged in, retrieve the cookies from the browser session.
    # Return the cookies as a dictionary.
    # You can use browser automation tools like Selenium for this step.
    
def main():
    # Get user cookies (already logged in)
    cookies = login_and_get_cookies()

    # Initialize a session with the cookies
    session = requests.Session()
    session.cookies.update(cookies)

    # Initialize progress bar
    progress_bar = tqdm(total=MAX_INSET_ID, desc="Processing", unit="insetId")

    # Iterate through insetIds
    for insetId in range(MAX_INSET_ID):
        url = BASE_URL.format(insetId)
        response = session.get(url)

        # Check if the HTML content contains the desired link
        if "https://cae-eng-cace-endpoint-p-tas.azureedge.net/assets/" in response.text:
            # Parse HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            prettified_html = soup.prettify()

            # Write prettified HTML content to dataLink.txt
            with open("dataLink.txt", "a") as file:
                file.write(f"--- InsetId {insetId} ---\n")
                file.write(prettified_html)
                file.write("\n\n")

        # Update progress bar
        progress_bar.update(1)

    # Close progress bar
    progress_bar.close()
    print("HTML content from valid insetIds has been saved to dataLink.txt.")

if __name__ == "__main__":
    main()
