#!/bin/bash
sed -i "s#<<api_version>>#$branch_version#g" tests/integration/integration_config.yml
sed -i "s#<<controller>>#$controller_ip#g" tests/integration/integration_config.yml
sed -i "s#<<username>>#admin#g" tests/integration/integration_config.yml
sed -i "s#<<password>>#admin#g" tests/integration/integration_config.yml
sed -i "s#<<vcenter_host>>#$vcenter_host#g" tests/integration/integration_config.yml
sed -i "s#<<vcenter_username>>#$vcenter_username#g" tests/integration/integration_config.yml
sed -i "s#<<vcenter_password>>#$vcenter_password#g" tests/integration/integration_config.yml
sed -i "s#<<datacenter>>#$datacenter#g" tests/integration/integration_config.yml
sed -i "s#<<cluster>>#$cluster#g" tests/integration/integration_config.yml
sed -i "s#<<network>>#$network#g" tests/integration/integration_config.yml
sed -i "s#<<vcenter_folder>>#$vcenter_folder#g" tests/integration/integration_config.yml
sed -i "s#<<ovftool_path>>#$ovftool_path#g" tests/integration/integration_config.yml
sed -i "s#<<con_ova_path>>#$ova_path#g" tests/integration/integration_config.yml
sed -i "s#<<con_vm_name>>#ansible-test-controller#g" tests/integration/integration_config.yml

echo "Started ansible integration tests execution."
python38=3.8
for version in 3.5 3.6 3.7 3.8 3.9
do
  cd ~/.ansible/collections/ansible_collections/vmware/alb
  echo "Ansible test runing on python version: $version"
  st=$( echo "$version < $python38"| bc )
  if [ "$st -eq 1" ]
  then
    sudo ansible-test integration --exclude test_avi_serviceenginegroup --python $version --docker --docker-privileged
  else
    sudo ansible-test integration --python $version --docker --docker-privileged
  fi
done
echo "Ansible tests integration tests execution completed."
