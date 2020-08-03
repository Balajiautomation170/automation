import paramiko
import sys
import pytest
import json


class Test_login_to_devices():

    @pytest.fixture(scope='class', autouse=True)
    def initial_setup (self, request):
        """
        Set the variables at global
        """
        common_input_js = open("/home/python_test/python_network/automation/testcases/cisco/input_data/common_input.json", "r")
        feature_input_js = open("/home/python_test/python_network/automation/testcases/cisco/input_data/feature_input.json", "r")
        common_output = common_input_js.read()
        feature_output = feature_input_js.read()
        common_input = json.loads(common_output)
        feature_input = json.loads(feature_output)
        request.cls.device_mac = []
        request.cls.device_ip = []
        request.cls.device_user = []
        request.cls.device_pwd = []
        request.cls.all_devices = common_input["cisco_devices"]["login_details"]
        for det in common_input["cisco_devices"]["login_details"]:
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
        # ## cut
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
