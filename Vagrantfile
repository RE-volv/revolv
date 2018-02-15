# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # Base box to build off, and download URL for when it doesn't exist on the user's system already
    config.vm.box = "ubuntu/trusty64"

    # Boot with a GUI so you can see the screen. (Default is headless)
    # config.vm.boot_mode = :gui

    # Assign this VM to a host only network IP, allowing you to access it
    # via the IP.
    # config.vm.network "33.33.33.10"

    # Forward a port from the guest to the host, which allows for outside
    # computers to access the VM, whereas host only networking does not.
    config.vm.network :forwarded_port, guest: 8000, host: 8000

    # Share an additional folder to the guest VM. The first argument is
    # an identifier, the second is the path on the guest to mount the
    # folder, and the third is the path on the host to the actual folder.
    config.vm.synced_folder ".", "/vagrant"

    # Enable provisioning with a shell script.
    config.vm.provision :shell, path: "vagrant/install.sh"

    config.vm.provider "virtualbox" do |vb|
        vb.customize [ "guestproperty", "set", :id, "/VirtualBox/GuestAdd/VBoxService/--timesync-set-threshold", 10000 ]
    end
end
