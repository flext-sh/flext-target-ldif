# flext-target-ldif - LDIF Singer Target
PROJECT_NAME := flext-target-ldif
ifneq ("$(wildcard ../base.mk)", "")
include ../base.mk
else
include base.mk
endif

# === PROJECT-SPECIFIC TARGETS ===
.PHONY: target-run test-unit test-integration build shell

target-run: ## Run target with config
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run target-ldif --config config.json

.DEFAULT_GOAL := help
