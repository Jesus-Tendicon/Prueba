from datetime import datetime
import webbrowser

def main():
    now = datetime.now()
    print(f"Script ejecutado en: {now}")
    
    # Abrir la página de Google
    webbrowser.open('https://www.google.com')

if __name__ == "__main__":
    main()
