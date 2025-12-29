# __main__.py

try:
    from virus import start_virus
except:
    try:
        from .virus import start_virus
    except:
        from Chinese_Virus_Core.virus import start_virus

def main():
    start_virus()

if __name__ == '__main__':
    main()