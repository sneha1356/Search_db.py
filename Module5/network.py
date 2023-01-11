import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="10.0.",username=".\\test",password="pass@word1")
stdin,stdout,stderr=ssh.exec_command("free -m")
print(stdout.readlines())
stdout.close()
