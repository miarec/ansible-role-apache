This file provides guidance to coding agent when working with code in this repository.

## Overview

This is an Ansible role for installing and configuring Apache 2.x on Ubuntu 22.04/24.04, Rocky Linux 9, and RHEL 9.

## Testing Commands

```bash
# Run molecule tests (default: Ubuntu 24.04)
uv run molecule test

# Run tests for a specific distro
MOLECULE_DISTRO=ubuntu2404 uv run molecule test
MOLECULE_DISTRO=rockylinux9 uv run molecule test

# Run individual molecule stages
uv run molecule converge     # Apply the role
uv run molecule verify       # Run testinfra tests
uv run molecule destroy      # Clean up containers

# Run ansible-lint
uv run ansible-lint
```

Available distros: `ubuntu2204`, `ubuntu2404`, `rockylinux9`, `rhel9`

## Role Architecture

The role uses OS-family-based variable loading and task separation:

- **Entry point**: `tasks/main.yml` - Loads OS-specific vars, installs Apache, detects version, configures based on OS family
- **OS variables**: `vars/Debian.yml`, `vars/RedHat.yml` - Package names, service names, paths
- **Version variables**: `vars/apache-22.yml`, `vars/apache-24.yml` - Version-specific configuration directives
- **Configuration tasks**: `tasks/configure-Debian.yml`, `tasks/configure-RedHat.yml`
- **Templates**: `templates/vhosts.conf.j2` - VirtualHost configuration

Key differences by platform:
- Debian/Ubuntu: Service `apache2`, config at `/etc/apache2`, uses `a2enmod`/`a2ensite` style symlinks
- RedHat/Rocky: Service `httpd`, config at `/etc/httpd/conf.d`, modules via packages

## Default Variables

All defaults are in `defaults/main.yml`. Key variables:
- `apache_listen_port`: HTTP port (default: 80)
- `apache_listen_port_ssl`: HTTPS port (default: 443)
- `apache_vhosts`: List of VirtualHost configurations
- `apache_mods_enabled`: Apache modules to enable (Debian/Ubuntu only)
