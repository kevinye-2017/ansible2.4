excute playbook with ansible 2.4 api

set ssh no check host fingerprints

sed -i 's/#host_key_checking = False/host_key_checking = False/g' /etc/ansible/ansible.cfg

pip install ansible==2.4 or yum install ansible or sudo zypper in ansible  | just make sure ansible version ==2.4

###############
./run.py -h
###############
