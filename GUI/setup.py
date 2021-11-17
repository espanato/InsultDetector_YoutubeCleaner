from cx_Freeze import setup, Executable
base = None
executables = [Executable("main.py", base=base)]
packages = ["idna", "bs4", "requests", "pyperclip", "dash", "nltk", "sklearn"]
options = {
    'build_exe': {
        'packages': packages,
    },
}
setup(
    name="YoutubeCleaner",
    options=options,
    version="1.0",
    description='Cheh',
    executables=executables
)
