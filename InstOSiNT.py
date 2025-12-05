from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from termcolor import colored
import time
import os

YELLOW = "\033[93m"

banner = f"""

{YELLOW}

   _        _________ _        _______ _________            _______  _______ _________ _       _________        _   
  / )       \__   __/( (    /|(  ____ \\__   __/           (  ___  )(  ____ \\__   __/( (    /|\__   __/       ( \  
 / /    _      ) (   |  \  ( || (    \/   ) (              | (   ) || (    \/   ) (   |  \  ( |   ) (      _    \ \ 
( (    (_)     | |   |   \ | || (_____    | |      _____   | |   | || (_____    | |   |   \ | |   | |     (_)    ) )
| |            | |   | (\ \) |(_____  )   | |     (_____)  | |   | |(_____  )   | |   | (\ \) |   | |            | |
( (     _      | |   | | \   |      ) |   | |              | |   | |      ) |   | |   | | \   |   | |      _     ) )
 \ \   (_)  ___) (___| )  \  |/\____) |   | |              | (___) |/\____) |___) (___| )  \  |   | |     (_)   / / 
  \_)       \_______/|/    )_)\_______)   )_(              (_______)\_______)\_______/|/    )_)   )_(          (_/  
                                                                                                                                                          
                             
                                  .An Instagram OSINT Tool By Yash.
                                                                                                                                                                                                                                                                          
"""

print(banner)

def setup_driver():
    """Setup Chrome driver with appropriate options"""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # Remove headless for debugging, you can add it back later
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    return driver

def login_to_instagram(driver, username, password):
    """Login to Instagram account"""
    try:
        print(colored("==> Navigating to Instagram...", 'cyan'))
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        
        # Wait for and fill username
        print(colored("==> Entering credentials...", 'cyan'))
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.clear()
        username_field.send_keys(username)
        
        # Fill password
        password_field = driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)
        
        # Click login button
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Wait for login to complete - checking for home page elements
        print(colored("==> Waiting for login to complete...", 'cyan'))
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Search') or contains(text(), 'Home')]"))
        )
        time.sleep(3)
        return True
        
    except Exception as e:
        print(colored(f"[-] Login failed: {str(e)}", 'red'))
        return False

def get_profile_info(driver, username):
    """Extract profile information from Instagram"""
    try:
        victim_acc_url = f"https://www.instagram.com/{username}/"
        print(colored(f"==> Accessing profile: {victim_acc_url}", 'cyan'))
        driver.get(victim_acc_url)
        time.sleep(5)
        
        profile_data = {
            
            'name': "Not available",
            'posts': "Not available", 
            'followers': "Not available",
            'following': "Not available",
            'bio': "Not available",
            'url': victim_acc_url
        }
        
        # Try multiple selectors for each field
        print(colored("==> Extracting profile information...", 'cyan'))
        
        # Get profile name
        name_selectors = [
            
            "//h2",
            "//h1",
            "//header//h1",
            "//span[contains(@class, '_ap3a')]",
            "//div[contains(@class, '_aacl')]//span"
        ]
        
        for selector in name_selectors:
            try:
                name_element = driver.find_element(By.XPATH, selector)
                if name_element.text.strip():
                    profile_data['name'] = name_element.text
                    break
            except:
                continue
        
        # Get posts count
        posts_selectors = [
            
            "//span[contains(text(), 'posts')]/span",
            "//li[1]//span[@class='_ac2a']/span",
            "(//span[@class='html-span'])[1]",
            "//header//ul/li[1]//span"
        ]
        
        for selector in posts_selectors:
            try:
                posts_element = driver.find_element(By.XPATH, selector)
                if posts_element.text.strip():
                    profile_data['posts'] = posts_element.text
                    break
            except:
                continue
        
        # Get followers count
        followers_selectors = [
            
            "//a[contains(@href, 'followers')]//span",
            "//li[2]//span[@class='_ac2a']/span", 
            "(//span[@class='html-span'])[2]",
            "//header//ul/li[2]//span"
        ]
        
        for selector in followers_selectors:
            try:
                followers_element = driver.find_element(By.XPATH, selector)
                if followers_element.text.strip():
                    profile_data['followers'] = followers_element.text
                    break
            except:
                continue
        
        # Get following count
        following_selectors = [
            
            "//a[contains(@href, 'following')]//span",
            "//li[3]//span[@class='_ac2a']/span",
            "(//span[@class='html-span'])[3]",
            "//header//ul/li[3]//span"
        ]
        
        for selector in following_selectors:
            try:
                following_element = driver.find_element(By.XPATH, selector)
                if following_element.text.strip():
                    profile_data['following'] = following_element.text
                    break
            except:
                continue
        
        # Get bio
        bio_selectors = [
            
            "//div[contains(@class, '_aacu')]",
            "//header//div[contains(@class, '_aa_c')]//span",
            "//div[contains(text(), '')]//span",
            "//h1/following-sibling::div//span"
        ]
        
        for selector in bio_selectors:
            try:
                bio_element = driver.find_element(By.XPATH, selector)
                if bio_element.text.strip():
                    profile_data['bio'] = bio_element.text
                    break
            except:
                continue
        
        return profile_data
        
    except Exception as e:
        print(colored(f"[-] Error extracting profile info: {str(e)}", 'red'))
        return None

