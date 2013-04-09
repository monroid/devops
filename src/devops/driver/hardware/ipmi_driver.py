# vim: ts=4 sw=4 expandtab
from time import sleep
import libvirt
from devops.helpers.retry import retry
import ipaddr


class IpmiDriver(object):
    def __init__(self, ip, user='root', password='r00tme', interface='lanplus'):
        #TODO: write connection handler for IPMI
        pass
#        return IpmiConnection
        

    @retry()
    def node_active(self, node):
        """
        :type node: Node
        :rtype : Boolean
        """
        return self.conn.isActive()

    @retry()
    def node_destroy(self, node):
        """
        :type node: Node
        :rtype : None
        """
        self.conn.poweroff()

    @retry()
    def node_undefine(self, node):
        """
        :type node: Node
        :rtype : None
        """
        #"TODO: may be, we should cleanup node manually including mbr and other stuff"
        self.conn.poweroff()

    @retry()
    def node_create(self, node):
        """
        :type node: Node
        :rtype : None
        """
        self.conn.poweron()

    @retry()
    def node_reset(self, node):
        """
        :type node: Node
        :rtype : None
        """
        self.conn.reset()

    @retry()
    def node_reboot(self, node):
        """
        :type node: Node
        :rtype : None
        """
        self.conn.reboot()

    @retry()
    def node_shutdown(self, node):
        """
        :type node: Node
        :rtype : None
        """
        self.conn.shutdown()
