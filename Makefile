  
.DEFAULT_GOAL := help
MAKEFILE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))

help:
	@echo "the ambient server installer"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

install: ## install the ambient-server as a service
	cp ambient-server.service /etc/systemd/system/ambient-server.service
	systemctl daemon-reload
	systemctl enable ambient-server.service
	@echo 'Run "systemctl start ambient-server"'

uninstall: ## remove the ambient-server from systemd
	-systemctl stop ambient-server.service
	systemctl disable ambient-server.service
	rm /etc/systemd/system/ambient-server.service
