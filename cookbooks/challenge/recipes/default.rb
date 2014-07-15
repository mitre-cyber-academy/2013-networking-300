cookbook_file "/etc/init.d/challenge" do
  source "startserver_init_d"
  mode 0755
end

package "python" do
  action :install
end

remote_directory "/opt/challenge" do
  source "src"
  owner "root"
  group "root"
end

file "/opt/challenge/asciiServer.sh" do
  mode "755"
end

service "challenge" do
  supports :start => true, :stop => true, :restart => true
  action [:start, :enable]
end