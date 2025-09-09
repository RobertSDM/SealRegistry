.PHONY: build

PYINSTALLER = $(CURDIR)/.venv/Scripts/pyinstaller.exe

build:
	$(PYINSTALLER) main.py --onefile --name cadlacre --noconsole