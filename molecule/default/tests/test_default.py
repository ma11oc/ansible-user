import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_user_root(host):
    pwhash = ''.join([
        u'$6$JOYM5lAJ3HsvqH1$PYCBLv8iXhjgG8eDXoHD5Y7iFADP49YUgxm6Hr7tqw67TJ',
        u'0bWIoYS4jSirW9pllqkE9Y.8KMF5xoprAJgtBkF1'
    ])
    user = host.user(u'root')
    assert user.password == pwhash


def test_user_foo(host):
    user = host.user(u'foo')
    assert user.exists


def test_user_foo_sudo(host):
    sudo_file = host.file(u'/etc/sudoers.d/foo')
    assert sudo_file.exists
    assert sudo_file.contains(u'foo')


def test_user_foo_sudo_pwless(host):
    cmd = host.run(u'sudo -iu foo sudo uname -a')
    assert cmd.rc == 0


def test_user_foo_ssh_key(host):
    auth_keys = host.file(u'/home/foo/.ssh/authorized_keys')
    assert auth_keys.exists
    assert auth_keys.contains(u'MARKER')


def test_user_bar_sudo_pwless(host):
    cmd = host.run(u'sudo -iu bar sudo uname -a')
    assert cmd.rc == 1


def test_user_bar_prompt(host):
    bashrc = host.file(u'/home/bar/.bashrc')
    assert bashrc.contains(u'PROMPT_COMMAND=set_prompt')
