SCSS_PATH = nexus9k/scss
CSS_PATH = nexus9k/static/css

.PHONY: compile-scss compile-scss-debug install run run-public watch-scss

compile-scss:
	sassc $(SCSS_PATH)/main.scss $(CSS_PATH)/main.css --output-style compressed

compile-scss-debug:
	sassc $(SCSS_PATH)/main.scss $(CSS_PATH)/main.css --sourcemap

install:
	pip install -r requirements.txt

run:
	python manage.py runserver

run-public:
	python manage.py runserver 0.0.0.0:8000

watch-scss:
	watchmedo shell-command \
		--patterns=*.scss \
		--recursive \
		--command='make compile-scss' $(SCSS_PATH)