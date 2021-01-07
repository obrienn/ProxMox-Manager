from connection import Connection
from config import ProxMoxConfig
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

