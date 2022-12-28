import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_service(host):
    if host.system_info.distribution == "debian":
        s = host.service("apache2")
        assert s.is_enabled
        assert s.is_running
    if host.system_info.distribution == "centos":
        s = host.service("httpd")
        assert s.is_enabled
        assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://0.0.0.0:80",
        "tcp://0.0.0.0:443"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening