import re
import time
import paramiko
import json


class Routerssh():

    def __init__(self):
        self.ssh = paramiko.SSHClient()

    def ssh_login_show(self, router_ip, router_username, router_password, execute_cmd):
        """
        ssh login to devices : show commands
        """
        # Load SSH host keys.
        ssh.load_system_host_keys()
        # Add SSH host key automatically if needed.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Connect to router using username/password authentication.
        ssh.connect(router_ip, username=router_username, password=router_password, look_for_keys=False)
        # Run command.
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(execute_cmd)
        output = ssh_stdout.readlines()
        return output


if __name__ == "__main__":
    print("hi")
