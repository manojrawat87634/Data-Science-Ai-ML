from bs4 import BeautifulSoup

def extract_image_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    image_links = []

    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            image_links.append(src)

    return image_links

def main():
    print("Choose input method:")
    print("1. Paste HTML code")
    print("2. Enter HTML file path")
    
    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == '1':
        print("\nPaste your HTML (end with a blank line):")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        html_content = "\n".join(lines)

    elif choice == '2':
        file_path = input("Enter full path to the HTML file: ").strip()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
            return
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    image_links = extract_image_links(html_content)
    
    print(f"\nFound {len(image_links)} image link(s):\n")
    for url in image_links:
        print(url)

if __name__ == "__main__":
    main()
