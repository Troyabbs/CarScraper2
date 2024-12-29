import requests
import zipfile
import io
import os
import shutil

def download_chromedriver():
    print("Downloading latest ChromeDriver...")
    
    # URL for the latest stable ChromeDriver
    url = "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE"
    version = requests.get(url).text.strip()
    print(f"Latest stable version: {version}")
    
    # Download URL for Windows
    download_url = f"https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/{version}/win64/chromedriver-win64.zip"
    print(f"Downloading from: {download_url}")
    
    response = requests.get(download_url)
    
    if response.status_code == 200:
        # Extract the zip file
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
            # Create a temporary directory for extraction
            if not os.path.exists("temp"):
                os.makedirs("temp")
            
            # Extract to temp directory
            zip_ref.extractall("temp")
            
            # Move the chromedriver to the current directory
            src = os.path.join("temp", "chromedriver-win64", "chromedriver.exe")
            dst = "chromedriver.exe"
            
            # Remove existing chromedriver if it exists
            if os.path.exists(dst):
                os.remove(dst)
            
            # Move new chromedriver to current directory
            shutil.move(src, dst)
            
            # Clean up temp directory
            shutil.rmtree("temp")
            
        print("ChromeDriver successfully updated!")
        return True
    else:
        print(f"Failed to download ChromeDriver. Status code: {response.status_code}")
        return False

if __name__ == "__main__":
    download_chromedriver()
