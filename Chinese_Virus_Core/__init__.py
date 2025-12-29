# __init__.py

try:
    from virus import start_virus
except:
    try:
        from .virus import start_virus
    except:
        from Chinese_Virus_Core.virus import start_virus


__all__ = ['start_virus']