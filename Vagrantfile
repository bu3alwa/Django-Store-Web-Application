Vagrant.configure("2") do |config|

    config.vm.box = "ubuntu/xenial64"

    config.ssh.forward_agent = true
    config.vm.network :forwarded_port, guest: 80, host: 8000, auto_correct: true
    config.vm.provision :shell, path:"bootstrap.sh"
    config.vm.synced_folder "python-store/", "/var/www/python-store", owner: "www-data", group: "www-data"

end
