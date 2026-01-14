import undetected_chromedriver as uc
import os

def get_driver():
    options = uc.ChromeOptions()

    # Use existing Chrome profile credentials so no need to login
    options.add_argument(
        "--user-data-dir=/Users/saransh/Library/Application\ Support/Google/Chrome"
    )

    # Using Default profile
    options.add_argument("--profile-directory=Default")

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")

    return uc.Chrome(options=options)






# https://github.com/saranshgupta0107
# https://www.linkedin.com/in/saranshgupta0107/