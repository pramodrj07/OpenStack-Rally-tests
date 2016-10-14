@validation.required_services(consts.Service.NEUTRON)
@validation.required_openstack(users=True)
@scenario.configure(context={"cleanup": ["neutron"]},
                    name="NeutronNetworks.create_and_delete_networks_subnets_ports")
class CreateAndDeleteNetworksSubnetsPorts(utils.NeutronScenario):

    def run(self, network_create_args=None, subnet_create_args=None,
            subnet_cidr_start=None, subnets_per_network=None,
            port_create_args=None, ports_per_network=None ):


        network = self._create_network(network_create_args or {})
        self._delete_network(network["network"])

        network = self._get_or_create_network(network_create_args)
        subnets = self._create_subnets(network, subnet_create_args, subnet_cidr_start, subnets_per_network)
        for subnet in subnets:
            self._delete_subnet(subnet)

        for i in range(ports_per_network):
            port = self._create_port(network, port_create_args)
            self._delete_port(port)