def take_screenshot(driver, username):
    """Take screenshot of profile page"""
    try:
        # Ensure we're on the profile page
        driver.get(f"https://www.instagram.com/{username}/")
        time.sleep(3)
        
        screenshot_name = f"{username}_InstaPage.png"
        driver.save_screenshot(screenshot_name)
        return screenshot_name
    except Exception as e:
        print(colored(f"[-] Error taking screenshot: {str(e)}", 'red'))
        return None

def display_menu():
    """Display the information menu"""
    print("\n" + "="*60)
    print(colored("INSTAGRAM OSINT INFORMATION MENU", 'yellow', attrs=['bold']))
    print("="*60)
    print(colored("[1] Profile Name", 'red'))
    print(colored("[2] Number Of Posts", 'green')) 
    print(colored("[3] Number Of Followers", 'yellow'))
    print(colored("[4] Number Of Followings", 'magenta'))
    print(colored("[5] Bio Information", 'cyan'))
    print(colored("[6] Profile URL", 'blue'))
    print(colored("[7] Take Screenshot", 'white'))
    print(colored("[8] Show All Information", 'green', attrs=['bold']))
    print(colored("[E] Exit", 'red', attrs=['bold']))
    print("="*60)

def main():
    proceed = True
    
    while proceed:
        try:
            print("\n")
            ui = input(colored("[ * ] Enter Your Instagram Username : ", 'green'))
            print("")
            ui2 = input(colored("[ * ] Enter Your Instagram Password : ", 'green'))
            print("")
            ui3 = input(colored("[ * ] Enter Victim's Instagram Username : ", 'red'))
            print("")
            
            print(colored("==> Setting up browser...", 'cyan'))
            driver = setup_driver()
            
            try:
                if login_to_instagram(driver, ui, ui2):
                    print(colored("✅ Logged in successfully!", 'green'))
                    
                    print(colored("==> Gathering profile information...", 'cyan'))
                    profile_info = get_profile_info(driver, ui3)
                    
                    if profile_info:
                        print(colored("✅ Information gathered successfully!", 'green'))
                        
                        proceed2 = True
                        while proceed2:
                            display_menu()
                            print("")
                            choice = input(colored("Select an option (1-8 or E): ", 'green')).strip().lower()
                            
                            if choice == '1':
                                print(colored(f"\n📝 Profile Name: {profile_info['name']}", 'red'))
                                
                            elif choice == '2':
                                print(colored(f"\n📊 Number of Posts: {profile_info['posts']}", 'green'))
                                
                            elif choice == '3':
                                print(colored(f"\n👥 Number of Followers: {profile_info['followers']}", 'yellow'))
                                
                            elif choice == '4':
                                print(colored(f"\n🔍 Number of Following: {profile_info['following']}", 'magenta'))
                                
                            elif choice == '5':
                                print(colored(f"\n📖 Bio: {profile_info['bio']}", 'cyan'))
                                
                            elif choice == '6':
                                print(colored(f"\n🔗 Profile URL: {profile_info['url']}", 'blue'))
                                
                            elif choice == '7':
                                print(colored("\n📸 Taking screenshot...", 'cyan'))
                                screenshot_name = take_screenshot(driver, ui3)
                                if screenshot_name:
                                    print(colored(f"✅ Screenshot saved as: {screenshot_name}", 'green'))
                                else:
                                    print(colored("❌ Failed to take screenshot", 'red'))
                                    
                            elif choice == '8':
                                print(colored("\n" + "="*50, 'yellow'))
                                print(colored("COMPLETE PROFILE INFORMATION", 'yellow', attrs=['bold']))
                                print("="*50)
                                print(colored(f"📝 Profile Name: {profile_info['name']}", 'red'))
                                print(colored(f"📊 Posts: {profile_info['posts']}", 'green'))
                                print(colored(f"👥 Followers: {profile_info['followers']}", 'yellow'))
                                print(colored(f"🔍 Following: {profile_info['following']}", 'magenta'))
                                print(colored(f"📖 Bio: {profile_info['bio']}", 'cyan'))
                                print(colored(f"🔗 URL: {profile_info['url']}", 'blue'))
                                print("="*50)
                                
                            elif choice == 'e':
                                proceed2 = False
                                print(colored(f"\n✅ OSINT completed for: {ui3}", 'green'))
                                
                            else:
                                print(colored("\n❌ Invalid option. Please try again.", 'red'))
                            
                            if choice != 'e':
                                input(colored("\nPress Enter to continue...", 'yellow'))
                                
                    else:
                        print(colored("❌ Failed to gather profile information", 'red'))
                else:
                    print(colored("❌ Login failed. Please check your credentials.", 'red'))
                    
            except Exception as e:
                print(colored(f"❌ An error occurred during operation: {str(e)}", 'red'))
                
            finally:
                print(colored("\n==> Closing browser...", 'cyan'))
                driver.quit()
                
            print("")
            continue_search = input(colored("[?] Do you want to search another account? (y/n): ", 'yellow')).strip().lower()
            if continue_search != 'y':
                proceed = False
                print(colored("\n🎯 Thank you for using Instagram OSINT Tool!", 'green'))
                
        except KeyboardInterrupt:
            print(colored("\n\n⏹️  Operation cancelled by user.", 'red'))
            proceed = False
        except Exception as e:
            print(colored(f"\n❌ Unexpected error: {str(e)}", 'red'))

if __name__ == "__main__":
    main()