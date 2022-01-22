# ansible-user

This role provides an ability of high-level user management on target systems


## Requirements

- `ansible` version >= 2.0


## Role Variables

The following block describes default values of variables. It will be merged with variables, defined by user as role vars (see [Example Playbook](#example-playbook)).

```yaml
user_defaults:
  enabled: true
  password: null
  sudo:
    enabled: false
    passwordless: false
  prompt:
    enabled: false
    systemwide: false
  public_key: null
```

## Dependencies

None


## Example Playbook

Since role's variables will be merged with defaults, you need to define only required variables.

```yaml
---
- hosts: bootstrap_hosts
  vars:
  roles:
    - role: ansible-user
      users:
        - name: root
          password: "$6$DuTTmMSk/JaS$GF.08qDPa7EqhoYt/BMwrrwVO0ojDWAvhKlZ/UgFQ8.Xfp0duQBp8Z6YIe/q/bF29etOoJ23r49VZtEKHyqAc."

        - name: user1
          sudo:
            enabled: true
            passwordless: true
          public_key: |
            ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDH0NvqvX7QBLryFe6MYD8cW459FHoMRbaM5Gn6IH30Hg0ll5gAKMshlNVfhspWAg6VAqR57qP3ofbuwaq4VOMmOwUfz+Orkakknv+BxNmvue3SXI5VxYINF4VbOZVLsDopqMYqCqM9wVYQg/KBUW6GXZ2nvZ4ZI5LS9epYjyK8clXeeA/CT64S1m/1iAUi7WOovp1aq38lcdBalH6QRfJe0NKSnAAsWeMq77IN10Zn0YfyFPihQI8yujShjH9mLgygxEQ13PmKjfDOxwNes7+EATqBj59cHLf65Qih/h5bLD/Uuj++mckmvdjtb190V3XWa0bpoDGFWD/hncP+FFbX workstation

        - name: user2
          password: "$6$QbzN8OUg$oY5HhEDpfWfw5q40kp/tHmGOadaZ5bnPOtnyiPq8B5HZAqoLYOaVgtF1Rd5mIvaCM10YamNWzT2Qw9ObaiHt81"
          sudo:
            enabled: true
          prompt:
            enabled: true

```

For the first time the usage will be something like this:

```bash
ansible-playbook -l hosts site.yml --ask-pass -e 'ansible_user=root'
```


## Testing
### Requirements
- [molecule](https://github.com/metacloud/molecule)
- [testinfra](https://github.com/philpep/testinfra)
- [docker](https://www.docker.com/)

### Running the tests
- you have to pull each docker image which is defined within `platforms` section in `molecule/default/molecule.yml` config file **before running the tests**:
```
docker pull centos:7
```

- run molecule tests
```
cd /to/project/root
molecule test
```

## Versioning

[SemVer](http://semver.org/) is used for versioning.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


## Authors

* **Alexey Shchukin** - Initial work
