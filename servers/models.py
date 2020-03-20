from django.db import models

# Create your models here.

class ServerInfo(models.Model):
    serverName = models.CharField(max_length=60)
    serverOS = models.CharField(max_length=100)
    serverLogicalDrive = models.CharField(max_length=20)
    serverProcessors = models.CharField(max_length=20)
    serverRam = models.CharField(max_length=40)
    serverLocation = models.TextField()
    serverIpInternal = models.GenericIPAddressField()
    serverSubnetMask = models.GenericIPAddressField()
    serverGateway = models.GenericIPAddressField()
    serverDns = models.CharField(max_length=50)
    serverVlan = models.CharField(max_length=50)
    serverIpExternal = models.GenericIPAddressField()
    serverMns = models.CharField(max_length=100)
    object = models.Manager()

    def __str__(self):
        return self.serverName
