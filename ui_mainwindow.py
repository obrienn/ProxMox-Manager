# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProxMoxManagerWindow-v2awGmzA.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from connection import Connection
from config import ProxMoxConfig


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.pmconfig = ProxMoxConfig()

        self.pmconnection = Connection()
        self.pmconnection.set_session(self.pmconfig.pmApi, self.pmconfig.pmAuthJson)

        self.nodes = self.pmconnection.get_nodes()
        self.node = self.nodes["data"][0]["node"]

        self.pmconnection.get_initial_gui_data(self.nodes)
        print(self.pmconnection.virtual_machines)
        print(self.pmconnection.pools)

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1081, 546)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 1061, 521))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeader = QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName(u"horizontalLayoutHeader")
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(28)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setAutoFillBackground(False)
        self.labelTitle.setFrameShape(QFrame.Panel)
        self.labelTitle.setFrameShadow(QFrame.Raised)
        self.labelTitle.setLineWidth(4)
        self.labelTitle.setMidLineWidth(2)
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutHeader.addWidget(self.labelTitle)

        self.verticalLayout.addLayout(self.horizontalLayoutHeader)

        self.horizontalLayoutListviews = QHBoxLayout()
        self.horizontalLayoutListviews.setObjectName(u"horizontalLayoutListviews")
        self.verticalLayoutPoolSelect = QVBoxLayout()
        self.verticalLayoutPoolSelect.setObjectName(u"verticalLayoutPoolSelect")
        self.labelPoolSelect = QLabel(self.widget)
        self.labelPoolSelect.setObjectName(u"labelPoolSelect")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        self.labelPoolSelect.setFont(font1)
        self.labelPoolSelect.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayoutPoolSelect.addWidget(self.labelPoolSelect)

        self.listWidgetPools = QListWidget(self.widget)
        self.listWidgetPools.setObjectName(u"listWidgetPools")

        self.verticalLayoutPoolSelect.addWidget(self.listWidgetPools)

        self.horizontalLayoutListviews.addLayout(self.verticalLayoutPoolSelect)

        self.verticalLayoutVmSelect = QVBoxLayout()
        self.verticalLayoutVmSelect.setObjectName(u"verticalLayoutVmSelect")
        self.labelVmListView = QLabel(self.widget)
        self.labelVmListView.setObjectName(u"labelVmListView")
        self.labelVmListView.setFont(font1)
        self.labelVmListView.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayoutVmSelect.addWidget(self.labelVmListView)

        self.listWidgetVms = QListWidget(self.widget)
        self.listWidgetVms.setObjectName(u"listWidgetVms")

        self.verticalLayoutVmSelect.addWidget(self.listWidgetVms)

        self.horizontalLayoutListviews.addLayout(self.verticalLayoutVmSelect)

        self.verticalLayout.addLayout(self.horizontalLayoutListviews)

        self.labelPoolManagement = QLabel(self.widget)
        self.labelPoolManagement.setObjectName(u"labelPoolManagement")
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(20)
        font2.setBold(True)
        self.labelPoolManagement.setFont(font2)
        self.labelPoolManagement.setFrameShape(QFrame.Panel)
        self.labelPoolManagement.setFrameShadow(QFrame.Raised)
        self.labelPoolManagement.setLineWidth(4)
        self.labelPoolManagement.setMidLineWidth(2)
        self.labelPoolManagement.setScaledContents(False)
        self.labelPoolManagement.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelPoolManagement)

        self.horizontalLayoutActions = QHBoxLayout()
        self.horizontalLayoutActions.setObjectName(u"horizontalLayoutActions")
        self.verticalLayoutCloning = QVBoxLayout()
        self.verticalLayoutCloning.setObjectName(u"verticalLayoutCloning")
        self.labelCloning = QLabel(self.widget)
        self.labelCloning.setObjectName(u"labelCloning")
        self.labelCloning.setFont(font1)
        self.labelCloning.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCloning.addWidget(self.labelCloning)

        self.verticalSpacerCloning = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutCloning.addItem(self.verticalSpacerCloning)

        self.checkBoxTemplatesRestriction = QCheckBox(self.widget)
        self.checkBoxTemplatesRestriction.setObjectName(u"checkBoxTemplatesRestriction")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.checkBoxTemplatesRestriction.setFont(font3)
        self.checkBoxTemplatesRestriction.setChecked(True)

        self.verticalLayoutCloning.addWidget(self.checkBoxTemplatesRestriction)

        self.labelTemplateNote = QLabel(self.widget)
        self.labelTemplateNote.setObjectName(u"labelTemplateNote")
        self.labelTemplateNote.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCloning.addWidget(self.labelTemplateNote)

        self.checkBoxLinkedClones = QCheckBox(self.widget)
        self.checkBoxLinkedClones.setObjectName(u"checkBoxLinkedClones")
        self.checkBoxLinkedClones.setFont(font3)
        self.checkBoxLinkedClones.setChecked(True)

        self.verticalLayoutCloning.addWidget(self.checkBoxLinkedClones)

        self.horizontalLayoutSelectNode = QHBoxLayout()
        self.horizontalLayoutSelectNode.setObjectName(u"horizontalLayoutSelectNode")
        self.labelSelectNode = QLabel(self.widget)
        self.labelSelectNode.setObjectName(u"labelSelectNode")
        self.labelSelectNode.setFont(font3)

        self.horizontalLayoutSelectNode.addWidget(self.labelSelectNode)

        self.comboBoxSelectNode = QComboBox(self.widget)
        self.comboBoxSelectNode.setObjectName(u"comboBoxSelectNode")

        self.horizontalLayoutSelectNode.addWidget(self.comboBoxSelectNode)

        self.verticalLayoutCloning.addLayout(self.horizontalLayoutSelectNode)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelConfirmSourcePool = QLabel(self.widget)
        self.labelConfirmSourcePool.setObjectName(u"labelConfirmSourcePool")
        self.labelConfirmSourcePool.setFont(font3)

        self.horizontalLayout.addWidget(self.labelConfirmSourcePool)

        self.labelSourcePool = QLabel(self.widget)
        self.labelSourcePool.setObjectName(u"labelSourcePool")

        self.horizontalLayout.addWidget(self.labelSourcePool)

        self.verticalLayoutCloning.addLayout(self.horizontalLayout)

        self.horizontalLayoutSelectTargetPool = QHBoxLayout()
        self.horizontalLayoutSelectTargetPool.setObjectName(u"horizontalLayoutSelectTargetPool")
        self.horizontalLayoutSelectTargetPool.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.labelTargetPool = QLabel(self.widget)
        self.labelTargetPool.setObjectName(u"labelTargetPool")
        self.labelTargetPool.setFont(font3)

        self.horizontalLayoutSelectTargetPool.addWidget(self.labelTargetPool)

        self.comboBoxTargetPool = QComboBox(self.widget)
        self.comboBoxTargetPool.setObjectName(u"comboBoxTargetPool")
        self.comboBoxTargetPool.setMinimumSize(QSize(0, 0))

        self.horizontalLayoutSelectTargetPool.addWidget(self.comboBoxTargetPool)

        self.verticalLayoutCloning.addLayout(self.horizontalLayoutSelectTargetPool)

        self.pushButtonClone = QPushButton(self.widget)
        self.pushButtonClone.setObjectName(u"pushButtonClone")

        self.verticalLayoutCloning.addWidget(self.pushButtonClone)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutCloning)

        self.verticalLayoutSnapshots = QVBoxLayout()
        self.verticalLayoutSnapshots.setObjectName(u"verticalLayoutSnapshots")
        self.labelSnapshots = QLabel(self.widget)
        self.labelSnapshots.setObjectName(u"labelSnapshots")
        self.labelSnapshots.setFont(font1)
        self.labelSnapshots.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshots)

        self.labelSnapshotNote1 = QLabel(self.widget)
        self.labelSnapshotNote1.setObjectName(u"labelSnapshotNote1")
        self.labelSnapshotNote1.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshotNote1)

        self.labelSnapshotNote2 = QLabel(self.widget)
        self.labelSnapshotNote2.setObjectName(u"labelSnapshotNote2")
        self.labelSnapshotNote2.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshotNote2)

        self.verticalSpacerSnapshot = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutSnapshots.addItem(self.verticalSpacerSnapshot)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelSnapshotNode = QLabel(self.widget)
        self.labelSnapshotNode.setObjectName(u"labelSnapshotNode")
        self.labelSnapshotNode.setFont(font3)

        self.horizontalLayout_6.addWidget(self.labelSnapshotNode)

        self.comboBoxSnapshotNode = QComboBox(self.widget)
        self.comboBoxSnapshotNode.setObjectName(u"comboBoxSnapshotNode")

        self.horizontalLayout_6.addWidget(self.comboBoxSnapshotNode)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSelectSnapshotPool = QLabel(self.widget)
        self.labelSelectSnapshotPool.setObjectName(u"labelSelectSnapshotPool")
        self.labelSelectSnapshotPool.setFont(font3)

        self.horizontalLayout_2.addWidget(self.labelSelectSnapshotPool)

        self.comboBoxSnapshotPool = QComboBox(self.widget)
        self.comboBoxSnapshotPool.setObjectName(u"comboBoxSnapshotPool")

        self.horizontalLayout_2.addWidget(self.comboBoxSnapshotPool)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonRevertToOldest = QPushButton(self.widget)
        self.pushButtonRevertToOldest.setObjectName(u"pushButtonRevertToOldest")

        self.horizontalLayout_3.addWidget(self.pushButtonRevertToOldest)

        self.pushButtonRevertToLatest = QPushButton(self.widget)
        self.pushButtonRevertToLatest.setObjectName(u"pushButtonRevertToLatest")

        self.horizontalLayout_3.addWidget(self.pushButtonRevertToLatest)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelNewSnapshotName = QLabel(self.widget)
        self.labelNewSnapshotName.setObjectName(u"labelNewSnapshotName")

        self.horizontalLayout_4.addWidget(self.labelNewSnapshotName)

        self.lineEditSnapshotName = QLineEdit(self.widget)
        self.lineEditSnapshotName.setObjectName(u"lineEditSnapshotName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditSnapshotName.sizePolicy().hasHeightForWidth())
        self.lineEditSnapshotName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lineEditSnapshotName)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_4)

        self.pushButtonCreateNewSnapshots = QPushButton(self.widget)
        self.pushButtonCreateNewSnapshots.setObjectName(u"pushButtonCreateNewSnapshots")

        self.verticalLayoutSnapshots.addWidget(self.pushButtonCreateNewSnapshots)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutSnapshots)

        self.verticalLayoutDeleting = QVBoxLayout()
        self.verticalLayoutDeleting.setObjectName(u"verticalLayoutDeleting")
        self.labelDeleting = QLabel(self.widget)
        self.labelDeleting.setObjectName(u"labelDeleting")
        self.labelDeleting.setFont(font1)
        self.labelDeleting.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeleting)

        self.labelDeletingNote1 = QLabel(self.widget)
        self.labelDeletingNote1.setObjectName(u"labelDeletingNote1")
        self.labelDeletingNote1.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeletingNote1)

        self.labelDeletingNote2 = QLabel(self.widget)
        self.labelDeletingNote2.setObjectName(u"labelDeletingNote2")
        self.labelDeletingNote2.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeletingNote2)

        self.verticalSpacerDelete = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutDeleting.addItem(self.verticalSpacerDelete)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelDeleteSelectPool = QLabel(self.widget)
        self.labelDeleteSelectPool.setObjectName(u"labelDeleteSelectPool")
        self.labelDeleteSelectPool.setFont(font3)

        self.horizontalLayout_5.addWidget(self.labelDeleteSelectPool)

        self.comboBoxDeleteSelectPool = QComboBox(self.widget)
        self.comboBoxDeleteSelectPool.setObjectName(u"comboBoxDeleteSelectPool")

        self.horizontalLayout_5.addWidget(self.comboBoxDeleteSelectPool)

        self.verticalLayoutDeleting.addLayout(self.horizontalLayout_5)

        self.pushButtonDelete = QPushButton(self.widget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.verticalLayoutDeleting.addWidget(self.pushButtonDelete)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutDeleting)

        self.verticalLayout.addLayout(self.horizontalLayoutActions)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.listWidgetPools.itemSelectionChanged.connect(self.updateVmsListFromPool)
        self.checkBoxTemplatesRestriction.toggled.connect(self.updateVmsListFromPool)
        self.pushButtonClone.clicked.connect(self.clonePoolToPool)
        self.pushButtonDelete.clicked.connect(self.clearResourcePool)
        self.pushButtonCreateNewSnapshots.clicked.connect(self.createSnapshots)
        self.pushButtonRevertToLatest.clicked.connect(self.revertLatestSnapshot)
        self.pushButtonRevertToOldest.clicked.connect(self.revertEarliestSnapshot)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"ProxMox Lab Manager", None))
        self.labelPoolSelect.setText(QCoreApplication.translate("MainWindow", u"Select a Resource Pool Source", None))
        self.labelVmListView.setText(QCoreApplication.translate("MainWindow", u"Select a VM if Applicable", None))
        self.labelPoolManagement.setText(QCoreApplication.translate("MainWindow", u"Pool Management", None))
        self.labelCloning.setText(QCoreApplication.translate("MainWindow", u"Cloning", None))
        self.checkBoxTemplatesRestriction.setText(QCoreApplication.translate("MainWindow", u"Only Clone Resource Pool Templates", None))
        self.labelTemplateNote.setText(QCoreApplication.translate("MainWindow", u"Note: Restricts view scope above.", None))
        self.checkBoxLinkedClones.setText(QCoreApplication.translate("MainWindow", u"Create Linked Clones", None))
        self.labelSelectNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.comboBoxSelectNode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.labelConfirmSourcePool.setText(QCoreApplication.translate("MainWindow", u"Confirm Source Pool:", None))
        self.labelSourcePool.setText(QCoreApplication.translate("MainWindow", u"Select a Resource Pool Source", None))
        self.labelTargetPool.setText(QCoreApplication.translate("MainWindow", u"Select Target Pool", None))
        self.comboBoxTargetPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonClone.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.labelSnapshots.setText(QCoreApplication.translate("MainWindow", u"Snapshot Management", None))
        self.labelSnapshotNote1.setText(QCoreApplication.translate("MainWindow", u"Note: Not applicable to templates", None))
        self.labelSnapshotNote2.setText(QCoreApplication.translate("MainWindow", u"Note: All target VM's will be shutdown first.", None))
        self.labelSnapshotNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.labelSelectSnapshotPool.setText(QCoreApplication.translate("MainWindow", u"Select Pool", None))
        self.comboBoxSnapshotPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonRevertToOldest.setText(QCoreApplication.translate("MainWindow", u"Revert to Oldest", None))
        self.pushButtonRevertToLatest.setText(QCoreApplication.translate("MainWindow", u"Revert to Latest", None))
        self.labelNewSnapshotName.setText(QCoreApplication.translate("MainWindow", u"New snapshot base name:", None))
        self.lineEditSnapshotName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonCreateNewSnapshots.setText(QCoreApplication.translate("MainWindow", u"Create New Snapshots", None))
        self.labelDeleting.setText(QCoreApplication.translate("MainWindow", u"Resource Removal", None))
        self.labelDeletingNote1.setText(QCoreApplication.translate("MainWindow", u"Note: Only removes non-template virtual machines.", None))
        self.labelDeletingNote2.setText(QCoreApplication.translate("MainWindow", u"Note: Will not remove Protected virtual machines.", None))
        self.labelDeleteSelectPool.setText(QCoreApplication.translate("MainWindow", u"Select Pool", None))
        self.comboBoxDeleteSelectPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonDelete.setText(QCoreApplication.translate("MainWindow", u"Remove Non-Protected Non-Template VM's", None))

        self.updateNodesDropdown()
        self.updatePoolsList()
        self.updateVmsListFromPool()

        # retranslateUi

    def updateNodesDropdown(self):
        print("LOG: Updating Nodes List")
        print(self.nodes)
        for node in self.nodes["data"]:
            self.comboBoxSelectNode.addItem(node["node"])
            self.comboBoxSnapshotNode.addItem(node["node"])
        self.comboBoxSelectNode.setCurrentIndex(0)
        self.comboBoxSelectNode.setCurrentIndex(0)

    def updateVmsListFromPool(self):
        print("LOG: Updating VM's List")
        self.listWidgetVms.clear()
        try:
            selectedPool = self.listWidgetPools.selectedItems()[0].text()
        except:
            return

        if self.checkBoxTemplatesRestriction.isChecked():
            for vmid in self.pmconnection.pools[selectedPool]:
                if self.pmconnection.virtual_machines[str(vmid)]["template"] == 1:
                    self.listWidgetVms.addItem(
                        "[template]" + self.pmconnection.virtual_machines[str(vmid)]["name"])
        else:
            for vmid in self.pmconnection.pools[selectedPool]:
                if self.pmconnection.virtual_machines[str(vmid)]["template"] == 1:
                    self.listWidgetVms.addItem(
                        "[template]" + self.pmconnection.virtual_machines[str(vmid)]["name"])
                else:
                    self.listWidgetVms.addItem(self.pmconnection.virtual_machines[str(vmid)]["name"])
        self.listWidgetVms.setSortingEnabled(1)
        self.listWidgetVms.update()
        return

    def updatePoolsList(self):
        print("LOG: Updating Pools Lists")
        self.listWidgetPools.clear()
        self.comboBoxDeleteSelectPool.clear()
        self.comboBoxTargetPool.clear()
        self.comboBoxSnapshotPool.clear()

        for pool in self.pmconnection.pools:
            self.listWidgetPools.addItem(pool)
            self.comboBoxDeleteSelectPool.addItem(pool)
            self.comboBoxTargetPool.addItem(pool)
            self.comboBoxSnapshotPool.addItem(pool)

        self.listWidgetPools.setSortingEnabled(1)

        self.listWidgetPools.update()
        self.comboBoxDeleteSelectPool.update()
        self.comboBoxTargetPool.update()
        self.comboBoxSnapshotPool.update()
        return

    def clonePoolToPool(self):
        self.pushButtonClone.setDisabled(1)
        sourcePool = self.listWidgetPools.selectedItems()[0].text()
        targetPool = self.comboBoxTargetPool.currentText()
        for vmid in self.pmconnection.pools[sourcePool]:
            if self.pmconnection.virtual_machines[str(vmid)]["template"] == 1:
                print("LOG: Cloning " + self.pmconnection.virtual_machines[str(vmid)]["name"])
                self.pmconnection.create_clone_linked(self.comboBoxSelectNode.currentText(), str(vmid), targetPool)
        self.pmconnection.get_initial_gui_data(self.nodes)
        self.pushButtonClone.setDisabled(0)
        return

    def clearResourcePool(self):
        self.pushButtonDelete.setDisabled(1)
        targetPool = self.comboBoxDeleteSelectPool.currentText()
        print("LOG: Clearing out resource pool " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Deleting " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.destroy_vm(str(vmid))
        self.pushButtonDelete.setDisabled(0)
        return

    def createSnapshots(self):
        self.pushButtonCreateNewSnapshots.setDisabled(1)
        targetPool = self.comboBoxSnapshotPool.currentText()
        print("LOG: Creating snapshots in " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Creating snapshot for " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.create_snapshot(self.comboBoxSnapshotNode.currentText(),str(vmid),self.lineEditSnapshotName.text())
        self.pushButtonCreateNewSnapshots.setDisabled(0)
        return

    def revertLatestSnapshot(self):
        self.pushButtonRevertToLatest.setDisabled(1)
        targetPool = self.comboBoxSnapshotPool.currentText()
        print("LOG: Reverting to latest snapshots for " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Reverting snapshot to latest for " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.revertLatestSnapshot(self.comboBoxSnapshotNode.currentText(),str(vmid))
        self.pushButtonRevertToLatest.setDisabled(0)
        return

    def revertEarliestSnapshot(self):
        self.pushButtonRevertToOldest.setDisabled(1)
        targetPool = self.comboBoxSnapshotPool.currentText()
        print("LOG: Reverting to latest snapshots for " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Reverting snapshot to latest for " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.revertEarliestSnapshot(self.comboBoxSnapshotNode.currentText(),str(vmid))
        self.pushButtonRevertToLatest.setDisabled(0)
        return

