Vagrant.configure("2") do |config|
  config.vm.box = "roboxes-p64/debian12"
  config.vm.provider :libvirt do |libvirt|
    libvirt.memory = 1024
    libvirt.cpus = 1
  end

  config.vm.define "staging" do |st|
    st.vm.hostname = "staging"
    st.vm.network "private_network", ip: "192.168.122.10"
  end

  config.vm.define "production" do |prod|
    prod.vm.hostname = "production"
    prod.vm.network "private_network", ip: "192.168.122.11"
  end

  config.vm.define "mock" do |mock|
    mock.vm.hostname = "mock"
    mock.vm.network "private_network", ip: "192.168.122.20"
    mock.vm.provider :libvirt do |libvirt|
      libvirt.memory = 512
    end
  end
end
