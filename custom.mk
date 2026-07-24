# Private project handlers for flext-target-ldif.
# Strict extension: only `_custom_<verb>_<what>` handlers and `(pre|post)-<verb>[-<what>]`
# hooks. Public targets, toolchain vars, .DEFAULT_GOAL, includes, and help are
# invalid (base.mk owns those). Invoke via `make run WHAT=<what>`.
.PHONY: _custom_run_target
_custom_run_target: ## make run WHAT=target — run target with config.json
	$(Q)PYTHONPATH=$(SRC_DIR) $(POETRY) run target-ldif --config config.json
