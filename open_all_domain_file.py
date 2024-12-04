import webbrowser
import time

def open_domains_in_chrome(file_path, delay=1):
    try:
        with open(file_path, 'r') as file:
            domains = file.readlines()
        
        domains = [domain.strip() for domain in domains if domain.strip()]
        
        if not domains:
            print("No domains found in the file.")
            return
        
        for domain in domains:
            print(f"Opening: {domain}")
            webbrowser.open(f"http://{domain}")  
            time.sleep(delay)  
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "C:\clg\scripts\domains.txt" 
    open_domains_in_chrome(file_path)
