import requests
import json


class Connection:
    pmApi = ''
    pmAuthJson = {}

    def set_session(self, myApi, myAuthJson):
        self.pmApi = myApi
        self.pmAuthJson = myAuthJson
        return

    def get_token(self, pmUser, pmPass):
        apiAuth = self.pmAPI + '/api2/json/access/ticket'
        payload = {'username': pmUser, 'password': pmPass}
        pm_session = requests.post(self.pmAuthJson, payload, verify=False)
        return pm_session.json()

    def get_nodes(self):
        apiNodes = self.pmApi + "/api2/json/nodes"
        pm_nodes = requests.get(apiNodes, headers=self.pmAuthJson, verify=False)
        return pm_nodes.json()

    def get_node_network_bridges(self, vmNode):
        apiNodeBridges = self.pmApi + "/api2/json/nodes/" + vmNode + "/network"
        pm_node_bridges = requests.get(apiNodeBridges, headers=self.pmAuthJson, verify=False)

        node_bridges = {}
        node_bridges_array = []

        # parse for VM bridge interfaces
        for interface in pm_node_bridges.json()["data"]:
            if interface["iface"].startswith("vmbr"):
                node_bridges_array.append(interface["iface"])

        node_bridges[vmNode] = node_bridges_array
        node_bridges_json = json.dumps(node_bridges)
        return node_bridges_json

    def get_virtual_machines(self, vmNode):
        apiNodeVms = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu"
        pm_node_vms = requests.get(apiNodeVms, headers=self.pmAuthJson, verify=False)
        return pm_node_vms.json()

    def get_snapshots(self, vmNode, vmID):
        apiSnapshots = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot"
        pm_snapshots = requests.get(apiSnapshots, headers=self.pmAuthJson, verify="False")
        return pm_snapshots.json()

    def create_snapshot(self, vmNode, vmID, snapshotName, includeRam="0", description='Created by Python'):
        data = {
            "node": vmNode,
            "snapname": snapshotName,
            "vmid": vmID,
            "description": description,
            "vmstate": includeRam
        }
        apiCreateSnapshot = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot"
        pm_create_snapshot = requests.post(apiCreateSnapshot, headers=self.pmAuthJson, data=data, verify=False)
        return pm_create_snapshot.json()

    def delete_snapshot(self, vmNode, vmID, snapshotName, forceDelete="0"):
        newHeader = {
            "Authorization": self.pmAuthJson["Authorization"],
            "node": vmNode,
            "snapname": snapshotName,
            "vmid": vmID,
            "force": forceDelete
        }
        apiDeleteSnapshot = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot/" + snapshotName
        print(apiDeleteSnapshot)
        pm_delete_snapshot = requests.delete(apiDeleteSnapshot, headers=newHeader, verify=False)
        return pm_delete_snapshot

    def get_vm_config(self, vmNode, vmID, currentSetting='0'):
        newHeader = {
            "Authorization": self.pmAuthJson["Authorization"],
            "node": vmNode,
            "vmid": vmID,
            "current": currentSetting
        }
        apiGetVmConfig = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/config"
        pm_vm_config = requests.get(apiGetVmConfig, headers=newHeader, verify=False)
        return pm_vm_config.json()

    def set_network_bridge(self, vmNode, vmID, vmNetId='net0', vmNetBridge='e1000,bridge=vmbr0,firewall=0,link_down=0'):
        # vmNetBridge should look like 'e1000,bridge=vmbr0'
        data = {
            "node": vmNode,
            "vmid": vmID,
            vmNetId: vmNetBridge
        }
        apiSetNetBridge = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/config"
        pm_set_net_bridge = requests.post(apiSetNetBridge, headers=self.pmAuthJson, data=data, verify=False)
        return pm_set_net_bridge.json()