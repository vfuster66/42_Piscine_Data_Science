.PHONY: build run clean shell \
        run-ex00 run-ex01 run-ex02 run-ex03 run-ex04 \
        test-ex00 test-ex01 test-ex02 test-ex03 test-ex04 all-tests

# Variables d'environnement (à adapter si besoin)
PGHOST = host.docker.internal
PGUSER = vfuster
PGPORT = 5432
PGDATABASE = piscineds
PGPASSWORD = Bonjour42

build:
	docker-compose build

# Shell interactif (bash dans le container Python)
shell:
	PGHOST=$(PGHOST) docker-compose run python bash

# Se connecter à PostgreSQL via psql depuis Docker (pour debug)
psql:
	docker run -it --rm postgres:15-alpine psql -h $(PGHOST) -p $(PGPORT) -U $(PGUSER) -d $(PGDATABASE)

# Nettoyer le container
clean:
	docker-compose down

# Commandes pour exécuter chaque script Python
run-ex02:
	PGHOST=$(PGHOST) docker-compose run python python ex02/table.py

run-ex03:
	PGHOST=$(PGHOST) docker-compose run python python ex03/automatic_table.py

run-ex04:
	PGHOST=$(PGHOST) docker-compose run python python ex04/items_table.py

# Commandes pour exécuter les tests unitaires
test-ex02:
	PGHOST=$(PGHOST) docker-compose run python pytest tests/test_02.py

test-ex03:
	PGHOST=$(PGHOST) docker-compose run python pytest tests/test_03.py

test-ex04:
	PGHOST=$(PGHOST) docker-compose run python pytest tests/test_04.py

# Commande pour exécuter tous les tests
all-tests:
	PGHOST=$(PGHOST) docker-compose run python pytest tests/
