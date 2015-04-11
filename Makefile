ifeq ($(OS), Windows_NT)
	RM := del /F /Q
else
	RM := rm -rf
endif

test:
	python tools/test.py

clean:
	$(RM) main\__pycache__
