# -*- mode: ruby -*-
# vi: set ft=ruby :

boxes = {}

['RHEL', 'DEBIAN', 'MACOSX'].each do |var|
  boxes[:"#{var.downcase}_box_name"] = ENV["VAGRANT_#{var.upcase}_BASED_BOX_NAME"]
  if boxes[:"#{var.downcase}_box_name"]
    puts "boxes[:#{var.downcase}_box_name] = " << boxes[:"#{var.downcase + '_box_name'}"].to_s
  end
end

Vagrant.configure(2) do |config|

  config.ssh.insert_key = false
  config.vm.synced_folder ".", "/vagrant", type: "rsync", rsync__exclude: ".git/"

  config.vm.define 'centos7' do |instance|
    instance.vm.box = boxes[:rhel_box_name] ? boxes[:rhel_box_name] : 'centos/7'
    instance.vm.network 'private_network', ip: '192.168.11.11'
  end

  config.vm.define 'ubuntu' do |instance|
    instance.vm.box = boxes[:debian_box_name] ? boxes[:debian_box_name] : 'ubuntu/trusty64'
    instance.vm.network 'private_network', ip: '192.168.11.12'
  end

  config.vm.provision :ansible do |ansible|
    ansible.sudo = true
    ansible.tags = ENV['VAGRANT_ANSIBLE_TAGS'] ? ENV['VAGRANT_ANSIBLE_TAGS'] : 'all'
    ansible.verbose = 'vv'
    ansible.playbook = 'test.yml'
    ansible.extra_vars = {
      ansible_user: 'vagrant',
      local_user: '{{ ansible_user }}',
      local_user_group: '{{ ansible_user }}',
    }
  end
end
