## Google Suggestion Fetcher

This Python script retrieves Google search suggestions for a given keyword. It uses the Google Suggest API to fetch popular related search terms.

### How it Works

1.  **Imports:**
    * `requests`: Used to make HTTP requests to the Google Suggest API.
    * `json`: Used to parse the JSON response from the API.

2.  **`get_google_suggestions(keyword)` Function:**
    * Constructs the API URL: `https://suggestqueries.google.com/complete/search?client=firefox&q={keyword}`. This URL is used to query Google's suggestion service.
    * Sets the `User-Agent` header to mimic a Firefox browser. This is often necessary to avoid being blocked by Google.
    * Sends a GET request to the API using the `requests.get()` method.
    * Checks the response status code:
        * If the status code is 200 (OK), it parses the JSON response using `json.loads()`.
        * The suggestions are extracted from the second element of the parsed JSON array (index 1).
        * Returns the list of suggestions.
        * If the status code is not 200, it prints an error message and returns an empty list.

3.  **`if __name__ == "__main__":` Block:**
    * Prompts the user to enter a keyword using `input()`.
    * Calls the `get_google_suggestions()` function with the entered keyword.
    * Prints the retrieved suggestions in a user-friendly format.

### Usage

1.  **Installation:**
    * Ensure you have Python installed.
    * Install the `requests` library: `pip install requests`

2.  **Running the Script:**
    * Save the code as a `.py` file (e.g., `google_suggestions.py`).
    * Run the script from your terminal: `python google_suggestions.py`
    * Enter a keyword when prompted.
    * The script will display the popular related keywords.

### Example Output

Masukkan kata kunci: python programming
Keyword populer terkait:

python programming tutorial
python programming for beginners
python programming language
python programming examples
python programming jobs
python programming online
python programming books

