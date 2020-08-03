import re
import time
import paramiko
from home.python_test.python_network.automation.library.cisco.basic.config.cfg_output.lib_cisco_login_output import Routerssh


class Routerssh_output():

    def __init__(self):
        self.ssh_out = Routerssh

    def ssh_login_show_ouput(self, router_ip, router_username, router_password, execute_cmd):
        """
        ssh login to devices output : show commands 
        """
        device_information = self.ssh_out.ssh_login_show(router_ip, router_username, router_password, execute_cmd)

