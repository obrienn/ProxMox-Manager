

class Processing:
    templates = {}
    endpoints = {}

    def node_list_vms_and_templates(self, vmsJson, vmNode):
        """ Provide a list of endpoints and templates by node.
        @param: The JSON output as provided by pmconnection.get_virtual_machines(node).
        @param: The node used by the first parameter.
        """
        templates_ids = []
        endpoints_ids = []

        for vm in vmsJson["data"]:
            if vm["template"] is 1:
                templates_ids.append(vm["vmid"])
            else:
                endpoints_ids.append(vm["vmid"])
        self.templates[vmNode] = templates_ids
        self.endpoints[vmNode] = endpoints_ids
        return
