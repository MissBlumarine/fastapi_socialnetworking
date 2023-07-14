MAKEFILE_PATH := $(lastword $(abspath $(MAKEFILE_LIST)))
ROOT_DIR := $(dir $(MAKEFILE_PATH))

api-install:
	cd ${ROOT_DIR}/api/; poetry install;

api-dev:
	cd ${ROOT_DIR}/api/; poetry run uvicorn main:app --reload;

db-up:
	docker-compose -f stack.yml up --build >> /dev/null 2>&1 &