# ➤ CONFIGURATION
DOCKER_RUN = docker-compose exec app

# ➤ BUILD
build:
	docker-compose up -d --build

# ➤ CLEAN & PURGE
clean:
	docker-compose down -v
	docker system prune -f

purge:
	docker-compose down -v --rmi all --remove-orphans
	docker system prune -f

# ➤ GLOBAL TESTS
test_all:
	@$(DOCKER_RUN) pytest tests/

# ================================
# ➤ EXERCISE TARGETS TEMPLATE
# ================================

define EX_TEMPLATE
run_ex$(1):
	@$(DOCKER_RUN) python ex$(1)/tester.py

test_$(1):
	@$(DOCKER_RUN) pytest -s -v tests/test_$(1).py
endef

$(foreach n,00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15,$(eval $(call EX_TEMPLATE,$(n))))

# ➤ HELP
help:
	@echo ""
	@echo "⚙️  USAGE"
	@echo "--------------------------------------"
	@echo " build          -> docker-compose up -d --build"
	@echo " clean          -> docker-compose down -v && prune"
	@echo " purge          -> docker-compose down -v --rmi all --remove-orphans"
	@echo " test_all       -> Run all unit tests (pytest)"
	@echo ""
	@echo "🏃‍♂️ Run examples"
	@echo " run_ex00       -> Run ex00 tester.py"
	@echo " test_ex00      -> Run pytest for ex00"
	@echo " run_ex01       -> Run ex01 tester.py"
	@echo " test_ex01      -> Run pytest for ex01"
	@echo " ..."
	@echo "--------------------------------------"
