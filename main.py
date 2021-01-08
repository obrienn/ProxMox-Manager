from connection import Connection
from config import ProxMoxConfig
import sys
import json

pmconfig = ProxMoxConfig()
pmconnection = Connection()
pmconnection.set_session(pmconfig.pmApi, pmconfig.pmAuthJson)

nodes = pmconnection.get_nodes()
node = nodes["data"][0]["node"]

#print(pmconnection.delete_snapshot(node, "900", "testymctestface2"))
#print(pmconnection.create_snapshot(node, "900", "testymctestface2"))
#print(pmconnection.get_snapshots(node, "900"))
#vm_config = pmconnection.get_vm_config(node, "900")
#print(vm_config["data"]["net0"])
#print(pmconnection.set_network_bridge(node, "900"))
#print(pmconnection.get_node_network_bridges(node))
#pmc_ccl = pmconnection.create_clone_linked(node, "920")
#pmc_ccf = pmconnection.create_clone_full(node, "920")
#pmconnection.wait_on_task(node, pmc_ccf)
#pmconnection.destroy_pool_vms("Lab")

pmconnection.get_initial_gui_data(nodes)
print(pmconnection.endpoints)
print(pmconnection.templates)
print(pmconnection.pools)
