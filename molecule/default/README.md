# Molecule test this role


## Scenario - `default`
Test run of this role

Run Molecule test
```
molecule test
```

Run test with variable example
```
MOLECULE_DISTRO=centos7 molecule test
```

### Variables
 - `MOLECULE_DISTRO` OS of docker container to test, default `ubuntu2204`
    List of tested distros
    - `centos7`
    - `ubuntu2004`
    - `ubuntu2204`
    - `rockylinux8`
    - `rockylinux9`
    - `rhel7`
    - `rhel8`
    - `rhel9`
 - `MOLECULE_ANSIBLE_VERBOSITY` 0-3 used for troubleshooting, will set verbosity of ansible output, same as `-vvv`, default `0`
