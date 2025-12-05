INSTAGRAM OSINT TOOL - README
=============================

Tool Name: InstOSiNT
Description: An Instagram Open Source Intelligence (OSINT) tool for gathering profile information
Author: Yash
Language: Python

OVERVIEW
--------
This tool automates the process of gathering public Instagram profile information using Selenium WebDriver. It allows users to login to their Instagram account and extract data from target profiles.

PREREQUISITES
-------------
1. Python 3.7 or higher
2. Chrome browser installed
3. ChromeDriver compatible with your Chrome version
4. Required Python packages

INSTALLATION
------------
1. Install required packages:
   pip install selenium termcolor

2. Download ChromeDriver:
   - Visit https://chromedriver.chromium.org/
   - Download the version matching your Chrome browser
   - Add ChromeDriver to your system PATH or place it in the script directory

FEATURES
--------
- Profile name extraction
- Posts count retrieval
- Followers count extraction
- Following count extraction
- Bio information gathering
- Profile URL capture
- Screenshot functionality
- Interactive menu system
- Colored console output

USAGE INSTRUCTIONS
------------------
1. Run the script:
   python InstOSiNT.py

2. Follow the prompts:
   - Enter your Instagram username
   - Enter your Instagram password
   - Enter the target/victim's username

3. Menu Options:
   [1] - Show Profile Name
   [2] - Show Number of Posts
   [3] - Show Number of Followers
   [4] - Show Number of Following
   [5] - Show Bio Information
   [6] - Show Profile URL
   [7] - Take Screenshot of profile
   [8] - Show All Information
   [E] - Exit

HOW TO USE THE TOOL EFFECTIVELY
--------------------------------

1. BASIC PROFILE INFORMATION GATHERING:
   - Run the tool and provide your credentials
   - Enter the target username
   - Use options 1-6 to extract specific information
   - Use option 8 for a complete profile overview

2. SCREENSHOT CAPTURE:
   - Select option 7 to capture a screenshot
   - Screenshot is saved as [username]_InstaPage.png
   - Useful for evidence preservation

3. MULTIPLE ACCOUNT ANALYSIS:
   - After completing one analysis, choose 'y' to search another account
   - The tool will restart the browser session

4. DATA COLLECTION:
   - All extracted data is displayed in real-time
   - Information includes counts, bio, and profile details
   - Data can be manually recorded from the console

TROUBLESHOOTING
----------------

Common Issues:
1. Login Failures:
   - Verify your Instagram credentials
   - Check internet connection
   - Ensure 2FA is disabled or handle appropriately

2. ChromeDriver Errors:
   - Ensure ChromeDriver version matches Chrome browser
   - Add ChromeDriver to system PATH
   - Run with administrative privileges if needed

3. Element Not Found Errors:
   - Instagram may have updated their HTML structure
   - Update the XPATH selectors in the code
   - Wait for page to fully load

4. Rate Limiting:
   - Instagram may temporarily block automated requests
   - Add delays between requests
   - Use the tool responsibly

ETHICAL USAGE GUIDELINES
------------------------
⚠️ IMPORTANT LEGAL DISCLAIMER:

1. ONLY use this tool on accounts you own or have explicit permission to analyze
2. Do not use for harassment, stalking, or illegal activities
3. Respect Instagram's Terms of Service
4. This tool is for educational and authorized security research purposes only
5. The author is not responsible for misuse of this tool

SECURITY NOTES
--------------
- Your Instagram credentials are used only for authentication
- Credentials are not stored or transmitted elsewhere
- Consider using a dedicated account for OSINT activities
- Be aware that automated access may violate Instagram's ToS

LIMITATIONS
-----------
- Requires valid Instagram login credentials
- Dependent on Instagram's current HTML structure
- May break if Instagram updates their website
- Limited to public profile information only
- Does not bypass privacy settings

SUPPORT
-------
For issues and updates, check the code structure and adapt selectors as needed.

VERSION: 1.0
LAST UPDATED: [06/11/2025]

For Educational Purposes:

Use on your own accounts to understand the tool's capabilities

Study the code to learn about web automation and OSINT techniques

For Security Professionals:

Use during authorized penetration tests

Document findings for security assessments

Obtain proper authorization before use

For Developers:

The code demonstrates Selenium automation techniques

Shows handling of dynamic web content

Example of menu-driven console applications

Customization Options:

Modify XPATH selectors if Instagram updates their layout

Add additional data points as needed

Customize output format for reports