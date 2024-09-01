# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:36:44 2024

@author: Physe
"""

import sys
from PyQt5.QtCore import Qt, QThreadPool, QRunnable, pyqtSlot, pyqtSignal, QObject
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QSpinBox,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
    QFrame,
    QMessageBox,
    QProgressBar
    )
from qdarktheme import setup_theme
from numpy import floor, ceil
from requests import get, RequestException
from Magic_Find_Req_Luck import Magic_Find_Req_Luck_List

class GUI(QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.threadpool = QThreadPool()
        
        self.Set_Up_GUI()
    
    def Set_Up_GUI(self):
        
        self.setWindowTitle('Luck Boost Profitability')
        
        """
        Interactable Features
        """
        # Run Button
        self.Run_Button = QPushButton("CALCULATE")
        self.Run_Button.pressed.connect(self.CALCULATE)
        
        # Box to specify number of Ectos to Buy
        self.Number_of_Ectos_to_Buy = QSpinBox()
        self.Number_of_Ectos_to_Buy.setMinimum(1)
        self.Number_of_Ectos_to_Buy.setMaximum(250)
        self.Number_of_Ectos_to_Buy.setValue(1)
        self.Number_of_Ectos_to_Buy.setAlignment(Qt.AlignCenter)
        
        # Box to specify current Base Magic Find
        self.Current_MF = QSpinBox()
        self.Current_MF.setMinimum(0)
        self.Current_MF.setMaximum(300)
        self.Current_MF.setValue(0)
        self.Current_MF.setAlignment(Qt.AlignCenter)
        
        # Box to specify current Luck
        self.Current_Luck = QSpinBox()
        self.Current_Luck.setMinimum(0)
        self.Current_Luck.setMaximum(472_510)
        self.Current_Luck.setValue(0)
        self.Current_Luck.setAlignment(Qt.AlignCenter)

        # Drop Box to specify which Salvage Tool to Use
        self.Salvage_Tool_Select = QComboBox()
        self.Salvage_Tools = [
            "Crude Salvage Kit.........................(2.13 CpU | 1.47 DpE)",
            "Basic Salvage Kit..........................(3.52 CpU | 1.63 DpE)",
            "Copper-Fed Salvage-o-Matic.......(3.00 CpU | 1.63 DpE)",
            "Fine Salvage Kit..........................(11.52 CpU | 1.75 DpE)",
            "Journeyman's Salvage Kit.............(32.0 CpU | 1.58 DpE)",
            "Runecrafter's Salvage-o-Matic.....(30.0 CpU | 1.58 DpE)",
            "Master's Salvage Kit...................(61.44 CpU | 1.85 DpE)",
            "Silver-Fed Salvage-o-Matic..........(60.0 CpU | 1.85 DpE)",
            "Mystic Salvage Kit........................(60.0 CpU | 1.85 DpE)",
            "Black Lion Salvage Kit...................(0.0 CpU | 2.04 DpE)"
            ]
        self.Salvage_Tool_Select.addItems(self.Salvage_Tools)
        
        # Check Boxes to select either Place Order or Buy Instantly (Ectos)
        self.Ecto_Place_Order_Checkbox = QCheckBox("Place Order (Ectos)")
        self.Ecto_Place_Order_Checkbox.setChecked(True)
        self.Ecto_Buy_Instantly_Checkbox = QCheckBox("Buy Instantly (Ectos)")
        
        self.Ecto_Place_Order_Checkbox.stateChanged.connect(self.Manage_Checkboxes)
        self.Ecto_Buy_Instantly_Checkbox.stateChanged.connect(self.Manage_Checkboxes)
        
        # Check Boxes to select either Sell Instantly or List This Item (Dust)
        self.Dust_Sell_Instantly_Checkbox = QCheckBox("Sell Instantly (Dust)")
        self.Dust_List_This_Item_CheckBox = QCheckBox("List This Item (Dust)")
        self.Dust_List_This_Item_CheckBox.setChecked(True)
        
        self.Dust_Sell_Instantly_Checkbox.stateChanged.connect(self.Manage_Checkboxes)
        self.Dust_List_This_Item_CheckBox.stateChanged.connect(self.Manage_Checkboxes)
        
        """
        General Labels
        """
        self.Prompt_User_Salveage_Tool_Label = QLabel("Salvage Tool/Kit you will use:")
        self.Prompt_User_Amount_of_Ectos_Label = QLabel("Number of Ectos you will purchase:")
        self.Current_Ecto_TP_Price_Label = QLabel("How will you purchase your Globs of Ectoplasm:")
        self.Current_Dust_TP_Price_Label = QLabel("How will you sell your resultant Piles of Crystalline Dust:")
        self.Total_Profit_Label = QLabel("ESTIMATED TOTAL PROFIT:")
        self.Estimated_Yield_Label = QLabel("ESTIMATED YIELD:")
        self.Essence_of_Luck_Fine_Yield_Label = QLabel("Essence of Luck (fine)")
        self.Essence_of_Luck_Masterwork_Yield_Label = QLabel("Essence of Luck (masterwork)")
        self.Essence_of_Luck_Rare_Yield_Label = QLabel("Essence of Luck (rare)")
        self.Essence_of_Luck_Exotic_Yield_Label = QLabel("Essence of Luck (exotic)")
        self.Pile_of_Crystalline_Dust_Estimated_Yield_Label = QLabel("Pile of Crystalline Dust")
        self.Current_MF_Label = QLabel("Please enter your current Base Magic Find:")
        self.Current_Luck_Label = QLabel("Please enter your current Luck:")
        self.Resultant_Luck_and_Magic_Find_Label = QLabel("ESTIMATED RESULTANT BASE MAGIC FIND AND LUCK:")
        self.Magic_Find_Label = QLabel("+0%")
        
        """
        Glob of Ectoplasm/Pile of Crystalline Dust Icons
        """
        self.Glob_of_Ectoplasm_Label = QLabel()
        self.Glob_of_Ectoplasm_Image = QPixmap("Images/Glob_of_Ectoplasm.png")
        self.Glob_of_Ectoplasm_Image = self.Glob_of_Ectoplasm_Image.scaled(50, 50, aspectRatioMode=True)
        self.Glob_of_Ectoplasm_Label.setPixmap(self.Glob_of_Ectoplasm_Image)
        
        self.Pile_of_Crystalline_Dust_Label_1 = QLabel()
        self.Pile_of_Crystalline_Dust_Image_1 = QPixmap("Images/Pile_of_Crystalline_Dust.png")
        self.Pile_of_Crystalline_Dust_Image_1 = self.Pile_of_Crystalline_Dust_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Pile_of_Crystalline_Dust_Label_1.setPixmap(self.Pile_of_Crystalline_Dust_Image_1)
        
        self.Pile_of_Crystalline_Dust_Label_2 = QLabel()
        self.Pile_of_Crystalline_Dust_Image_2 = QPixmap("Images/Pile_of_Crystalline_Dust.png")
        self.Pile_of_Crystalline_Dust_Image_2 = self.Pile_of_Crystalline_Dust_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Pile_of_Crystalline_Dust_Label_2.setPixmap(self.Pile_of_Crystalline_Dust_Image_2)
        
        """
        Profit/Loss/Placeholder Icons
        """
        self.Profit_Image = QPixmap("Images/Profit.png")
        self.Scaled_Profit_Image = self.Profit_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Loss_Image = QPixmap("Images/Loss.png")
        self.Scaled_Loss_Image = self.Loss_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Placeholder_Image = QPixmap("Images/User_Fey_Zeal_Gw2wlogo.png")
        self.Scaled_Placeholder_Image = self.Placeholder_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Flexible_Label = QLabel()
        self.Flexible_Label.setPixmap(self.Scaled_Placeholder_Image)
        
        """
        Coin Icons
        """
        # Gold
        self.Gold_Coin_Label_1 = QLabel()
        self.Gold_Coin_Image_1 = QPixmap("Images/Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_1 = self.Gold_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_1.setPixmap(self.Scaled_Gold_Coin_Image_1)
        
        self.Gold_Coin_Label_2 = QLabel()
        self.Gold_Coin_Image_2 = QPixmap("Images/Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_2 = self.Gold_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_2.setPixmap(self.Scaled_Gold_Coin_Image_2)
        
        self.Gold_Coin_Label_3 = QLabel()
        self.Gold_Coin_Image_3 = QPixmap("Images/Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_3 = self.Gold_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_3.setPixmap(self.Scaled_Gold_Coin_Image_3)
        
        # Silver
        self.Silver_Coin_Label_1 = QLabel()
        self.Silver_Coin_Image_1 = QPixmap("Images/Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_1 = self.Silver_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_1.setPixmap(self.Scaled_Silver_Coin_Image_1)
        
        self.Silver_Coin_Label_2 = QLabel()
        self.Silver_Coin_Image_2 = QPixmap("Images/Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_2 = self.Silver_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_2.setPixmap(self.Scaled_Silver_Coin_Image_2)
        
        self.Silver_Coin_Label_3 = QLabel()
        self.Silver_Coin_Image_3 = QPixmap("Images/Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_3 = self.Silver_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_3.setPixmap(self.Scaled_Silver_Coin_Image_3)
        
        # Copper
        self.Copper_Coin_Label_1 = QLabel()
        self.Copper_Coin_Image_1 = QPixmap("Images/Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_1 = self.Copper_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_1.setPixmap(self.Scaled_Copper_Coin_Image_1)
        
        self.Copper_Coin_Label_2 = QLabel()
        self.Copper_Coin_Image_2 = QPixmap("Images/Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_2 = self.Copper_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_2.setPixmap(self.Scaled_Copper_Coin_Image_2)
        
        self.Copper_Coin_Label_3 = QLabel()
        self.Copper_Coin_Image_3 = QPixmap("Images/Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_3 = self.Copper_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_3.setPixmap(self.Scaled_Copper_Coin_Image_3)
        
        """
        Essences of Luck Icons
        """
        # Essence of Luck (Fine)
        self.Essence_of_Luck_Fine_Label = QLabel()
        self.Essence_of_Luck_Fine_Image = QPixmap("Images/Essence_of_Luck_(fine).png")
        self.Scaled_Essence_of_Luck_Fine_Image = self.Essence_of_Luck_Fine_Image.scaled(50, 50, aspectRatioMode=True)
        self.Essence_of_Luck_Fine_Label.setPixmap(self.Scaled_Essence_of_Luck_Fine_Image)
        
        # Essence of Luck (Masterwork)
        self.Essence_of_Luck_Masterwork_Label = QLabel()
        self.Essence_of_Luck_Masterwork_Image = QPixmap("Images/Essence_of_Luck_(masterwork).png")
        self.Scaled_Essence_of_Luck_Masterwork_Image = self.Essence_of_Luck_Masterwork_Image.scaled(50, 50, aspectRatioMode=True)
        self.Essence_of_Luck_Masterwork_Label.setPixmap(self.Scaled_Essence_of_Luck_Masterwork_Image)
        
        # Essence of Luck (Rare)
        self.Essence_of_Luck_Rare_Label = QLabel()
        self.Essence_of_Luck_Rare_Image = QPixmap("Images/Essence_of_Luck_(rare).png")
        self.Scaled_Essence_of_Luck_Rare_Image = self.Essence_of_Luck_Rare_Image.scaled(50, 50, aspectRatioMode=True)
        self.Essence_of_Luck_Rare_Label.setPixmap(self.Scaled_Essence_of_Luck_Rare_Image)
        
        # Essence of Luck (Exotic)
        self.Essence_of_Luck_Exotic_Label = QLabel()
        self.Essence_of_Luck_Exotic_Image = QPixmap("Images/Essence_of_Luck_(exotic).png")
        self.Scaled_Essence_of_Luck_Exotic_Image = self.Essence_of_Luck_Exotic_Image.scaled(50, 50, aspectRatioMode=True)
        self.Essence_of_Luck_Exotic_Label.setPixmap(self.Scaled_Essence_of_Luck_Exotic_Image)
        
        """
        Text Fields
        """
        self.Gold_Profit_Field = QLineEdit()
        self.Gold_Profit_Field.setDisabled(True)
        self.Gold_Profit_Field.setAlignment(Qt.AlignRight)
        
        self.Silver_Profit_Field = QLineEdit()
        self.Silver_Profit_Field.setDisabled(True)
        self.Silver_Profit_Field.setAlignment(Qt.AlignRight)
        
        self.Copper_Profit_Field = QLineEdit()
        self.Copper_Profit_Field.setDisabled(True)
        self.Copper_Profit_Field.setAlignment(Qt.AlignRight)
        
        self.Ecto_Gold_Price_Field = QLineEdit()
        self.Ecto_Gold_Price_Field.setDisabled(True)
        self.Ecto_Gold_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Ecto_Silver_Price_Field = QLineEdit()
        self.Ecto_Silver_Price_Field.setDisabled(True)
        self.Ecto_Silver_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Ecto_Copper_Price_Field = QLineEdit()
        self.Ecto_Copper_Price_Field.setDisabled(True)
        self.Ecto_Copper_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Dust_Gold_Price_Field = QLineEdit()
        self.Dust_Gold_Price_Field.setDisabled(True)
        self.Dust_Gold_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Dust_Silver_Price_Field = QLineEdit()
        self.Dust_Silver_Price_Field.setDisabled(True)
        self.Dust_Silver_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Dust_Copper_Price_Field = QLineEdit()
        self.Dust_Copper_Price_Field.setDisabled(True)
        self.Dust_Copper_Price_Field.setAlignment(Qt.AlignRight)
        
        self.Essence_of_Luck_Fine_Estimated_Yield_Field = QLineEdit()
        self.Essence_of_Luck_Fine_Estimated_Yield_Field.setDisabled(True)
        self.Essence_of_Luck_Fine_Estimated_Yield_Field.setAlignment(Qt.AlignCenter)
        
        self.Essence_of_Luck_Masterwork_Estimated_Yield_Field = QLineEdit()
        self.Essence_of_Luck_Masterwork_Estimated_Yield_Field.setDisabled(True)
        self.Essence_of_Luck_Masterwork_Estimated_Yield_Field.setAlignment(Qt.AlignCenter)
        
        self.Essence_of_Luck_Rare_Estimated_Yield_Field = QLineEdit()
        self.Essence_of_Luck_Rare_Estimated_Yield_Field.setDisabled(True)
        self.Essence_of_Luck_Rare_Estimated_Yield_Field.setAlignment(Qt.AlignCenter)
        
        self.Essence_of_Luck_Exotic_Estimated_Yield_Field = QLineEdit()
        self.Essence_of_Luck_Exotic_Estimated_Yield_Field.setDisabled(True)
        self.Essence_of_Luck_Exotic_Estimated_Yield_Field.setAlignment(Qt.AlignCenter)
        
        self.Dust_Estimated_Yield_Field = QLineEdit()
        self.Dust_Estimated_Yield_Field.setDisabled(True)
        self.Dust_Estimated_Yield_Field.setAlignment(Qt.AlignCenter)
        
        """
        Luck Progress Bar
        """
        #!!!
        self.Resultant_Luck_Bar = QProgressBar()
        self.Resultant_Luck_Bar.setFormat("0")
        self.Resultant_Luck_Bar.setValue(0)
        
        """
        Salvage Tool/Number of Ectos to Buy Layer
        """
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer = QVBoxLayout()
        
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Prompt_User_Salveage_Tool_Label)
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Salvage_Tool_Select, alignment=Qt.AlignCenter)
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Prompt_User_Amount_of_Ectos_Label)
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Number_of_Ectos_to_Buy, alignment=Qt.AlignCenter)
        
        """
        Ecto Place Order or Buy Instantly Layer
        """
        self.Ecto_Place_Order_or_Buy_Instantly_Layout = QHBoxLayout()
        
        self.Ecto_Place_Order_or_Buy_Instantly_Layout.addWidget(self.Ecto_Place_Order_Checkbox, alignment=Qt.AlignCenter)
        self.Ecto_Place_Order_or_Buy_Instantly_Layout.addWidget(self.Ecto_Buy_Instantly_Checkbox, alignment=Qt.AlignCenter)
        
        """
        Dust Sell Instantly or List This Item Layer
        """
        self.Dust_Sell_Instantly_or_List_This_Item_Layout = QHBoxLayout()
        
        self.Dust_Sell_Instantly_or_List_This_Item_Layout.addWidget(self.Dust_Sell_Instantly_Checkbox, alignment=Qt.AlignCenter)
        self.Dust_Sell_Instantly_or_List_This_Item_Layout.addWidget(self.Dust_List_This_Item_CheckBox, alignment=Qt.AlignCenter)
        
        """
        Current Glob of Ectoplasm Trading Post Price Layout
        """
        self.Current_Ecto_TP_Price_Layout = QHBoxLayout()
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Gold_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Gold_Coin_Label_2)
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Silver_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Silver_Coin_Label_2)
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Copper_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Copper_Coin_Label_2)
        
        """
        Current Pile of Crystalline Dust Trading Post Price Layout
        """
        self.Current_Dust_TP_Price_Layout = QHBoxLayout()
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Gold_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Gold_Coin_Label_3)
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Silver_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Silver_Coin_Label_3)
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Copper_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Copper_Coin_Label_3)
        
        """
        Profit Layout
        """
        self.Profit_Layout = QHBoxLayout()
        
        self.Profit_Layout.addWidget(self.Flexible_Label)
        
        self.Profit_Layout.addWidget(self.Gold_Profit_Field)
        self.Profit_Layout.addWidget(self.Gold_Coin_Label_1)
        
        self.Profit_Layout.addWidget(self.Silver_Profit_Field)
        self.Profit_Layout.addWidget(self.Silver_Coin_Label_1)
        
        self.Profit_Layout.addWidget(self.Copper_Profit_Field)
        self.Profit_Layout.addWidget(self.Copper_Coin_Label_1)
        
        """
        Estimated Yield Layout
        """
        # Macro Estimated Yield Layout
        self.Estimated_Yield_Layout = QVBoxLayout()
        
        # Micro Estimated Yield Layouts
        self.Row_1 = QHBoxLayout()
        self.Row_2 = QHBoxLayout()
        
        # Essence of Luck (Fine) Frame
        self.Essence_of_Luck_Fine_Frame = QFrame()
        self.Essence_of_Luck_Fine_Frame.setFrameShape(QFrame.StyledPanel)
        self.Essence_of_Luck_Fine_Frame.setFrameShadow(QFrame.Raised)
        self.Essence_of_Luck_Fine_Frame_Layout = QVBoxLayout()
        self.Essence_of_Luck_Fine_Frame.setLayout(self.Essence_of_Luck_Fine_Frame_Layout)
        self.Essence_of_Luck_Fine_Frame_Layout.addWidget(self.Essence_of_Luck_Fine_Yield_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Fine_Frame_Layout.addWidget(self.Essence_of_Luck_Fine_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Fine_Frame_Layout.addWidget(self.Essence_of_Luck_Fine_Estimated_Yield_Field , alignment=Qt.AlignCenter)
        
        # Essence of Luck (Masterwork) Frame
        self.Essence_of_Luck_Masterwork_Frame = QFrame()
        self.Essence_of_Luck_Masterwork_Frame.setFrameShape(QFrame.StyledPanel)
        self.Essence_of_Luck_Masterwork_Frame.setFrameShadow(QFrame.Raised)
        self.Essence_of_Luck_Masterwork_Frame_Layout = QVBoxLayout()
        self.Essence_of_Luck_Masterwork_Frame.setLayout(self.Essence_of_Luck_Masterwork_Frame_Layout)
        self.Essence_of_Luck_Masterwork_Frame_Layout.addWidget(self.Essence_of_Luck_Masterwork_Yield_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Masterwork_Frame_Layout.addWidget(self.Essence_of_Luck_Masterwork_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Masterwork_Frame_Layout.addWidget(self.Essence_of_Luck_Masterwork_Estimated_Yield_Field , alignment=Qt.AlignCenter)
        
        # Essence of Luck (Rare) Frame
        self.Essence_of_Luck_Rare_Frame = QFrame()
        self.Essence_of_Luck_Rare_Frame.setFrameShape(QFrame.StyledPanel)
        self.Essence_of_Luck_Rare_Frame.setFrameShadow(QFrame.Raised)
        self.Essence_of_Luck_Rare_Frame_Layout = QVBoxLayout()
        self.Essence_of_Luck_Rare_Frame.setLayout(self.Essence_of_Luck_Rare_Frame_Layout)
        self.Essence_of_Luck_Rare_Frame_Layout.addWidget(self.Essence_of_Luck_Rare_Yield_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Rare_Frame_Layout.addWidget(self.Essence_of_Luck_Rare_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Rare_Frame_Layout.addWidget(self.Essence_of_Luck_Rare_Estimated_Yield_Field , alignment=Qt.AlignCenter)
        
        # Essence of Luck (Exotic) Frame
        self.Essence_of_Luck_Exotic_Frame = QFrame()
        self.Essence_of_Luck_Exotic_Frame.setFrameShape(QFrame.StyledPanel)
        self.Essence_of_Luck_Exotic_Frame.setFrameShadow(QFrame.Raised)
        self.Essence_of_Luck_Exotic_Frame_Layout = QVBoxLayout()
        self.Essence_of_Luck_Exotic_Frame.setLayout(self.Essence_of_Luck_Exotic_Frame_Layout)
        self.Essence_of_Luck_Exotic_Frame_Layout.addWidget(self.Essence_of_Luck_Exotic_Yield_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Exotic_Frame_Layout.addWidget(self.Essence_of_Luck_Exotic_Label, alignment=Qt.AlignCenter)
        self.Essence_of_Luck_Exotic_Frame_Layout.addWidget(self.Essence_of_Luck_Exotic_Estimated_Yield_Field , alignment=Qt.AlignCenter)
        
        # Essence of Luck (Exotic) Frame
        self.Pile_of_Crystalline_Dust_Frame = QFrame()
        self.Pile_of_Crystalline_Dust_Frame.setFrameShape(QFrame.StyledPanel)
        self.Pile_of_Crystalline_Dust_Frame.setFrameShadow(QFrame.Raised)
        self.Pile_of_Crystalline_Dust_Frame_Layout = QVBoxLayout()
        self.Pile_of_Crystalline_Dust_Frame.setLayout(self.Pile_of_Crystalline_Dust_Frame_Layout)
        self.Pile_of_Crystalline_Dust_Frame_Layout.addWidget(self.Pile_of_Crystalline_Dust_Estimated_Yield_Label, alignment=Qt.AlignCenter)
        self.Pile_of_Crystalline_Dust_Frame_Layout.addWidget(self.Pile_of_Crystalline_Dust_Label_2, alignment=Qt.AlignCenter)
        self.Pile_of_Crystalline_Dust_Frame_Layout.addWidget(self.Dust_Estimated_Yield_Field, alignment=Qt.AlignCenter)
        
        # Adding each of the above frames to the micro layout
        self.Row_1.addWidget(self.Essence_of_Luck_Fine_Frame)
        self.Row_1.addWidget(self.Essence_of_Luck_Masterwork_Frame)
        self.Row_2.addWidget(self.Essence_of_Luck_Rare_Frame)
        self.Row_2.addWidget(self.Essence_of_Luck_Exotic_Frame)
        
        # Adding the label and micro layout to the macro layout
        self.Estimated_Yield_Layout.addWidget(self.Estimated_Yield_Label)
        self.Estimated_Yield_Layout.addLayout(self.Row_1)
        self.Estimated_Yield_Layout.addLayout(self.Row_2)
        self.Estimated_Yield_Layout.addWidget(self.Pile_of_Crystalline_Dust_Frame)
        
        """
        Visual Dividers
        """
        self.Sub_Frame_1 = QFrame()
        self.Sub_Frame_1.setFrameShape(QFrame.StyledPanel)
        self.Sub_Frame_1_Layout = QVBoxLayout()
        self.Sub_Frame_1.setLayout(self.Sub_Frame_1_Layout)
        self.Sub_Frame_1_Layout.addWidget(self.Current_MF_Label)
        self.Sub_Frame_1_Layout.addWidget(self.Current_MF)
        self.Sub_Frame_1_Layout.addWidget(self.Current_Luck_Label)
        self.Sub_Frame_1_Layout.addWidget(self.Current_Luck)
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Sub_Frame_1)
        
        self.Frame_1 = QFrame()
        self.Frame_1.setFrameShape(QFrame.StyledPanel)
        self.Frame_1_Layout = QVBoxLayout()
        self.Frame_1.setLayout(self.Frame_1_Layout)
        self.Frame_1_Layout.addLayout(self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer)
        self.Frame_1_Layout.addWidget(self.Sub_Frame_1)
        
        self.Frame_2 = QFrame()
        self.Frame_2.setFrameShape(QFrame.Panel)
        self.Frame_2_Layout = QVBoxLayout()
        self.Frame_2.setLayout(self.Frame_2_Layout)
        self.Frame_2_Layout.addWidget(self.Current_Ecto_TP_Price_Label)
        self.Frame_2_Layout.addWidget(self.Glob_of_Ectoplasm_Label, alignment=Qt.AlignCenter)
        self.Frame_2_Layout.addLayout(self.Ecto_Place_Order_or_Buy_Instantly_Layout)
        self.Frame_2_Layout.addLayout(self.Current_Ecto_TP_Price_Layout)
        
        self.Frame_3 = QFrame()
        self.Frame_3.setFrameShape(QFrame.Panel)
        self.Frame_3_Layout = QVBoxLayout()
        self.Frame_3.setLayout(self.Frame_3_Layout)
        self.Frame_3_Layout.addWidget(self.Current_Dust_TP_Price_Label)
        self.Frame_3_Layout.addWidget(self.Pile_of_Crystalline_Dust_Label_1, alignment=Qt.AlignCenter)
        self.Frame_3_Layout.addLayout(self.Dust_Sell_Instantly_or_List_This_Item_Layout)
        self.Frame_3_Layout.addLayout(self.Current_Dust_TP_Price_Layout)
        
        self.Frame_4 = QFrame()
        self.Frame_4.setFrameShape(QFrame.Panel)
        self.Frame_4_Layout = QVBoxLayout()
        self.Frame_4.setLayout(self.Frame_4_Layout)
        self.Frame_4_Layout.addLayout(self.Estimated_Yield_Layout)
        #!!!
        self.Frame_5 = QFrame()
        self.Frame_5.setFrameShape(QFrame.Panel)
        self.Frame_5_Layout = QVBoxLayout()
        self.Frame_5.setLayout(self.Frame_5_Layout)
        self.Frame_5_Layout.addWidget(self.Resultant_Luck_and_Magic_Find_Label)
        self.Frame_5_Layout.addWidget(self.Magic_Find_Label, alignment=Qt.AlignCenter)
        self.Frame_5_Layout.addWidget(self.Resultant_Luck_Bar)
        
        self.Frame_6 = QFrame()
        self.Frame_6.setFrameShape(QFrame.StyledPanel)
        self.Frame_6_Layout = QVBoxLayout()
        self.Frame_6.setLayout(self.Frame_6_Layout)
        self.Frame_6_Layout.addWidget(self.Total_Profit_Label)
        self.Frame_6_Layout.addLayout(self.Profit_Layout)
        
        """
        GUI Layout
        """
        # Overall Layout
        self.GUI_Layout = QVBoxLayout()
        
        # Left and Right Columns
        self.Left_Column = QVBoxLayout()
        self.Right_Column = QVBoxLayout()
        
        # Adding Columns to GUI
        self.Columns = QHBoxLayout()
        self.Columns.addLayout(self.Left_Column)
        self.Columns.addLayout(self.Right_Column)
        self.GUI_Layout.addLayout(self.Columns)
        
        # Salvage Tool/Number of Ectos Stuff
        self.Left_Column.addWidget(self.Frame_1)
        
        # Ecto Related Stuff
        self.Left_Column.addWidget(self.Frame_2)
        
        # Dust Related Stuff
        self.Left_Column.addWidget(self.Frame_3)
        
        # Estimated Yield Stuff
        self.Right_Column.addWidget(self.Frame_4)
        
        # Estimated Resultant Luck/Magic Find
        self.Right_Column.addWidget(self.Frame_5)
        
        # Profit Related Stuff
        self.Right_Column.addWidget(self.Frame_6)
        
        # Run Button
        self.GUI_Layout.addWidget(self.Run_Button)
        
        self.setLayout(self.GUI_Layout)
    
    def CALCULATE(self):
        
        # Temporarily disable run button while CALCULATE runs
        self.Run_Button.setDisabled(True)
        
        # See what user selected for salvage tool
        self.Salvage_Tool = self.Salvage_Tool_Select.currentText()
        
        # See what amount of Ectos user wants to buy
        self.Number_of_Ectos = self.Number_of_Ectos_to_Buy.value()
        
        # See if user wants to place buy order or buy instantly (Ectos)
        if self.Ecto_Place_Order_Checkbox.isChecked():
            
            self.Ecto_Price = "BUY"
        
        else:
            
            self.Ecto_Price = "SELL"
        
        # See if user wants to instant sell or list (Dust)
        if self.Dust_Sell_Instantly_Checkbox.isChecked():
            
            self.Dust_Price = "BUY"
        
        else:
            
            self.Dust_Price = "SELL"
        
        # Get user's current Base Magic Find
        self.User_Base_Magic_Find = self.Current_MF.value()
        
        # Get user's current Luck
        self.User_Current_Luck = self.Current_Luck.value()
        
        # Spool up multithreaded worker
        self.worker = Worker(
            self.Salvage_Tool,
            self.Number_of_Ectos,
            self.Ecto_Price,
            self.Dust_Price,
            self.User_Base_Magic_Find,
            self.User_Current_Luck
            )
        
        # Let multithreaded worker print to console
        self.worker.signals.message.connect(self.PRINT)
        
        # Connect results of multithreaded worker to GUI configuration function
        self.worker.signals.RESULTS.connect(self.Set_Fields)
        
        # When multithreaded worker is done working, re-enable run button
        self.worker.signals.finished.connect(self.Enable_Run_Button)
        
        # Start multithreaded worker
        self.threadpool.start(self.worker)
    
    def Set_Fields(self, results: list):
        
        Gold_Profit = str(int(results[0]))
        Silver_Profit = str(int(results[1]))
        Copper_Profit = str(int(results[2]))
        
        Ecto_Price_Gold = str(int(results[3]))
        Ecto_Price_Silver = str(int(results[4]))
        Ecto_Price_Copper = str(int(results[5]))
        
        Dust_Price_Gold = str(int(results[6]))
        Dust_Price_Silver = str(int(results[7]))
        Dust_Price_Copper = str(int(results[8]))
        
        Fine_Luck_Yield = str(int(results[9]))
        Masterwork_Luck_Yield = str(int(results[10]))
        Rare_Luck_Yield = str(int(results[11]))
        Exotic_Luck_Yield = str(int(results[12]))
        
        Dust_Yield = str(int(results[13]))
        
        New_Base_MF = str(int(results[14]))
        New_Luck_int = int(results[15])
        New_Luck_str = str(int(results[15]))
        Next_Level_Luck_int = int(results[16])
        Next_Level_Luck_str = str(int(results[16]))
        #!!!
        if float(Gold_Profit) < 0:
            
            self.Flexible_Label.setPixmap(self.Scaled_Loss_Image)
        
        else:
            
            self.Flexible_Label.setPixmap(self.Scaled_Profit_Image)
            
        self.Gold_Profit_Field.setText(Gold_Profit)
        self.Silver_Profit_Field.setText(Silver_Profit)
        self.Copper_Profit_Field.setText(Copper_Profit)
        
        self.Ecto_Gold_Price_Field.setText(Ecto_Price_Gold)
        self.Ecto_Silver_Price_Field.setText(Ecto_Price_Silver)
        self.Ecto_Copper_Price_Field.setText(Ecto_Price_Copper)
        
        self.Dust_Gold_Price_Field.setText(Dust_Price_Gold)
        self.Dust_Silver_Price_Field.setText(Dust_Price_Silver)
        self.Dust_Copper_Price_Field.setText(Dust_Price_Copper)
        
        self.Essence_of_Luck_Fine_Estimated_Yield_Field.setText(Fine_Luck_Yield)
        self.Essence_of_Luck_Masterwork_Estimated_Yield_Field.setText(Masterwork_Luck_Yield)
        self.Essence_of_Luck_Rare_Estimated_Yield_Field.setText(Rare_Luck_Yield)
        self.Essence_of_Luck_Exotic_Estimated_Yield_Field.setText(Exotic_Luck_Yield)
        
        self.Dust_Estimated_Yield_Field.setText(Dust_Yield)
        
        if New_Base_MF == "300":
            New_Base_MF = "300 (MAX)"
            if New_Luck_int > 472_510:
                New_Luck_int = 472_510
                New_Luck_str = str(New_Luck_int)
        self.Magic_Find_Label.setText(f"+{New_Base_MF}%")
        self.Resultant_Luck_Bar.setFormat(f"{New_Luck_str}/{Next_Level_Luck_str}")
        self.Resultant_Luck_Bar.setMaximum(Next_Level_Luck_int)
        self.Resultant_Luck_Bar.setValue(New_Luck_int)
    
    def Manage_Checkboxes(self, state):
        
        sender = self.sender()
        
        if "Ectos" in sender.text():
            
            if "Buy Instantly" in sender.text():
                
                # If unchecked...
                if state == 0:
                    
                    self.Ecto_Place_Order_Checkbox.setChecked(True)
                
                else:
                    
                    self.Ecto_Place_Order_Checkbox.setChecked(False)
            
            else:
                
                if state == 0:
                    
                    self.Ecto_Buy_Instantly_Checkbox.setChecked(True)
                
                else:
                    
                    self.Ecto_Buy_Instantly_Checkbox.setChecked(False)
        
        elif "Dust" in sender.text():
            
            if "Sell Instantly" in sender.text():
                
                if state == 0:
                    
                    self.Dust_List_This_Item_CheckBox.setChecked(True)
                
                else:
                    
                    self.Dust_List_This_Item_CheckBox.setChecked(False)
            
            else:
                
                if state == 0:
                    
                    self.Dust_Sell_Instantly_Checkbox.setChecked(True)
                
                else:
                    
                    self.Dust_Sell_Instantly_Checkbox.setChecked(False)
    
    def Enable_Run_Button(self):
        
        self.Run_Button.setEnabled(True)
    
    def PRINT(self, stuff: str):
        
        print(stuff)

class Signals(QObject):
    
    message = pyqtSignal(str)
    finished = pyqtSignal()
    
    RESULTS = pyqtSignal(tuple)

class Worker(QRunnable):
    
    def __init__(self,
                 salvage_tool, number_of_ectos,
                 ecto_price, dust_price,
                 current_base_MF, current_luck):
        
        super().__init__()
        
        self.signals = Signals()
        
        self.salvage_tool = salvage_tool
        
        if "Crude Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 2.13
            self.dust_per_ecto = 1.47
        elif "Basic Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 3.52
            self.dust_per_ecto = 1.63
        elif "Copper-Fed Salvage-o-Matic" in self.salvage_tool:
            self.salvage_cost_per_ecto = 3.0
            self.dust_per_ecto = 1.63
        elif "Fine Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 11.52
            self.dust_per_ecto = 1.75
        elif "Journeyman's Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 32.0
            self.dust_per_ecto = 1.58
        elif "Runecrafter's Salvage-o-Matic" in self.salvage_tool:
            self.salvage_cost_per_ecto = 30.0
            self.dust_per_ecto = 1.58
        elif "Master's Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 61.44
            self.dust_per_ecto = 1.85
        elif "Silver-Fed Salvage-o-Matic" in self.salvage_tool:
            self.salvage_cost_per_ecto = 60.0
            self.dust_per_ecto = 1.85
        elif "Mystic Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 60.0
            self.dust_per_ecto = 1.85
        elif "Black Lion Salvage Kit" in self.salvage_tool:
            self.salvage_cost_per_ecto = 0.0
            self.dust_per_ecto = 2.04
        
        self.number_of_ectos = number_of_ectos
        
        self.ecto_price = ecto_price
        
        self.dust_price = dust_price
        
        self.current_base_MF = current_base_MF
        
        self.current_luck = current_luck

    def get_item_buy_price(self, item_id: int) -> float:
        """
        Retrieve the buy price of an item from the Guild Wars 2 API.
        
        Args:
            item_id (int): The ID of the item to retrieve the buy price for.
        
        Returns:
            float: The buy price of the item, or None if an error occurs.
        """
        base_url = "https://api.guildwars2.com/v2/commerce/prices"
        params = {"ids": item_id}

        try:
            response = get(base_url, params=params, timeout=10)  # Timeout set to 10 seconds
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

            data = response.json()
            return data[0]["buys"]["unit_price"]  # Accessing the buy price

        except RequestException as e:
            error_pop_up = QMessageBox()
            error_pop_up.setWindowTitle("ERROR")
            error_pop_up.setText(f"Error fetching data for item with ID {item_id}: {e}")
            error_pop_up.setIcon(QMessageBox.Information)
            print(f"Error fetching data for item with ID {item_id}: {e}")
            error_pop_up.exec_()
            return None
    
    def get_item_sell_price(self, item_id: int) -> float:
        """
        Retrieve the sell price of an item from the Guild Wars 2 API.
        
        Args:
            item_id (int): The ID of the item to retrieve the sell price for.
        
        Returns:
            float: The sell price of the item, or None if an error occurs.
        """
        base_url = "https://api.guildwars2.com/v2/commerce/prices"
        params = {"ids": item_id}

        try:
            response = get(base_url, params=params, timeout=10)  # Timeout set to 10 seconds
            response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

            data = response.json()
            return data[0]["sells"]["unit_price"]  # Accessing the sell price

        except RequestException as e:
            error_pop_up = QMessageBox()
            error_pop_up.setWindowTitle("ERROR")
            error_pop_up.setText(f"Error fetching data for item with ID {item_id}: {e}")
            error_pop_up.setIcon(QMessageBox.Information)
            print(f"Error fetching data for item with ID {item_id}: {e}")
            error_pop_up.exec_()
            return None
    
    def calculate_profit(self, ecto_quantity: int) -> tuple:
        """
        Calculate potential profit from buying, salvaging, and selling items.
        
        Args:
            ecto_quantity (int): The quantity of "Glob of Ectoplasm" to buy.
        
        Returns:
            tuple: A tuple containing the potential profit in gold, silver, and copper.
        """
        if self.ecto_price == "BUY":
            ecto_price = self.get_item_buy_price(19721)  # ID for "Glob of Ectoplasm"
        elif self.ecto_price == "SELL":
            ecto_price = self.get_item_sell_price(19721)  # ID for "Glob of Ectoplasm"
        
        ecto_price_gold, ecto_price_silver, ecto_price_copper = self.convert_to_currency(ecto_price)
        
        if self.dust_price == "BUY":
            dust_price = self.get_item_buy_price(24277)  # ID for "Pile of Crystalline Dust"
        elif self.dust_price == "SELL":
            dust_price = self.get_item_sell_price(24277)  # ID for "Pile of Crystalline Dust"
        
        dust_price_gold, dust_price_silver, dust_price_copper = self.convert_to_currency(dust_price)

        if ecto_price is not None and dust_price is not None:

            # Calculate total cost of buying "Glob of Ectoplasm"
            purchase_cost = ecto_quantity * ecto_price

            # Calculate amount of "Pile of Crystalline Dust" obtained by salvaging
            dust_per_ecto_function = lambda x: floor(self.dust_per_ecto * x)
            dust_quantity = dust_per_ecto_function(ecto_quantity)

            # Calculate list price for resultant quantity of "Pile of Crystalline Dust"
            listing_price = dust_quantity * dust_price

            # Calculate cost of salvaging number of purchased "Glob of Ectoplasm"
            total_salvage_cost = ecto_quantity * self.salvage_cost_per_ecto

            # Deduct listing fee (5%) and exchange fee (10%)
            listing_fee = max(1, 0.05 * listing_price)  # Minimum 1 copper
            exchange_fee = max(1, 0.10 * listing_price)  # Minimum 1 copper
            trading_post_fees = listing_fee + exchange_fee

            # Calculate total profit from selling "Pile of Crystalline Dust" after deducting costs
            total_profit = (dust_quantity * dust_price) - \
                (purchase_cost + total_salvage_cost + trading_post_fees)

            total_profit_gold, total_profit_silver, total_profit_copper = self.convert_to_currency(total_profit)
            
            (fine_luck_yield,
            masterwork_luck_yield,
            rare_luck_yield,
            exotic_luck_yield) = self.estimate_luck_yields(ecto_quantity, self.salvage_tool)
            
            (new_base_MF,
             new_luck,
             next_level_luck) = self.estimate_resultant_magic_find_and_luck(fine_luck_yield,
                                                                                  masterwork_luck_yield,
                                                                                  rare_luck_yield,
                                                                                  exotic_luck_yield,
                                                                                  self.current_base_MF,
                                                                                  self.current_luck)

            return (
                total_profit_gold, total_profit_silver, total_profit_copper,
                ecto_price_gold, ecto_price_silver, ecto_price_copper,
                dust_price_gold, dust_price_silver, dust_price_copper,
                fine_luck_yield, masterwork_luck_yield,
                rare_luck_yield, exotic_luck_yield,
                dust_quantity, new_base_MF, new_luck, next_level_luck
                )
        else:
            print("Unable to calculate profit.")
            return None
    
    @staticmethod
    def convert_to_currency(amount: float) -> tuple:
        """
        Convert an amount in copper to gold, silver, and copper.

        Args:
            amount (float): The amount in copper.

        Returns:
            tuple: A tuple containing the amount in gold, silver, and copper.
        """
        gold = amount // 10000
        silver = (amount % 10000) // 100
        copper = ceil(amount % 100)
        return gold, silver, copper
    
    @staticmethod
    def estimate_luck_yields(ecto_quantity: int, salvage_tool: str) -> tuple:
        """
        Parameters
        ----------
        ecto_quantity : int
            The quantity of Ectos the user will be salvaging with a
            selected salvage kit/tool.

        Returns
        -------
        tuple
            Estimated resultant amount of each of the following:
                
                Essence of Luck (fine)
                Essence of Luck (masterwork)
                Essence of Luck (rare)
                Essence of Luck (exotic)
        """
        if "Crude Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 6.77
            masterwork_luck_per_ecto = 0.51
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.01
        elif "Basic Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 7.08
            masterwork_luck_per_ecto = 0.47
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Copper-Fed Salvage-o-Matic" in salvage_tool:
            fine_luck_per_ecto = 7.08
            masterwork_luck_per_ecto = 0.47
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Fine Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 7.47
            masterwork_luck_per_ecto = 0.47
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Journeyman's Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 7.22
            masterwork_luck_per_ecto = 0.49
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Runecrafter's Salvage-o-Matic" in salvage_tool:
            fine_luck_per_ecto = 7.22
            masterwork_luck_per_ecto = 0.49
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Master's Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 7.16
            masterwork_luck_per_ecto = 0.49
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Silver-Fed Salvage-o-Matic" in salvage_tool:
            fine_luck_per_ecto = 7.16
            masterwork_luck_per_ecto = 0.49
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Mystic Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 7.16
            masterwork_luck_per_ecto = 0.49
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        elif "Black Lion Salvage Kit" in salvage_tool:
            fine_luck_per_ecto = 6.88
            masterwork_luck_per_ecto = 0.52
            rare_luck_per_ecto = 0.05
            exotic_luck_per_ecto = 0.02
        
        fine_luck_yield = floor(ecto_quantity * fine_luck_per_ecto)
        masterwork_luck_yield = floor(ecto_quantity * masterwork_luck_per_ecto)
        rare_luck_yield = floor(ecto_quantity * rare_luck_per_ecto)
        exotic_luck_yield = floor(ecto_quantity * exotic_luck_per_ecto)
        
        return (
            fine_luck_yield,
            masterwork_luck_yield,
            rare_luck_yield,
            exotic_luck_yield
            )
    
    @staticmethod
    def estimate_resultant_magic_find_and_luck(fine_lucks: int,
                                               masterwork_lucks: int,
                                               rare_lucks: int,
                                               exotic_lucks: int,
                                               current_base_MF: int,
                                               current_luck: int
                                               ) -> tuple:
        
        # Define the luck values for each essence type
        luck_values = {
            'fine': 10,
            'masterwork': 50,
            'rare': 100,
            'exotic': 200
        }
        
        # Define the maximum level and luck limit
        max_mf_level = 300
        max_luck_limit = 472_510
        
        # Calculate total luck to add
        luck_change = (
            (fine_lucks * luck_values['fine'])
            + (masterwork_lucks * luck_values['masterwork'])
            + (rare_lucks * luck_values['rare'])
            + (exotic_lucks * luck_values['exotic'])
            )
        
        # Initialize new base magic find and luck
        new_base_MF = current_base_MF
        new_luck = current_luck + luck_change
        
        # Process the list of tuples to find the new base magic find level
        for level, required_luck in Magic_Find_Req_Luck_List:
            if level > new_base_MF:
                if new_luck >= required_luck:
                    new_luck -= required_luck
                    new_base_MF = level
                else:
                    break
        
        # Handle the case where the user reaches or exceeds level 300
        if new_base_MF >= max_mf_level:
            new_base_MF = max_mf_level
            next_level_luck = max_luck_limit
        else:
            # Find the required luck for the next level, or set to None if max level is reached
            next_level_luck = max_luck_limit
            for level, required_luck in Magic_Find_Req_Luck_List:
                if level > new_base_MF:
                    next_level_luck = required_luck
                    break
        
        return new_base_MF, new_luck, next_level_luck
        
    @pyqtSlot()
    def run(self):
        
        self.results = self.calculate_profit(self.number_of_ectos)
        
        try:
            self.signals.RESULTS.emit(self.results)
            
            self.signals.finished.emit()
            
        except Exception as e:
            self.signals.message.emit(str(e))

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    
    # Increase the global font size and set font family to Times New Roman
    default_font = app.font()
    default_font.setPointSize(16)
    default_font.setFamily("Times New Roman")
    app.setFont(default_font)
    
    setup_theme()
    
    GUI = GUI()
    GUI.show()
    app.exec()
