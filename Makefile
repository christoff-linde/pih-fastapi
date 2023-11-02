.PHONY: default
default: build

.PHONY: help
help: ## Prints help for targets with comments
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build all containers
	docker compose build

.PHONY: up
up: create-dev-env-file ## Build & start all services
	docker compose up -d

.PHONY: down
down: create-dev-env-file ## Stop all services
	docker compose stop -t 1

.PHONY: restart
restart: ## Restart all services
	down up

.PHONY: create-dev-env-file
create-dev-env-file: ## Create a development environment file
	if [ ! -f .env ]; then cp .env.skel .env; fi

.PHONY: wipe
wipe: down ## Delete all services and data
	docker compose -rf -f -v

.PHONY: migrations
migrations: ## Generate databse migrations
	docker exec -i -t pig-fastapi-backend almbic revision --autogenerate

.PHONY: merge-migrations
merge-migrations: ## Merge database migrations
	docker exec -i -t pih-fastapi-backend alembic merge heads

.PHONY: run-migrations
run-migrations: ## Run database migrations
	docker exec -i -t pih-fastapi-backend alembic upgrade head

.PHONY: test
test: ## Run tests. Set test=<test_file_name> to run a specific test
	docker exec -i -t pih-fastapi-backend pytest -vv -s -o log_cli=true -o log_cli_level=DEBUG -o cache_dir=/tmp tests/$(test)
