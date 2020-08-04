import paramiko
import sys
import os
import pytest
import json
from library.cisco.basic.cfg_output.lib_cisco_login_output import Routerssh_output


class Test_login_to_devices():

    @pytest.fixture(scope='class', autouse=True)
    def initial_setup (self, request):
        """
        Set the variables at global
        """
        request.cls.comm_path = ""
        request.cls.feat_path = ""
        request.cls.comm_path = sys.path[3] + "/testcases/cisco/input_data/common_input.json"
        request.cls.feat_path = sys.path[3] + "/testcases/cisco/input_data/feature_input.json"
        request.cls.common_input_js = open(request.cls.comm_path, "r")
        request.cls.feature_input_js = open(request.cls.feat_path, "r")
        request.cls.common_input_dict = request.cls.common_input_js.read()
        request.cls.common_input = json.loads(request.cls.common_input_dict)
        request.cls.feature_input_dict = request.cls.feature_input_js.read()
        request.cls.feature_input = json.loads(request.cls.feature_input_dict)
        request.cls.device_mac = []
        request.cls.device_ip = []
        request.cls.device_user = []
        request.cls.device_pwd = []
        request.cls.all_devices = request.cls.common_input["cisco_devices"]["login_details"]
        for det in request.cls.common_input["cisco_devices"]["login_details"]:
            mac = det["device_mac"]
            ip = det["device_ip"]
            usr = det["device_user"]
            pwd = det["device_pwd"]
            request.cls.device_mac.append(mac)
            request.cls.device_ip.append(ip)
            request.cls.device_user.append(usr)
            request.cls.device_pwd.append(pwd)
        #

    def test001_ssh_login_show_ouput(self):
#         router_ip = str(self.device_ip[0])
#         router_username = str(self.device_user[0])
#         router_password = str(self.device_pwd[0])

        for det in self.all_devices:
            host = det["device_host"]
            mac = det["device_mac"]
            ip = det["device_ip"]
            usr = det["device_user"]
            pwd = det["device_pwd"]
            print ("#### Logged into device {}###".format(host))
            ssh = paramiko.SSHClient()
            ssh.load_system_host_keys()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, username=usr, password=pwd, look_for_keys=False)
            # Run command.
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip route")
            output = ssh_stdout.readlines()
            print (output)
            # Close connection.
            ssh.close()
            print ("#### Logged out from device {}###".format(host))
