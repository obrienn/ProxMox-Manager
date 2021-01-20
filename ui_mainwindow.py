# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProxMoxManagerWindow-v2jsSbcH.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os

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

        self.labTemplates = []
        self.getLabTemplates()

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1081, 986)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1081, 986))
        MainWindow.setMaximumSize(QSize(1081, 986))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1061, 971))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutHeader = QHBoxLayout()
        self.horizontalLayoutHeader.setObjectName(u"horizontalLayoutHeader")
        self.labelTitle = QLabel(self.layoutWidget)
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
        self.labelPoolSelect = QLabel(self.layoutWidget)
        self.labelPoolSelect.setObjectName(u"labelPoolSelect")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        self.labelPoolSelect.setFont(font1)
        self.labelPoolSelect.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayoutPoolSelect.addWidget(self.labelPoolSelect)

        self.listWidgetPools = QListWidget(self.layoutWidget)
        self.listWidgetPools.setObjectName(u"listWidgetPools")

        self.verticalLayoutPoolSelect.addWidget(self.listWidgetPools)

        self.horizontalLayoutListviews.addLayout(self.verticalLayoutPoolSelect)

        self.verticalLayoutVmSelect = QVBoxLayout()
        self.verticalLayoutVmSelect.setObjectName(u"verticalLayoutVmSelect")
        self.labelVmListView = QLabel(self.layoutWidget)
        self.labelVmListView.setObjectName(u"labelVmListView")
        self.labelVmListView.setFont(font1)
        self.labelVmListView.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.verticalLayoutVmSelect.addWidget(self.labelVmListView)

        self.listWidgetVms = QListWidget(self.layoutWidget)
        self.listWidgetVms.setObjectName(u"listWidgetVms")

        self.verticalLayoutVmSelect.addWidget(self.listWidgetVms)

        self.horizontalLayoutListviews.addLayout(self.verticalLayoutVmSelect)

        self.verticalLayout.addLayout(self.horizontalLayoutListviews)

        self.checkBoxTemplatesRestriction = QCheckBox(self.layoutWidget)
        self.checkBoxTemplatesRestriction.setObjectName(u"checkBoxTemplatesRestriction")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.checkBoxTemplatesRestriction.setFont(font2)
        self.checkBoxTemplatesRestriction.setChecked(True)

        self.verticalLayout.addWidget(self.checkBoxTemplatesRestriction)

        self.labelPoolManagement = QLabel(self.layoutWidget)
        self.labelPoolManagement.setObjectName(u"labelPoolManagement")
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(20)
        font3.setBold(True)
        self.labelPoolManagement.setFont(font3)
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
        self.labelCloning = QLabel(self.layoutWidget)
        self.labelCloning.setObjectName(u"labelCloning")
        self.labelCloning.setFont(font1)
        self.labelCloning.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCloning.addWidget(self.labelCloning)

        self.labelTemplateNote = QLabel(self.layoutWidget)
        self.labelTemplateNote.setObjectName(u"labelTemplateNote")
        self.labelTemplateNote.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCloning.addWidget(self.labelTemplateNote)

        self.verticalSpacerCloning = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutCloning.addItem(self.verticalSpacerCloning)

        self.horizontalLayoutSelectNode = QHBoxLayout()
        self.horizontalLayoutSelectNode.setObjectName(u"horizontalLayoutSelectNode")
        self.labelSelectNode = QLabel(self.layoutWidget)
        self.labelSelectNode.setObjectName(u"labelSelectNode")
        self.labelSelectNode.setFont(font2)

        self.horizontalLayoutSelectNode.addWidget(self.labelSelectNode)

        self.comboBoxSelectNode = QComboBox(self.layoutWidget)
        self.comboBoxSelectNode.setObjectName(u"comboBoxSelectNode")

        self.horizontalLayoutSelectNode.addWidget(self.comboBoxSelectNode)

        self.verticalLayoutCloning.addLayout(self.horizontalLayoutSelectNode)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelConfirmSourcePool = QLabel(self.layoutWidget)
        self.labelConfirmSourcePool.setObjectName(u"labelConfirmSourcePool")
        self.labelConfirmSourcePool.setFont(font2)

        self.horizontalLayout.addWidget(self.labelConfirmSourcePool)

        self.labelSourcePool = QLabel(self.layoutWidget)
        self.labelSourcePool.setObjectName(u"labelSourcePool")

        self.horizontalLayout.addWidget(self.labelSourcePool)

        self.verticalLayoutCloning.addLayout(self.horizontalLayout)

        self.horizontalLayoutSelectTargetPool = QHBoxLayout()
        self.horizontalLayoutSelectTargetPool.setObjectName(u"horizontalLayoutSelectTargetPool")
        self.horizontalLayoutSelectTargetPool.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.labelTargetPool = QLabel(self.layoutWidget)
        self.labelTargetPool.setObjectName(u"labelTargetPool")
        self.labelTargetPool.setFont(font2)

        self.horizontalLayoutSelectTargetPool.addWidget(self.labelTargetPool)

        self.comboBoxTargetPool = QComboBox(self.layoutWidget)
        self.comboBoxTargetPool.setObjectName(u"comboBoxTargetPool")
        self.comboBoxTargetPool.setMinimumSize(QSize(0, 0))

        self.horizontalLayoutSelectTargetPool.addWidget(self.comboBoxTargetPool)

        self.verticalLayoutCloning.addLayout(self.horizontalLayoutSelectTargetPool)

        self.horizontalLayoutCloneNetwork = QHBoxLayout()
        self.horizontalLayoutCloneNetwork.setObjectName(u"horizontalLayoutCloneNetwork")
        self.labelPoolCloneNetwork = QLabel(self.layoutWidget)
        self.labelPoolCloneNetwork.setObjectName(u"labelPoolCloneNetwork")
        self.labelPoolCloneNetwork.setFont(font2)

        self.horizontalLayoutCloneNetwork.addWidget(self.labelPoolCloneNetwork)

        self.comboBoxCloneNetwork = QComboBox(self.layoutWidget)
        self.comboBoxCloneNetwork.setObjectName(u"comboBoxCloneNetwork")

        self.horizontalLayoutCloneNetwork.addWidget(self.comboBoxCloneNetwork)

        self.verticalLayoutCloning.addLayout(self.horizontalLayoutCloneNetwork)

        self.checkBoxStartClonedPoolVms = QCheckBox(self.layoutWidget)
        self.checkBoxStartClonedPoolVms.setObjectName(u"checkBoxStartClonedPoolVms")
        self.checkBoxStartClonedPoolVms.setFont(font2)
        self.checkBoxStartClonedPoolVms.setChecked(True)

        self.verticalLayoutCloning.addWidget(self.checkBoxStartClonedPoolVms)

        self.pushButtonClone = QPushButton(self.layoutWidget)
        self.pushButtonClone.setObjectName(u"pushButtonClone")

        self.verticalLayoutCloning.addWidget(self.pushButtonClone)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutCloning)

        self.verticalLayoutSnapshots = QVBoxLayout()
        self.verticalLayoutSnapshots.setObjectName(u"verticalLayoutSnapshots")
        self.labelSnapshots = QLabel(self.layoutWidget)
        self.labelSnapshots.setObjectName(u"labelSnapshots")
        self.labelSnapshots.setFont(font1)
        self.labelSnapshots.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshots)

        self.labelSnapshotNote1 = QLabel(self.layoutWidget)
        self.labelSnapshotNote1.setObjectName(u"labelSnapshotNote1")
        self.labelSnapshotNote1.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshotNote1)

        self.labelSnapshotNote2 = QLabel(self.layoutWidget)
        self.labelSnapshotNote2.setObjectName(u"labelSnapshotNote2")
        self.labelSnapshotNote2.setAlignment(Qt.AlignCenter)

        self.verticalLayoutSnapshots.addWidget(self.labelSnapshotNote2)

        self.verticalSpacerSnapshot = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutSnapshots.addItem(self.verticalSpacerSnapshot)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.labelSnapshotNode = QLabel(self.layoutWidget)
        self.labelSnapshotNode.setObjectName(u"labelSnapshotNode")
        self.labelSnapshotNode.setFont(font2)

        self.horizontalLayout_6.addWidget(self.labelSnapshotNode)

        self.comboBoxSnapshotNode = QComboBox(self.layoutWidget)
        self.comboBoxSnapshotNode.setObjectName(u"comboBoxSnapshotNode")

        self.horizontalLayout_6.addWidget(self.comboBoxSnapshotNode)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelSelectSnapshotPool = QLabel(self.layoutWidget)
        self.labelSelectSnapshotPool.setObjectName(u"labelSelectSnapshotPool")
        self.labelSelectSnapshotPool.setFont(font2)

        self.horizontalLayout_2.addWidget(self.labelSelectSnapshotPool)

        self.comboBoxSnapshotPool = QComboBox(self.layoutWidget)
        self.comboBoxSnapshotPool.setObjectName(u"comboBoxSnapshotPool")

        self.horizontalLayout_2.addWidget(self.comboBoxSnapshotPool)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonRevertToOldest = QPushButton(self.layoutWidget)
        self.pushButtonRevertToOldest.setObjectName(u"pushButtonRevertToOldest")

        self.horizontalLayout_3.addWidget(self.pushButtonRevertToOldest)

        self.pushButtonRevertToLatest = QPushButton(self.layoutWidget)
        self.pushButtonRevertToLatest.setObjectName(u"pushButtonRevertToLatest")

        self.horizontalLayout_3.addWidget(self.pushButtonRevertToLatest)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelNewSnapshotName = QLabel(self.layoutWidget)
        self.labelNewSnapshotName.setObjectName(u"labelNewSnapshotName")

        self.horizontalLayout_4.addWidget(self.labelNewSnapshotName)

        self.lineEditSnapshotName = QLineEdit(self.layoutWidget)
        self.lineEditSnapshotName.setObjectName(u"lineEditSnapshotName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditSnapshotName.sizePolicy().hasHeightForWidth())
        self.lineEditSnapshotName.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.lineEditSnapshotName)

        self.verticalLayoutSnapshots.addLayout(self.horizontalLayout_4)

        self.pushButtonCreateNewSnapshots = QPushButton(self.layoutWidget)
        self.pushButtonCreateNewSnapshots.setObjectName(u"pushButtonCreateNewSnapshots")

        self.verticalLayoutSnapshots.addWidget(self.pushButtonCreateNewSnapshots)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutSnapshots)

        self.verticalLayoutDeleting = QVBoxLayout()
        self.verticalLayoutDeleting.setObjectName(u"verticalLayoutDeleting")
        self.labelDeleting = QLabel(self.layoutWidget)
        self.labelDeleting.setObjectName(u"labelDeleting")
        self.labelDeleting.setFont(font1)
        self.labelDeleting.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeleting)

        self.labelDeletingNote1 = QLabel(self.layoutWidget)
        self.labelDeletingNote1.setObjectName(u"labelDeletingNote1")
        self.labelDeletingNote1.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeletingNote1)

        self.labelDeletingNote2 = QLabel(self.layoutWidget)
        self.labelDeletingNote2.setObjectName(u"labelDeletingNote2")
        self.labelDeletingNote2.setAlignment(Qt.AlignCenter)

        self.verticalLayoutDeleting.addWidget(self.labelDeletingNote2)

        self.verticalSpacerDelete = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutDeleting.addItem(self.verticalSpacerDelete)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.labelDeleteSelectPool = QLabel(self.layoutWidget)
        self.labelDeleteSelectPool.setObjectName(u"labelDeleteSelectPool")
        self.labelDeleteSelectPool.setFont(font2)

        self.horizontalLayout_5.addWidget(self.labelDeleteSelectPool)

        self.comboBoxDeleteSelectPool = QComboBox(self.layoutWidget)
        self.comboBoxDeleteSelectPool.setObjectName(u"comboBoxDeleteSelectPool")

        self.horizontalLayout_5.addWidget(self.comboBoxDeleteSelectPool)

        self.verticalLayoutDeleting.addLayout(self.horizontalLayout_5)

        self.pushButtonDelete = QPushButton(self.layoutWidget)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")

        self.verticalLayoutDeleting.addWidget(self.pushButtonDelete)

        self.horizontalLayoutActions.addLayout(self.verticalLayoutDeleting)

        self.verticalLayout.addLayout(self.horizontalLayoutActions)

        self.labelAdditionalTools = QLabel(self.layoutWidget)
        self.labelAdditionalTools.setObjectName(u"labelAdditionalTools")
        self.labelAdditionalTools.setFont(font3)
        self.labelAdditionalTools.setFrameShape(QFrame.Panel)
        self.labelAdditionalTools.setFrameShadow(QFrame.Raised)
        self.labelAdditionalTools.setLineWidth(4)
        self.labelAdditionalTools.setMidLineWidth(2)
        self.labelAdditionalTools.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelAdditionalTools)

        self.horizontalLayoutAdditionalTools = QHBoxLayout()
        self.horizontalLayoutAdditionalTools.setObjectName(u"horizontalLayoutAdditionalTools")
        self.verticalLayoutCloneVM = QVBoxLayout()
        self.verticalLayoutCloneVM.setObjectName(u"verticalLayoutCloneVM")
        self.labelCloneIndividualVM = QLabel(self.layoutWidget)
        self.labelCloneIndividualVM.setObjectName(u"labelCloneIndividualVM")
        self.labelCloneIndividualVM.setFont(font1)
        self.labelCloneIndividualVM.setAlignment(Qt.AlignCenter)

        self.verticalLayoutCloneVM.addWidget(self.labelCloneIndividualVM)

        self.horizontalLayoutVMSelectNode = QHBoxLayout()
        self.horizontalLayoutVMSelectNode.setObjectName(u"horizontalLayoutVMSelectNode")
        self.labelVMNode = QLabel(self.layoutWidget)
        self.labelVMNode.setObjectName(u"labelVMNode")
        self.labelVMNode.setFont(font2)

        self.horizontalLayoutVMSelectNode.addWidget(self.labelVMNode)

        self.comboBoxVMNode = QComboBox(self.layoutWidget)
        self.comboBoxVMNode.setObjectName(u"comboBoxVMNode")

        self.horizontalLayoutVMSelectNode.addWidget(self.comboBoxVMNode)

        self.verticalLayoutCloneVM.addLayout(self.horizontalLayoutVMSelectNode)

        self.horizontalLayoutVMConfirmPool = QHBoxLayout()
        self.horizontalLayoutVMConfirmPool.setObjectName(u"horizontalLayoutVMConfirmPool")
        self.labelVMConfirmSourcePool = QLabel(self.layoutWidget)
        self.labelVMConfirmSourcePool.setObjectName(u"labelVMConfirmSourcePool")
        self.labelVMConfirmSourcePool.setFont(font2)

        self.horizontalLayoutVMConfirmPool.addWidget(self.labelVMConfirmSourcePool)

        self.labelVMSelectedSourcePool = QLabel(self.layoutWidget)
        self.labelVMSelectedSourcePool.setObjectName(u"labelVMSelectedSourcePool")

        self.horizontalLayoutVMConfirmPool.addWidget(self.labelVMSelectedSourcePool)

        self.verticalLayoutCloneVM.addLayout(self.horizontalLayoutVMConfirmPool)

        self.horizontalLayoutVMConfirmVM = QHBoxLayout()
        self.horizontalLayoutVMConfirmVM.setObjectName(u"horizontalLayoutVMConfirmVM")
        self.labelVMConfirmVM = QLabel(self.layoutWidget)
        self.labelVMConfirmVM.setObjectName(u"labelVMConfirmVM")
        self.labelVMConfirmVM.setFont(font2)

        self.horizontalLayoutVMConfirmVM.addWidget(self.labelVMConfirmVM)

        self.labelVMSelectedVM = QLabel(self.layoutWidget)
        self.labelVMSelectedVM.setObjectName(u"labelVMSelectedVM")

        self.horizontalLayoutVMConfirmVM.addWidget(self.labelVMSelectedVM)

        self.verticalLayoutCloneVM.addLayout(self.horizontalLayoutVMConfirmVM)

        self.horizontalLayoutVMTargetPool = QHBoxLayout()
        self.horizontalLayoutVMTargetPool.setObjectName(u"horizontalLayoutVMTargetPool")
        self.labelVMSelectTargetPool = QLabel(self.layoutWidget)
        self.labelVMSelectTargetPool.setObjectName(u"labelVMSelectTargetPool")
        self.labelVMSelectTargetPool.setFont(font2)

        self.horizontalLayoutVMTargetPool.addWidget(self.labelVMSelectTargetPool)

        self.comboBoxVMTargetPool = QComboBox(self.layoutWidget)
        self.comboBoxVMTargetPool.setObjectName(u"comboBoxVMTargetPool")

        self.horizontalLayoutVMTargetPool.addWidget(self.comboBoxVMTargetPool)

        self.verticalLayoutCloneVM.addLayout(self.horizontalLayoutVMTargetPool)

        self.horizontalLayoutVMName = QHBoxLayout()
        self.horizontalLayoutVMName.setObjectName(u"horizontalLayoutVMName")
        self.labelNewVMName = QLabel(self.layoutWidget)
        self.labelNewVMName.setObjectName(u"labelNewVMName")
        self.labelNewVMName.setFont(font2)

        self.horizontalLayoutVMName.addWidget(self.labelNewVMName)

        self.lineEditVMName = QLineEdit(self.layoutWidget)
        self.lineEditVMName.setObjectName(u"lineEditVMName")
        sizePolicy1.setHeightForWidth(self.lineEditVMName.sizePolicy().hasHeightForWidth())
        self.lineEditVMName.setSizePolicy(sizePolicy1)

        self.horizontalLayoutVMName.addWidget(self.lineEditVMName)

        self.verticalLayoutCloneVM.addLayout(self.horizontalLayoutVMName)

        self.pushButtonCloneVM = QPushButton(self.layoutWidget)
        self.pushButtonCloneVM.setObjectName(u"pushButtonCloneVM")

        self.verticalLayoutCloneVM.addWidget(self.pushButtonCloneVM)

        self.horizontalLayoutAdditionalTools.addLayout(self.verticalLayoutCloneVM)

        self.verticalLayoutLabs = QVBoxLayout()
        self.verticalLayoutLabs.setObjectName(u"verticalLayoutLabs")
        self.labelLabs = QLabel(self.layoutWidget)
        self.labelLabs.setObjectName(u"labelLabs")
        self.labelLabs.setFont(font1)

        self.verticalLayoutLabs.addWidget(self.labelLabs)

        self.horizontalLayoutLabsNode = QHBoxLayout()
        self.horizontalLayoutLabsNode.setObjectName(u"horizontalLayoutLabsNode")
        self.labelLabNode = QLabel(self.layoutWidget)
        self.labelLabNode.setObjectName(u"labelLabNode")
        self.labelLabNode.setFont(font2)

        self.horizontalLayoutLabsNode.addWidget(self.labelLabNode)

        self.comboBoxLabNode = QComboBox(self.layoutWidget)
        self.comboBoxLabNode.setObjectName(u"comboBoxLabNode")

        self.horizontalLayoutLabsNode.addWidget(self.comboBoxLabNode)

        self.horizontalLayoutLabsPool = QHBoxLayout()
        self.horizontalLayoutLabsPool.setObjectName(u"horizontalLayoutLabsPool")
        self.labelLabPool = QLabel(self.layoutWidget)
        self.labelLabPool.setObjectName(u"labelLabPool")
        self.labelLabPool.setFont(font2)

        self.comboBoxLabPool = QComboBox(self.layoutWidget)
        self.comboBoxLabPool.setObjectName(u"comboBoxLabPool")

        self.horizontalLayoutLabsPool.addWidget(self.labelLabPool)
        self.horizontalLayoutLabsPool.addWidget(self.comboBoxLabPool)

        self.verticalLayoutLabs.addLayout(self.horizontalLayoutLabsNode)
        self.verticalLayoutLabs.addLayout(self.horizontalLayoutLabsPool)

        self.horizontalLayoutLabsConfig = QHBoxLayout()
        self.horizontalLayoutLabsConfig.setObjectName(u"horizontalLayoutLabsConfig")
        self.labelSelectLab = QLabel(self.layoutWidget)
        self.labelSelectLab.setObjectName(u"labelSelectLab")
        self.labelSelectLab.setFont(font2)

        self.horizontalLayoutLabsConfig.addWidget(self.labelSelectLab)

        self.comboBoxLabConfig = QComboBox(self.layoutWidget)
        self.comboBoxLabConfig.setObjectName(u"comboBoxLabConfig")

        self.horizontalLayoutLabsConfig.addWidget(self.comboBoxLabConfig)

        self.verticalLayoutLabs.addLayout(self.horizontalLayoutLabsConfig)

        self.horizontalLayoutLabNetwork = QHBoxLayout()
        self.horizontalLayoutLabNetwork.setObjectName(u"horizontalLayoutLabNetwork")
        self.labelLabNetwork = QLabel(self.layoutWidget)
        self.labelLabNetwork.setObjectName(u"labelLabNetwork")
        self.labelLabNetwork.setFont(font2)

        self.horizontalLayoutLabNetwork.addWidget(self.labelLabNetwork)

        self.comboBoxLabNetwork = QComboBox(self.layoutWidget)
        self.comboBoxLabNetwork.setObjectName(u"comboBoxLabNetwork")

        self.horizontalLayoutLabNetwork.addWidget(self.comboBoxLabNetwork)

        self.verticalLayoutLabs.addLayout(self.horizontalLayoutLabNetwork)

        self.checkBox = QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font2)
        self.checkBox.setChecked(True)

        self.verticalLayoutLabs.addWidget(self.checkBox)

        self.pushButtonCreateLabEnvironment = QPushButton(self.layoutWidget)
        self.pushButtonCreateLabEnvironment.setObjectName(u"pushButtonCreateLabEnvironment")

        self.verticalLayoutLabs.addWidget(self.pushButtonCreateLabEnvironment)

        self.horizontalLayoutAdditionalTools.addLayout(self.verticalLayoutLabs)

        self.verticalLayout.addLayout(self.horizontalLayoutAdditionalTools)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.listWidgetPools.itemSelectionChanged.connect(self.updateVmsListFromPool)
        self.listWidgetVms.itemSelectionChanged.connect(self.updateVmSelected)
        self.checkBoxTemplatesRestriction.toggled.connect(self.updateVmsListFromPool)
        self.pushButtonClone.clicked.connect(self.clonePoolToPool)
        self.pushButtonDelete.clicked.connect(self.clearResourcePool)
        self.pushButtonCreateNewSnapshots.clicked.connect(self.createSnapshots)
        self.pushButtonRevertToLatest.clicked.connect(self.revertLatestSnapshot)
        self.pushButtonRevertToOldest.clicked.connect(self.revertEarliestSnapshot)
        self.pushButtonCloneVM.clicked.connect(self.cloneVM)
        self.comboBoxSelectNode.currentTextChanged.connect(self.updateNetworkBridgesCloning)
        self.comboBoxLabNode.currentTextChanged.connect(self.updateNetworkBridgesLab)
        self.pushButtonCreateLabEnvironment.clicked.connect(self.createLabEnvironment)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"ProxMox Lab Manager", None))
        self.labelPoolSelect.setText(QCoreApplication.translate("MainWindow", u"Select a Source Resource Pool", None))
        self.labelVmListView.setText(QCoreApplication.translate("MainWindow", u"Select a VM if Applicable", None))
        self.checkBoxTemplatesRestriction.setText(
            QCoreApplication.translate("MainWindow", u"Restrict View and Cloning Operations to Templates Only", None))
        self.labelPoolManagement.setText(QCoreApplication.translate("MainWindow", u"Pool Management", None))
        self.labelCloning.setText(QCoreApplication.translate("MainWindow", u"Cloning", None))
        self.labelTemplateNote.setText(
            QCoreApplication.translate("MainWindow", u"Note: Creates Linked Clones.", None))
        self.labelSelectNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.comboBoxSelectNode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.labelConfirmSourcePool.setText(QCoreApplication.translate("MainWindow", u"Confirm Source Pool:", None))
        self.labelSourcePool.setText(QCoreApplication.translate("MainWindow", u"...select a source pool above", None))
        self.labelTargetPool.setText(QCoreApplication.translate("MainWindow", u"Select Target Pool", None))
        self.comboBoxTargetPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.labelPoolCloneNetwork.setText(QCoreApplication.translate("MainWindow", u"Select Network", None))
        self.checkBoxStartClonedPoolVms.setText(QCoreApplication.translate("MainWindow", u"Start VMs on Deploy", None))
        self.pushButtonClone.setText(QCoreApplication.translate("MainWindow", u"Clone Pool", None))
        self.labelSnapshots.setText(QCoreApplication.translate("MainWindow", u"Snapshot Management", None))
        self.labelSnapshotNote1.setText(
            QCoreApplication.translate("MainWindow", u"Note: Not applicable to templates", None))
        self.labelSnapshotNote2.setText(
            QCoreApplication.translate("MainWindow", u"Note: All target VM's will be shutdown first.", None))
        self.labelSnapshotNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.labelSelectSnapshotPool.setText(QCoreApplication.translate("MainWindow", u"Select Pool", None))
        self.comboBoxSnapshotPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonRevertToOldest.setText(QCoreApplication.translate("MainWindow", u"Revert to Oldest", None))
        self.pushButtonRevertToLatest.setText(QCoreApplication.translate("MainWindow", u"Revert to Latest", None))
        self.labelNewSnapshotName.setText(QCoreApplication.translate("MainWindow", u"New snapshot base name:", None))
        self.lineEditSnapshotName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonCreateNewSnapshots.setText(
            QCoreApplication.translate("MainWindow", u"Create New Snapshots", None))
        self.labelDeleting.setText(QCoreApplication.translate("MainWindow", u"Resource Removal", None))
        self.labelDeletingNote1.setText(
            QCoreApplication.translate("MainWindow", u"Note: Only removes non-template virtual machines.", None))
        self.labelDeletingNote2.setText(
            QCoreApplication.translate("MainWindow", u"Note: Will not remove Protected virtual machines.", None))
        self.labelDeleteSelectPool.setText(QCoreApplication.translate("MainWindow", u"Select Pool", None))
        self.comboBoxDeleteSelectPool.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Required", None))
        self.pushButtonDelete.setText(
            QCoreApplication.translate("MainWindow", u"Remove Non-Protected Non-Template VM's", None))
        self.labelAdditionalTools.setText(QCoreApplication.translate("MainWindow", u"Additional Tools", None))
        self.labelCloneIndividualVM.setText(QCoreApplication.translate("MainWindow", u"Clone Single VM", None))
        self.labelVMNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.labelVMConfirmSourcePool.setText(QCoreApplication.translate("MainWindow", u"Confirm Source Pool", None))
        self.labelVMSelectedSourcePool.setText(
            QCoreApplication.translate("MainWindow", u"...select a source pool above", None))
        self.labelVMConfirmVM.setText(QCoreApplication.translate("MainWindow", u"Confirm Source VM", None))
        self.labelVMSelectedVM.setText(QCoreApplication.translate("MainWindow", u"..select a source VM above", None))
        self.labelVMSelectTargetPool.setText(QCoreApplication.translate("MainWindow", u"Select Target Pool", None))
        self.labelNewVMName.setText(QCoreApplication.translate("MainWindow", u"Enter a name for the new VM", None))
        self.lineEditVMName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Optional", None))
        self.pushButtonCloneVM.setText(QCoreApplication.translate("MainWindow", u"Clone VM", None))
        self.labelLabs.setText(QCoreApplication.translate("MainWindow", u"Create a Lab Environment", None))
        self.labelLabNode.setText(QCoreApplication.translate("MainWindow", u"Select Node", None))
        self.labelLabPool.setText(QCoreApplication.translate("MainWindow", u"Select Pool", None))
        self.labelSelectLab.setText(QCoreApplication.translate("MainWindow", u"Select Lab Config", None))
        self.labelLabNetwork.setText(QCoreApplication.translate("MainWindow", u"Select Network", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Start VMs on Deploy", None))
        self.pushButtonCreateLabEnvironment.setText(
            QCoreApplication.translate("MainWindow", u"Create Lab Environment", None))

        self.updateNodesDropdown()
        self.updatePoolsList()
        self.updateVmsListFromPool()
        self.updateNetworkBridgesCloning()
        self.updateNetworkBridgesLab()
        self.updateLabTemplates()

    # retranslateUi

    def updateNodesDropdown(self):
        print("LOG: Updating Nodes List")
        print(self.nodes)

        for node in self.nodes["data"]:
            self.comboBoxSelectNode.addItem(node["node"])
            self.comboBoxSnapshotNode.addItem(node["node"])
            self.comboBoxLabNode.addItem(node["node"])
            self.comboBoxVMNode.addItem(node["node"])

        self.comboBoxSelectNode.setCurrentIndex(0)
        self.comboBoxVMNode.setCurrentIndex(0)
        self.comboBoxLabNode.setCurrentIndex(0)
        self.comboBoxSnapshotNode.setCurrentIndex(0)

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
        self.labelSourcePool.setText(selectedPool)
        self.labelVMSelectedSourcePool.setText(selectedPool)
        return

    def updatePoolsList(self):
        print("LOG: Updating Pools Lists")
        self.listWidgetPools.clear()
        self.comboBoxDeleteSelectPool.clear()
        self.comboBoxTargetPool.clear()
        self.comboBoxSnapshotPool.clear()
        self.comboBoxVMTargetPool.clear()
        self.comboBoxLabPool.clear()

        for pool in self.pmconnection.pools:
            self.listWidgetPools.addItem(pool)
            self.comboBoxDeleteSelectPool.addItem(pool)
            self.comboBoxTargetPool.addItem(pool)
            self.comboBoxSnapshotPool.addItem(pool)
            self.comboBoxVMTargetPool.addItem(pool)
            self.comboBoxLabPool.addItem(pool)

        self.listWidgetPools.setSortingEnabled(1)

        self.listWidgetPools.update()
        self.comboBoxDeleteSelectPool.update()
        self.comboBoxTargetPool.update()
        self.comboBoxSnapshotPool.update()
        self.comboBoxVMTargetPool.update()
        self.comboBoxLabPool.update()
        return

    def updateVmSelected(self):
        try:
            selectedVM = self.listWidgetVms.selectedItems()[0].text()
            self.labelVMSelectedVM.setText(selectedVM)
        except:
            self.labelVMSelectedVM.setText("No VM Selected")
        return

    def clonePoolToPool(self):
        self.pushButtonClone.setDisabled(1)
        sourcePool = self.listWidgetPools.selectedItems()[0].text()
        targetNode = self.comboBoxSelectNode.currentText()
        targetPool = self.comboBoxTargetPool.currentText()
        targetNetwork = self.comboBoxCloneNetwork.currentText()

        for vmid in self.pmconnection.pools[sourcePool]:
            if self.pmconnection.virtual_machines[str(vmid)]["template"] == 1:
                print("LOG: Cloning " + self.pmconnection.virtual_machines[str(vmid)]["name"])
                newVMID = self.pmconnection.create_clone_linked(self.comboBoxSelectNode.currentText(), str(vmid), targetPool)
                self.pmconnection.set_network_bridge(targetNode, str(newVMID), "net0", targetNetwork)
                if self.checkBoxStartClonedPoolVms.isChecked():
                    print("Starting the VM")
                    print(self.pmconnection.startVM(str(newVMID)))
        self.pmconnection.get_initial_gui_data(self.nodes)
        self.updateVmsListFromPool()
        self.pushButtonClone.setDisabled(0)
        return

    def cloneVM(self):
        self.pushButtonCloneVM.setDisabled(1)
        targetNode = self.comboBoxVMNode.currentText()
        sourceVM = self.listWidgetVms.selectedItems()[0].text()
        sourceVMShortName = sourceVM.replace("[template]","")
        sourceVMID = ""

        for vm in self.pmconnection.virtual_machines:
            if self.pmconnection.virtual_machines[vm]["name"] == sourceVMShortName:
                sourceVMID = vm
                break

        targetPool = self.comboBoxVMTargetPool.currentText()
        targetName = self.lineEditVMName.text()
        self.pmconnection.create_clone_full(targetNode, sourceVMID, targetPool, targetName)
        self.updateVmsListFromPool()
        self.pushButtonCloneVM.setDisabled(0)

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
            self.pmconnection.create_snapshot(self.comboBoxSnapshotNode.currentText(), str(vmid),
                                              self.lineEditSnapshotName.text())
        self.pushButtonCreateNewSnapshots.setDisabled(0)
        return

    def revertLatestSnapshot(self):
        self.pushButtonRevertToLatest.setDisabled(1)
        targetPool = self.comboBoxSnapshotPool.currentText()
        print("LOG: Reverting to latest snapshots for " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Reverting snapshot to latest for " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.revertLatestSnapshot(self.comboBoxSnapshotNode.currentText(), str(vmid))
        self.pushButtonRevertToLatest.setDisabled(0)
        return

    def revertEarliestSnapshot(self):
        self.pushButtonRevertToOldest.setDisabled(1)
        targetPool = self.comboBoxSnapshotPool.currentText()
        print("LOG: Reverting to latest snapshots for " + targetPool)
        for vmid in self.pmconnection.pools[targetPool]:
            print("LOG: --- Reverting snapshot to latest for " + self.pmconnection.virtual_machines[str(vmid)]["name"])
            self.pmconnection.revertEarliestSnapshot(self.comboBoxSnapshotNode.currentText(), str(vmid))
        self.pushButtonRevertToLatest.setDisabled(0)
        return

    def updateNetworkBridgesCloning(self):
        self.comboBoxCloneNetwork.clear()
        currentNode = self.comboBoxSelectNode.currentText()
        for bridge in self.pmconnection.bridges[currentNode]:
            self.comboBoxCloneNetwork.addItem(bridge)
        self.comboBoxCloneNetwork.update()
        return

    def updateNetworkBridgesLab(self):
        self.comboBoxLabNetwork.clear()
        currentNode = self.comboBoxLabNode.currentText()
        for bridge in self.pmconnection.bridges[currentNode]:
            self.comboBoxLabNetwork.addItem(bridge)
        self.comboBoxLabNetwork.update()
        return

    def getLabTemplates(self):
        self.labTemplates += [each for each in os.listdir(os.getcwd()) if each.endswith('.lab')]
        print(self.labTemplates)
        return

    def updateLabTemplates(self):
        for template in self.labTemplates:
            self.comboBoxLabConfig.addItem(template)
        return

    def createLabEnvironment(self):
        self.pushButtonCreateLabEnvironment.setDisabled(1)
        labFile = open(self.comboBoxLabConfig.currentText(),'r')
        labLines = labFile.readlines()
        fullClone = True
        for line in labLines:
            lineFixed = line.replace("\n", "")
            if lineFixed == "[full]":
                fullClone = True
            elif lineFixed == "[linked]":
                fullClone = False
            else:
                if fullClone:
                    newVMID = self.pmconnection.create_clone_full(self.comboBoxLabNode.currentText(), lineFixed, self.comboBoxLabPool.currentText())
                    self.pmconnection.set_network_bridge(self.comboBoxLabNode.currentText(), str(newVMID), "net0", self.comboBoxLabNetwork.currentText())
                    if self.checkBox.isChecked():
                        self.pmconnection.startVM(str(newVMID))
                else:
                    newVMID = self.pmconnection.create_clone_linked(self.comboBoxLabNode.currentText(), lineFixed, self.comboBoxLabPool.currentText())
                    self.pmconnection.set_network_bridge(self.comboBoxLabNode.currentText(), str(newVMID), "net0", self.comboBoxLabNetwork.currentText())
                    if self.checkBox.isChecked():
                        self.pmconnection.startVM(str(newVMID))
        self.pushButtonCreateLabEnvironment.setDisabled(0)
        return