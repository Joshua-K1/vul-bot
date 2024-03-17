include .env

.PHONY: all

build-local:
	./buildscripts/build_local.sh

build:
	./buildscripts/build_docker.sh

run-local:
	./buildscripts/run_local.sh

run:
	./buildscripts/run_docker.sh

tf-fmt:
	./buildscripts/fmt_terraform.sh

tf-lint:
	./buildscripts/lint_terraform.sh

tf-init:
	$(MAKE) tf-lint
	./buildscripts/init_terraform.sh

tf-init-local:
	$(MAKE) tf-lint
	./buildscripts/init_terraform.sh -l true

tf-plan:
	./buildscripts/plan_terraform.sh

tf-plan-local:
	./buildscripts/plan_terraform.sh -l true

tf-apply:
	./buildscripts/apply_terraform.sh

tf-destroy:
	./buildscripts/destroy_terraform.sh