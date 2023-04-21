## Automated Script for Submitting a Heat/Hot Water Complaint to NYC 311 Portal

This Python script uses Selenium to automate the submission of a Heat/Hot Water complaint to the NYC 311 Portal. The script fills out the necessary forms and submits the complaint. The script also utilizes multi-threading to speed up the submission process.

### Prerequisites

- Python 3.x
- Selenium WebDriver
- `selenium_recaptcha_solver` package
- ChromeDriver executable (included in the repo)

### Usage

1. Clone the repo.
3. Install the dependencies `pip install -r requirements.txt` 
4. Run the script `python complain.py`.

Note: The script assumes that you are running on a Windows machine. If you are using a different operating system, you may need to adjust the path to the ChromeDriver executable.

