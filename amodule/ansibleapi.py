#!/usr/bin/env python
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
import json

'''
class bcolors:
    HEADER = '\033[95m'     #pink
    OKBLUE = '\033[94m'     #blue
    OKGREEN = '\033[92m'    #green
    WARNING = '\033[93m'    #yellow
    FAIL = '\033[91m'       #red
    WHITE = '\033[37m'      #white
    ENDC = '\033[0m'	    #end colors

class ResultCallback(CallbackBase):
	#override CallbackBase
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
	re = result._result
'''
def ansible_playbook(*args,**kwargs):
    pbpath = kwargs['pbpath']
    password = kwargs['password']    
    Options = namedtuple('Options',
                         ['listtags', 'listtasks', 'listhosts', 'syntax', 'connection', 'module_path', 'forks',
                          'remote_user', 'private_key_file', 'ssh_common_args', 'ssh_extra_args', 'sftp_extra_args',
                          'scp_extra_args', 'become', 'become_method', 'become_user', 'verbosity', 'check', 'diff'])
    loader = DataLoader()
    options = Options(listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                      module_path=None, forks=100, remote_user='root', private_key_file=None,
                      ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                      become_method=None, become_user='root', verbosity=None, check=False, diff=False)
    passwords = dict(conn_pass=password)
    inventory = InventoryManager(loader=loader, sources=['/etc/ansible/hosts'])
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    playbook = PlaybookExecutor(playbooks=[pbpath], inventory=inventory, variable_manager=variable_manager, loader=loader,
                            options=options, passwords=passwords)
    #callback = ResultCallback()
    #playbook._tqm._stdout_callback = callback
    playbook.run()

if __name__=="__main__":
    ansible_playbook(pbpath='/home/sw/github/ansible2.4/test.yml',password='654321')
