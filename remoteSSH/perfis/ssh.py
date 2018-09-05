from command.models import Command
from computer.models import Computer
import paramiko
import sys

def verifyConnection(computers):
 
        # Cria variavel com paramiko SSH
        client = paramiko.SSHClient()

        # Loop nos computadores 
        for cp in computers:

            # Declara atributo da conexao
            user = str(cp.user)
            hostname = str(cp.ip)
            password = str(cp.password)

            # Carrega as chaves de conexao conhecida do sistema
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.WarningPolicy)  

            # Testa conexao              
            try:
                client.connect(hostname, "22", user, password, timeout = 2)
                computer = Computer.objects.get(id = cp.id)
                computer.status = 1
                computer.save()
            except:
                computer = Computer.objects.get(id = cp.id)
                computer.status = 0
                computer.save()

            # Encerra conexaos
            client.close()