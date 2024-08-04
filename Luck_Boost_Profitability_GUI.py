# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:36:44 2024

@author: Asher
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
    QFrame
    )
from qdarktheme import setup_theme
from numpy import floor, ceil
# import requests
from requests import get, RequestException

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
        self.Prompt_User_Salveage_Tool_and_Amount_of_Ectos_Label = QLabel("Please select Salvage Tool and enter Number of Ectos to purchase:")
        self.Current_Dust_TP_Price_Label = QLabel("Current Pile of Crystalline Dust Trading Post Price:")
        self.Current_Ecto_TP_Price_Label = QLabel("Current Glob of Ectoplasm Trading Post Price:")
        self.Total_Profit_Label = QLabel("TOTAL PROFIT:")
        
        """
        Glob of Ectoplasm/Pile of Crystalline Dust Icons
        """
        self.Glob_of_Ectoplasm_Label = QLabel()
        self.Glob_of_Ectoplasm_Image = QPixmap("Glob_of_Ectoplasm.png")
        self.Glob_of_Ectoplasm_Image = self.Glob_of_Ectoplasm_Image.scaled(50, 50, aspectRatioMode=True)
        self.Glob_of_Ectoplasm_Label.setPixmap(self.Glob_of_Ectoplasm_Image)
        
        self.Pile_of_Crystalline_Dust_Label = QLabel()
        self.Pile_of_Crystalline_Dust_Image = QPixmap("Pile_of_Crystalline_Dust.png")
        self.Pile_of_Crystalline_Dust_Image = self.Pile_of_Crystalline_Dust_Image.scaled(50, 50, aspectRatioMode=True)
        self.Pile_of_Crystalline_Dust_Label.setPixmap(self.Pile_of_Crystalline_Dust_Image)
        
        """
        Profit/Loss/Placeholder Icons
        """
        self.Profit_Image = QPixmap("Profit.png")
        self.Scaled_Profit_Image = self.Profit_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Loss_Image = QPixmap("Loss.png")
        self.Scaled_Loss_Image = self.Loss_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Placeholder_Image = QPixmap("User_Fey_Zeal_Gw2wlogo.png")
        self.Scaled_Placeholder_Image = self.Placeholder_Image.scaled(50, 50, aspectRatioMode=True)
        
        self.Flexible_Label = QLabel()
        self.Flexible_Label.setPixmap(self.Scaled_Placeholder_Image)
        
        """
        Coin Icons
        """
        # Gold
        self.Gold_Coin_Label_1 = QLabel()
        self.Gold_Coin_Image_1 = QPixmap("Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_1 = self.Gold_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_1.setPixmap(self.Scaled_Gold_Coin_Image_1)
        
        self.Gold_Coin_Label_2 = QLabel()
        self.Gold_Coin_Image_2 = QPixmap("Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_2 = self.Gold_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_2.setPixmap(self.Scaled_Gold_Coin_Image_2)
        
        self.Gold_Coin_Label_3 = QLabel()
        self.Gold_Coin_Image_3 = QPixmap("Gold_coin_(highres).png")
        self.Scaled_Gold_Coin_Image_3 = self.Gold_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Gold_Coin_Label_3.setPixmap(self.Scaled_Gold_Coin_Image_3)
        
        # Silver
        self.Silver_Coin_Label_1 = QLabel()
        self.Silver_Coin_Image_1 = QPixmap("Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_1 = self.Silver_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_1.setPixmap(self.Scaled_Silver_Coin_Image_1)
        
        self.Silver_Coin_Label_2 = QLabel()
        self.Silver_Coin_Image_2 = QPixmap("Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_2 = self.Silver_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_2.setPixmap(self.Scaled_Silver_Coin_Image_2)
        
        self.Silver_Coin_Label_3 = QLabel()
        self.Silver_Coin_Image_3 = QPixmap("Silver_coin_(highres).png")
        self.Scaled_Silver_Coin_Image_3 = self.Silver_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Silver_Coin_Label_3.setPixmap(self.Scaled_Silver_Coin_Image_3)
        
        # Copper
        self.Copper_Coin_Label_1 = QLabel()
        self.Copper_Coin_Image_1 = QPixmap("Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_1 = self.Copper_Coin_Image_1.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_1.setPixmap(self.Scaled_Copper_Coin_Image_1)
        
        self.Copper_Coin_Label_2 = QLabel()
        self.Copper_Coin_Image_2 = QPixmap("Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_2 = self.Copper_Coin_Image_2.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_2.setPixmap(self.Scaled_Copper_Coin_Image_2)
        
        self.Copper_Coin_Label_3 = QLabel()
        self.Copper_Coin_Image_3 = QPixmap("Copper_coin_(highres).png")
        self.Scaled_Copper_Coin_Image_3 = self.Copper_Coin_Image_3.scaled(50, 50, aspectRatioMode=True)
        self.Copper_Coin_Label_3.setPixmap(self.Scaled_Copper_Coin_Image_3)
        
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
        
        """
        Salvage Tool/Number of Ectos to Buy Layer
        """
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer = QHBoxLayout()
        
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Salvage_Tool_Select)
        self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer.addWidget(self.Number_of_Ectos_to_Buy)
        
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
        Current Pile of Crystalline Dust Trading Post Price
        """
        self.Current_Dust_TP_Price_Layout = QHBoxLayout()
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Pile_of_Crystalline_Dust_Label)
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Gold_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Gold_Coin_Label_3)
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Silver_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Silver_Coin_Label_3)
        
        self.Current_Dust_TP_Price_Layout.addWidget(self.Dust_Copper_Price_Field)
        self.Current_Dust_TP_Price_Layout.addWidget(self.Copper_Coin_Label_3)
        
        """
        Current Glob of Ectoplasm Trading Post Price
        """
        self.Current_Ecto_TP_Price_Layout = QHBoxLayout()
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Glob_of_Ectoplasm_Label)
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Gold_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Gold_Coin_Label_2)
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Silver_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Silver_Coin_Label_2)
        
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Ecto_Copper_Price_Field)
        self.Current_Ecto_TP_Price_Layout.addWidget(self.Copper_Coin_Label_2)
        
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
        Visual Dividers
        """
        self.Frame_1 = QFrame()
        self.Frame_1.setFrameShape(QFrame.StyledPanel)
        self.Frame_1_Layout = QVBoxLayout()
        self.Frame_1.setLayout(self.Frame_1_Layout)
        self.Frame_1_Layout.addWidget(self.Prompt_User_Salveage_Tool_and_Amount_of_Ectos_Label)
        self.Frame_1_Layout.addLayout(self.Salvage_Tool_Number_of_Ectos_to_Buy_Layer)
        
        self.Frame_2 = QFrame()
        self.Frame_2.setFrameShape(QFrame.Panel)
        self.Frame_2_Layout = QVBoxLayout()
        self.Frame_2.setLayout(self.Frame_2_Layout)
        self.Frame_2_Layout.addWidget(self.Current_Ecto_TP_Price_Label)
        self.Frame_2_Layout.addLayout(self.Ecto_Place_Order_or_Buy_Instantly_Layout)
        self.Frame_2_Layout.addLayout(self.Current_Ecto_TP_Price_Layout)
        
        self.Frame_3 = QFrame()
        self.Frame_3.setFrameShape(QFrame.Panel)
        self.Frame_3_Layout = QVBoxLayout()
        self.Frame_3.setLayout(self.Frame_3_Layout)
        self.Frame_3_Layout.addWidget(self.Current_Dust_TP_Price_Label)
        self.Frame_3_Layout.addLayout(self.Dust_Sell_Instantly_or_List_This_Item_Layout)
        self.Frame_3_Layout.addLayout(self.Current_Dust_TP_Price_Layout)
        
        self.Frame_4 = QFrame()
        self.Frame_4.setFrameShape(QFrame.StyledPanel)
        self.Frame_4_Layout = QVBoxLayout()
        self.Frame_4.setLayout(self.Frame_4_Layout)
        self.Frame_4_Layout.addWidget(self.Total_Profit_Label)
        self.Frame_4_Layout.addLayout(self.Profit_Layout)
        
        """
        GUI Layout
        """
        # Overall Layout
        self.GUI_Layout = QVBoxLayout()
        
        # Salvage Tool/Number of Ectos Stuff
        self.GUI_Layout.addWidget(self.Frame_1)
        
        # Ecto Related Stuff
        self.GUI_Layout.addWidget(self.Frame_2)
        
        # Dust Related Stuff
        self.GUI_Layout.addWidget(self.Frame_3)
        
        # Profit Related Stuff
        self.GUI_Layout.addWidget(self.Frame_4)
        
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
        
        # Spool up multithreaded worker
        self.worker = Worker(
            self.Salvage_Tool,
            self.Number_of_Ectos,
            self.Ecto_Price,
            self.Dust_Price
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
        
        Gold_Profit = str(results[0])
        Silver_Profit = str(results[1])
        Copper_Profit = str(results[2])
        
        Ecto_Price_Gold = str(results[3])
        Ecto_Price_Silver = str(results[4])
        Ecto_Price_Copper = str(results[5])
        
        Dust_Price_Gold = str(results[6])
        Dust_Price_Silver = str(results[7])
        Dust_Price_Copper = str(results[8])
        
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
    
    def __init__(self, salvage_tool, number_of_ectos, ecto_price, dust_price):
        
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
            print(f"Error fetching data for item with ID {item_id}: {e}")
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
            print(f"Error fetching data for item with ID {item_id}: {e}")
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

            return (
                total_profit_gold, total_profit_silver, total_profit_copper,
                ecto_price_gold, ecto_price_silver, ecto_price_copper,
                dust_price_gold, dust_price_silver, dust_price_copper
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
