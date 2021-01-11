
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec_()

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


