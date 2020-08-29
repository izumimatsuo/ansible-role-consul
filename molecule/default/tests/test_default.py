import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_consul_is_installed(host):
    assert host.exists('consul')


def test_consul_running_and_enabled(host):
    service = host.service('consul')
    assert service.is_running
    assert service.is_enabled


def test_consul_is_listen(host):
    assert host.socket('tcp://127.0.0.1:8500').is_listening
    assert host.socket('tcp://127.0.0.1:8600').is_listening
    assert host.socket('udp://127.0.0.1:8600').is_listening


def test_dnsmasq_is_installed(host):
    package = host.package('dnsmasq')
    assert package.is_installed
    assert package.version.startswith('2.76')


def test_dnsmasq_running_and_enabled(host):
    service = host.service('dnsmasq')
    assert service.is_running
    assert service.is_enabled


def test_dnsmasq_is_listen(host):
    assert host.socket('tcp://0.0.0.0:53').is_listening
