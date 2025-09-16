# Makefile for Steam Stats EDA Dashboard

.PHONY: help install test clean dashboard notebook lint format

help:
	@echo "Steam Stats EDA Dashboard - Available Commands:"
	@echo ""
	@echo "  install     Install project dependencies"
	@echo "  test        Run unit tests"
	@echo "  clean       Clean up temporary files"
	@echo "  dashboard   Launch Streamlit dashboard"
	@echo "  notebook    Start Jupyter notebook server"
	@echo "  lint        Run code linting"
	@echo "  format      Format code with black"
	@echo "  setup       Run initial project setup"

install:
	pip install -r requirements.txt

test:
	python -m pytest tests/ -v

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

dashboard:
	streamlit run dashboards/streamlit_app.py

notebook:
	jupyter notebook notebooks/

lint:
	flake8 src/ tests/ dashboards/

format:
	black src/ tests/ dashboards/
	isort src/ tests/ dashboards/

setup:
	python setup.py