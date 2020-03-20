from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_protect
from .models import ServerInfo
import json

# Create your views here.

# def serverInfo(request):
#     data = {
#         'servers': [
#             {
#                 'name': 'rhlab1',
#                 'os': 'Linux',
#                 'logicalDrive': '256GB',
#                 'processors': '4 Cores',
#                 'ram': 'TBC',
#                 'location': 'Halifax',
#                 'ipInternal': '10.100.107.23',
#                 'subnetMask': '255.155.255.0',
#                 'gateway': '10.100.107.254',
#                 'dns': 'TBC',
#                 'vlan': 'TBC',
#                 'ipExternal': 'TBC',
#                 'mns': 'TBC',
#             },
#             {
#                 'name': 'rhlab1',
#                 'os': 'Linux',
#                 'logicalDrive': '256GB',
#                 'processors': '4 Cores',
#                 'ram': 'TBC',
#                 'location': 'Halifax',
#                 'ipInternal': '10.100.107.23',
#                 'subnetMask': '255.155.255.0',
#                 'gateway': '10.100.107.254',
#                 'dns': 'TBC',
#                 'vlan': 'TBC',
#                 'ipExternal': 'TBC',
#                 'mns': 'TBC',
#             },
#             {
#                 'name': 'rhlab1',
#                 'os': 'Linux',
#                 'logicalDrive': '256GB',
#                 'processors': '4 Cores',
#                 'ram': 'TBC',
#                 'location': 'Halifax',
#                 'ipInternal': '10.100.107.23',
#                 'subnetMask': '255.155.255.0',
#                 'gateway': '10.100.107.254',
#                 'dns': 'TBC',
#                 'vlan': 'TBC',
#                 'ipExternal': 'TBC',
#                 'mns': 'TBC',
#             },
#         ],
#     }
#     return JsonResponse(data)


def serverInfo(request):
    try:
        serverName = request.GET.get("serverName")
        if serverName == None:
            servers = ServerInfo.object.all().values()
            return JsonResponse({'servers': list(servers)})
        else:
            servers = ServerInfo.object.filter(serverName=serverName).values()
            return JsonResponse({'servers': list(servers)})

        # server_json = [{'servers':list(servers)}]
        # print(server_json)
        # return HttpResponse(json.dump(server_json), 'application/json')
    except:
        return "This server not exist! "