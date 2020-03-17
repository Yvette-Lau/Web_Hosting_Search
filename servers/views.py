from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def serverInfo(request):
    data = {
        'servers': [
            {
                'name': 'rhlab1',
                'os': 'Linux',
                'logicalDrive': '256GB',
                'processors': '4 Cores',
                'ram': 'TBC',
                'location': 'Halifax',
                'ipInternal': '10.100.107.23',
                'subnetMask': '255.155.255.0',
                'gateway': '10.100.107.254',
                'dns': 'TBC',
                'vlan': 'TBC',
                'ipExternal': 'TBC',
                'mns': 'TBC',
            },
            {
                'name': 'rhlab1',
                'os': 'Linux',
                'logicalDrive': '256GB',
                'processors': '4 Cores',
                'ram': 'TBC',
                'location': 'Halifax',
                'ipInternal': '10.100.107.23',
                'subnetMask': '255.155.255.0',
                'gateway': '10.100.107.254',
                'dns': 'TBC',
                'vlan': 'TBC',
                'ipExternal': 'TBC',
                'mns': 'TBC',
            },
            {
                'name': 'rhlab1',
                'os': 'Linux',
                'logicalDrive': '256GB',
                'processors': '4 Cores',
                'ram': 'TBC',
                'location': 'Halifax',
                'ipInternal': '10.100.107.23',
                'subnetMask': '255.155.255.0',
                'gateway': '10.100.107.254',
                'dns': 'TBC',
                'vlan': 'TBC',
                'ipExternal': 'TBC',
                'mns': 'TBC',
            },
        ],
    }
    return JsonResponse(data)