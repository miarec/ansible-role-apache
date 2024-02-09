import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    if host.system_info.distribution == "ubuntu":
        dirs = [
            "/etc/apache2"
        ]
    else:
        dirs = [
            "/etc/httpd",
            "/etc/httpd/conf.d"
        ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_files(host):
    if host.system_info.distribution == "ubuntu":
        files = [
            "/etc/apache2/mods-enabled/ssl.load",
            "/etc/apache2/mods-enabled/rewrite.load",
            "/etc/apache2/sites-available/vhosts.conf",
            "/etc/apache2/sites-enabled/vhosts.conf"
        ]
    else:
        files = [
            "/etc/httpd/conf.d/vhosts.conf"
        ]
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    if host.system_info.distribution == "ubuntu":
        s = host.service("apache2")
    else:
        s = host.service("httpd")

    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    sockets = [
        "tcp://0.0.0.0:443",
        "tcp://0.0.0.0:80"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening