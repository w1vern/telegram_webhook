.PHONY: back

back:
	uvicorn main:app --reload

back_install:
	uv sync
