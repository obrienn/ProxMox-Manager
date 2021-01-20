import requests
import json
import time


class Connection:
    requests.packages.urllib3.disable_warnings()
    pmApi = ''
    pmAuthJson = {}
    virtual_machines = {}
    snapshots = {}
    pools = {}
    bridges = {}

    def set_session(self, myApi, myAuthJson):
        self.pmApi = myApi
        self.pmAuthJson = myAuthJson
        return

    def get_token(self, pmUser, pmPass):
        apiAuth = self.pmAPI + '/api2/json/access/ticket'
        payload = {'username': pmUser, 'password': pmPass}
        pm_session = requests.post(self.pmAuthJson, payload, verify=False)
        return pm_session.json()

    def get_task_status(self, vmNode, upid):
        apiTaskStatus = self.pmApi + "/api2/json/nodes/" + vmNode + "/tasks/" + upid + "/status"
        pm_task_status = requests.get(apiTaskStatus, headers=self.pmAuthJson, verify=False)
        task_id_json = pm_task_status.json()
        return task_id_json["data"]

    def wait_on_task(self, vmNode, upid):
        status = self.get_task_status(vmNode, upid)
        print(status["status"] + " - " + status["type"] + ": " + status["id"])
        while status["status"] == "running":
            time.sleep(2)
            status = self.get_task_status(vmNode, upid)
        print(status["status"] + " - " + status["type"] + ": " + status["id"])
        return

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
        return node_bridges[vmNode]

    def get_virtual_machines(self, vmNode):
        apiNodeVms = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu"
        pm_node_vms = requests.get(apiNodeVms, headers=self.pmAuthJson, verify=False)
        return pm_node_vms.json()

    def get_initial_gui_data(self, vmNodes):
        self.pools = {}
        self.virtual_machines = {}
        self.snapshots = {}
        for vmNode in vmNodes["data"]:
            bridgesJson = self.get_node_network_bridges(vmNode["node"])
            self.bridges[vmNode["node"]] = bridgesJson
            vms = self.get_virtual_machines(vmNode["node"])
            for vm in vms["data"]:
                if vm["template"] == 1:
                    vm_details = {
                        "name": vm["name"],
                        "status": vm["status"],
                        "node": vmNode["node"],
                        "template": 1
                    }
                    self.virtual_machines[vm["vmid"]] = vm_details
                else:
                    vm_details = {
                        "name": vm["name"],
                        "status": vm["status"],
                        "node": vmNode["node"],
                        "template": 0,
                        "snapshots": self.get_snapshots(vmNode["node"], vm["vmid"])
                    }
                    self.virtual_machines[vm["vmid"]] = vm_details
        apiGetPools = self.pmApi + "/api2/json/pools"
        pm_get_pools = requests.get(apiGetPools, headers=self.pmAuthJson, verify=False)
        for pool in pm_get_pools.json()["data"]:
            pool_member_ids = []
            apiGetPoolVms = self.pmApi + "/api2/json/pools/" + pool["poolid"]
            pm_pool_vms = requests.get(apiGetPoolVms, headers=self.pmAuthJson, verify=False)
            pool_members = pm_pool_vms.json()["data"]["members"]
            for member in pool_members:
                pool_member_ids.append(member["vmid"])
            self.pools[pool["poolid"]] = pool_member_ids
        return

    def get_snapshots(self, vmNode, vmID):
        apiSnapshots = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot"
        pm_snapshots = requests.get(apiSnapshots, headers=self.pmAuthJson, verify=False)
        return pm_snapshots.json()["data"]

    def create_snapshot(self, vmNode, vmID, snapshotName="proxmox_manager", includeRam="0", description='Created by Python'):
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

    def revertLatestSnapshot(self, vmNode, vmID):
        snapshots = self.get_snapshots(vmNode, vmID)
        print(snapshots)
        snapTimes = []
        for snap in snapshots:
            try:
                if snap["snaptime"]:
                    snapTimes.append(snap["snaptime"])
            except:
                None
        for snap in snapshots:
            try:
                if snap["snaptime"] == max(snapTimes):
                    apiRevertSnapLatest = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot/" + snap["name"] + "/rollback"
                    pm_snapback_latest = requests.post(apiRevertSnapLatest, headers=self.pmAuthJson, verify=False)
                    return pm_snapback_latest.json()["data"]
            except:
                None
        return

    def revertEarliestSnapshot(self, vmNode, vmID):
        snapshots = self.get_snapshots(vmNode, vmID)
        print(snapshots)
        snapTimes = []
        for snap in snapshots:
            try:
                if snap["snaptime"]:
                    snapTimes.append(snap["snaptime"])
            except:
                None
        for snap in snapshots:
            try:
                if snap["snaptime"] == min(snapTimes):
                    apiRevertSnapLatest = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/snapshot/" + snap["name"] + "/rollback"
                    pm_snapback_latest = requests.post(apiRevertSnapLatest, headers=self.pmAuthJson, verify=False)
                    return pm_snapback_latest.json()["data"]
            except:
                None
        return

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
        if vmNetBridge != 'e1000,bridge=vmbr0,firewall=0,link_down=0':
            vmBridge = 'e1000,bridge=' + vmNetBridge + ',firewall=0,link_down=0'
        else:
            vmBridge = vmNetBridge

        data = {
            "node": vmNode,
            "vmid": vmID,
            vmNetId: vmBridge
        }
        print(vmBridge)
        apiSetNetBridge = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmID + "/config"
        pm_set_net_bridge = requests.post(apiSetNetBridge, headers=self.pmAuthJson, data=data, verify=False)
        return pm_set_net_bridge.json()

    def get_free_vmid(self):
        apiFreeVmid = self.pmApi + "/api2/json/cluster/nextid"
        pm_free_vmid = requests.get(apiFreeVmid, headers=self.pmAuthJson, verify=False)
        freeVmid = pm_free_vmid.json()
        return freeVmid["data"]


    def create_pool(self, vmNode, vmPoolName):
        apiCreatePool = self.pmApi + "/api2/json/pools"
        data = {
            "poolid": vmPoolName
        }
        pm_create_pool = requests.post(apiCreatePool, headers=self.pmAuthJson, data=data, verify=False)
        return pm_create_pool.json()

    def create_clone_linked(self, vmNode, vmSourceId, pool="Lab"):
        apiClone = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmSourceId + "/clone"
        newID = self.get_free_vmid()
        data = {
            "newid": newID,
            "pool": pool,
            "full": "0"
        }
        pm_create_clone_linked = requests.post(apiClone, headers=self.pmAuthJson, data=data, verify=False)
        self.wait_on_task(vmNode, pm_create_clone_linked.json()["data"])
        return newID

    def create_clone_full(self, vmNode, vmSourceId, pool="Lab", name=""):
        if name == "":
            name = self.virtual_machines[vmSourceId]["name"]
        newID = self.get_free_vmid()
        apiClone = self.pmApi + "/api2/json/nodes/" + vmNode + "/qemu/" + vmSourceId + "/clone"
        data = {
            "newid": newID,
            "pool": pool,
            "full": "1",
            "name": name
        }
        pm_create_clone_full = requests.post(apiClone, headers=self.pmAuthJson, data=data, verify=False)
        print(pm_create_clone_full.json())
        self.wait_on_task(vmNode, pm_create_clone_full.json()["data"])
        return newID

    def destroy_vm(self, vmId):
        apiDestroy = self.pmApi + "/api2/json/nodes/" + self.virtual_machines[vmId]["node"] + "/qemu/" + vmId
        pm_destroy_vm = requests.delete(apiDestroy, headers=self.pmAuthJson, verify=False)
        return pm_destroy_vm.json()

    def destroy_pool_vms(self, pool):
        for vm in self.pools[pool]:
            if self.virtual_machines[str(vm)]["template"] == 1:
                self.destroy_vm(str(vm))

    def startVM(self, vmid):
        apiStartVM = self.pmApi + "/api2/json/nodes/" + self.virtual_machines[vmid]["node"] + "/qemu/" + vmid +  "/status/start"
        pm_start_vm = requests.post(apiStartVM, headers=self.pmAuthJson, verify=False)
        return pm_start_vm.json()
