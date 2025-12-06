# Pull Request Description Template

## Summary

Migrate dependency management from pip/requirements.txt to uv with pyproject.toml, modernize CI workflow, and drop support for EOL operating systems.

---

## Purpose

- **Modernize tooling**: uv provides faster, more reliable dependency management with lockfiles for reproducible builds
- **Reduce maintenance burden**: Remove EOL distros that are no longer supported upstream
- **Improve code quality**: Fix deprecated Ansible variable syntax and ansible-lint warnings
- **Add AI assistant documentation**: Include CLAUDE.md and AGENTS.md for coding agents

---

## Testing

How did you verify it works?

* [x] Added/updated tests
* [x] Ran `uv run ansible-lint`
* Notes: ansible-lint passes with 0 failures, 0 warnings. Molecule tests run via `uv run molecule test`.

---

## Related Issues

N/A - Maintenance/modernization task

---

## Changes

Brief list of main changes:

* Replace pip-based dependencies with uv (pyproject.toml + uv.lock)
* Update CI workflow to use `astral-sh/setup-uv@v4` and `uv run` commands
* Update distro matrix to supported versions only:
  - Ubuntu 22.04, Ubuntu 24.04
  - Rocky Linux 9
  - RHEL 9
* Remove EOL distros: CentOS 7, Ubuntu 20.04, Rocky 8, RHEL 7/8
* Fix deprecated `ansible_*` variables to use `ansible_facts['*']` format
* Quote octal file modes (e.g., `mode: "0644"`) to fix ansible-lint warnings
* Remove legacy files: `.travis.yml`, `.yamllint`, `test-requirements.txt`
* Add `ansible.cfg` for role path configuration
* Update README with testing instructions and distro matrix table
* Update `meta/main.yml` to reflect supported platforms and bump min_ansible_version to 2.14
* Add CLAUDE.md and AGENTS.md for AI assistant guidance

---

## Notes for Reviewers

* The uv.lock file is auto-generated and should not be manually edited
* CI now runs on ubuntu-22.04 runners (previously ubuntu-20.04)
* AGENTS.md is a symlink to CLAUDE.md to support different AI assistants

---

## Docs

* [x] Updated relevant documentation (README.md testing section, molecule README)
