# Guild Wars 2: Net Cost Estimator of Leveling Magic Find GUI
Python version: 3.11.10

This is a GUI for estimating the net cost of leveling one's Magic Find through the most direct and time-efficient method of purchasing Globs of Ectoplasm from the Trading Post, salvaging said Ectos, eating the resultant Luck, and selling the resultant Piles of Crystalline Dust back on the Trading Post. It is designed to provide a reasonable estimate (based on the information from various relevant https://wiki.guildwars2.com/ articles listed below) of said costs as a reflection of CURRENT MARKET CONDITIONS.

![image](https://github.com/user-attachments/assets/094da13b-e213-4bd2-a360-acce9646634b)

Non-exhaustive testing has so far determined the GUI's predictions regarding the net cost of the process are accurate to within +/- 1%. Though it is anecdotal, the hard-coded python script that predates this GUI and used the same logic/math returned results with similar accuracy.

![image](https://github.com/user-attachments/assets/21fc3b05-b724-4c27-b592-a4a878cf6869)

Assumptions:
  1) The user will salvage 100% of the Globs of Ectoplasm they purchase from the Trading Post.
  2) The user will sell 100% of the resultant Piles of Crystalline Dust back to the Trading Post.
  3) Any Buy/Sell orders made buy the user will successfully buy/sell without the need for re-listing.

**Disclaimer:**

Please understand that a perfect prediction simply is not possible. I have used the research compiled by dozens of users (see the Relevant Wiki Articles section below) to inform my code, but such values have been derived from the combined results of thousands of data points. Such values will most likely continue to be accurate when working with a significant quantity of ectos, but will most likely become increasingly innacurate as the user works with smaller and smaller quantities of resources. This is not to be taken as an admonishment to only use this GUI if you're comfortable purchasing hundreds of ectos at a time, but rather that the risks of using this method AT ALL to level your Magic Find should be considered before you put any of your hard-earned gold at risk. Always determine how much gold your are comfortable putting at risk before using this method, and to quote GW2 YouTuber Abree in his video about flipping: "If you can't afford to go that long without the gold, that's a sign the cost or risk was too high for you." (https://youtu.be/9-cn9Wa9agQ?si=MMYQgCuHWDGR72z6 @7:41)

# Relevant Wiki Articles
Glob of Ectoplasm/salvage research:
https://wiki.guildwars2.com/wiki/Glob_of_Ectoplasm/salvage_research

Luck:
https://wiki.guildwars2.com/wiki/Luck

Salvage Kits:
https://wiki.guildwars2.com/wiki/Salvage_kit

**Art Assets taken from the Wiki**

Glob of Ectoplasm Icon: https://wiki.guildwars2.com/wiki/Glob_of_Ectoplasm#/media/File:Glob_of_Ectoplasm.png

Pile of Crystalline Dust Icon: https://wiki.guildwars2.com/wiki/Pile_of_Crystalline_Dust#/media/File:Pile_of_Crystalline_Dust.png

Gold Coin Icon: https://wiki.guildwars2.com/wiki/Coin#/media/File:Gold_coin_(highres).png

Silver Coin Icon: https://wiki.guildwars2.com/wiki/Coin#/media/File:Silver_coin_(highres).png

Copper Coin Icon: https://wiki.guildwars2.com/wiki/Coin#/media/File:Copper_coin_(highres).png

Essence of Luck (fine) Icon: https://wiki.guildwars2.com/wiki/Essence_of_Luck_(fine)#/media/File:Essence_of_Luck_(fine).png

Essence of Luck (masterwork) Icon: https://wiki.guildwars2.com/wiki/Essence_of_Luck_(masterwork)#/media/File:Essence_of_Luck_(masterwork).png

Essence of Luck (rare) Icon: https://wiki.guildwars2.com/wiki/Essence_of_Luck_(rare)#/media/File:Essence_of_Luck_(rare).png

Essence of Luck (exotic) Icon: https://wiki.guildwars2.com/wiki/Essence_of_Luck_(exotic)#/media/File:Essence_of_Luck_(exotic).png

Net Loss (Red Arrow) Icon: https://wiki.guildwars2.com/wiki/Category:Guild_upgrade_icons#/media/File:Research_Art_of_War_Level_1.png

Net Profit (Green Arrow) Icon: https://wiki.guildwars2.com/wiki/Category:Guild_upgrade_icons#/media/File:Research_Architecture_Level_1.png

Placeholder Icon: https://wiki.guildwars2.com/wiki/Category:ArenaNet_logos#/media/File:User_Fey_Zeal_Gw2wlogo.png

# GitHub Page of the PyQt5 LED I used in this project
https://github.com/nlamprian/pyqt5-led-indicator-widget

# Why does this exist?
My attempts to rapidly level my magic find stat taught me that the net cost of said process can vary wildly (up to 30 gold of difference in my experience) depending on contemporaneous market conditions and the tools used. My initial solution to estimate net cost was a hard-coded python script, but once I maxed out my base magic find stat I thought there's a chance someone else might find this code useful. The result is a GUI that is (hopefully) intuitive and helpful for others who find themselves in the same situation I did.

# Installation Instructions (Method 1: Pure python, non-exe)
For those skeptical of running a random .exe from the internet, GOOD! You should always be skeptical of such a thing. For you, here is the first method. The .exe is still available, and I will explain how to access it later.

At some point in the process you might get a Windows pop-up telling you that python is trying to access the internet, and asking you to determine its network permissions (e.g. Home, Public, Workplace). Select whatever you're most comfortable with, though in general I wouldn't recommend "Public" or "Workplace".

**Step 1: Download Python**

  Go to the Microsoft Store and download Python 3.11 [I know this is technically version 3.11.9, but it works regardless]: https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare
  ![image](https://github.com/user-attachments/assets/97e585b1-7c25-40ab-888e-cd501f8d2194)

**Step 2: Download Code**

  First click on this green "Code" button at the top of the page, which should open a drop-down menu:
  
  ![image](https://github.com/user-attachments/assets/3e9c9da6-0aba-4922-8d89-daccda208225)

  Then, click on the option that says "Download ZIP":
  
  ![image](https://github.com/user-attachments/assets/886aadcc-d8fe-4760-8a39-0a164030862c)

  You should now see a zip folder in your "Downloads" folder:

  ![image](https://github.com/user-attachments/assets/0e698905-4491-403b-9ad6-9a4dbbfc832d)

**Step 3: Extract Files**

  Move that zip folder into whatever folder you wish on your computer, though I recommend creating one that is easy to access (e.g. "Documents\GW2_GUI").

  Once you have done that, right-click the file and select "Extract All". A pop-up will appear letting you know where the files will be extracted to, so just ensure they're going where you expect.

**Step 4: Running "Run_Set_Up.bat" File**

  Once you have your files where you want them, you'll need to run the file "Run_Set_Up.bat". Running this will tell the version of python you installed earlier to run the file "Set_Up.py" which will automatically install the pyhton libraries necessary to run the GUI, listed here (you don't have to do anything with these links, I'm just providing them for maximum transparency):

  PyQt5 (https://pypi.org/project/PyQt5/)
  
  pyqtdarktheme (https://pypi.org/project/pyqtdarktheme/)
  
  numpy (https://pypi.org/project/numpy/)
  
  requests (https://pypi.org/project/requests/)

  Once you run it, you will most likely see this pop-up or something like it appear:

  ![image](https://github.com/user-attachments/assets/c704437f-c20d-41a3-8217-c2994524387b)

  This is just Windows saying it doesn't recognize the file and it thinks it might be malware or a virus or something. You can just click "More Info" and then "Run Anyway":

  ![image](https://github.com/user-attachments/assets/d278e24d-735d-4148-8a74-3085a4c7fcb4)

  Once you do, you'll see a command prompt window appear which will give you information about the library installation process, which will look something like this:

  ![image](https://github.com/user-attachments/assets/be678844-6c83-4325-b5ba-a4a71d857628)

  You'll know it's done because a line will appear saying "Press any key to continue . . ."

  Then just hit any key like it says and the window will close.

**Step 5: Running "Launch_GUI.bat" File**

  Now we can actually launch the GUI! All you have to do is run "Launch_GUI.bat" and after a few seconds the GUI should appear!

  You might get another pop-up from Windows warning you it doesn't recognize the file; same advice goes this time as last time.

# Installation Instructions (Method 2: .exe File made using PyInstaller)

"Are you joking? I'm not doing all that! Just give me the file already!"

Ok, first click on this section:

![image](https://github.com/user-attachments/assets/1a177672-37cf-40fb-a847-3affdf20d3ad)

Then click on this link, which should download a zip file:

![image](https://github.com/user-attachments/assets/5dae2f8d-43ee-4260-9b27-b7710468102b)

You should now see the file in your downloads folder:

![image](https://github.com/user-attachments/assets/c135b4d3-9731-43d4-8e62-9ea361eae6c8)

Next, you can just follow the same instructions in "Step 3: Extract Files".

Once the files are in the folder where you want them and have been extracted, you should see this:

![image](https://github.com/user-attachments/assets/a8975a1b-5835-4e08-b8cc-44a792616423)

Now just run (double-click) the file "Luck_Boost_Profitability_GUI.exe"!

You will get a Windows pop-up like those discussed earlier, just follow the same steps I layed out for dealing with those.

At some point in the process you might get a Windows pop-up telling you that python is trying to access the internet, and asking you to determine its network permissions (e.g. Home, Public, Workplace). Select whatever you're most comfortable with, though in general I wouldn't recommend "Public" or "Workplace".

# How to Use the GUI

Here are your inputs, a.k.a. the things with which you interact:

![image](https://github.com/user-attachments/assets/b9a243c5-2006-46e4-8e41-784471619a79)

And here are the outputs, a.k.a. the results of your inputs and the resultant information from both data retrieved from the GW2 API and values calculated by the GUI:

![image](https://github.com/user-attachments/assets/126e9973-8b18-41e0-bdf8-4ebfbcc6cac8)

This is just a Green/Red LED that will let you know (along with a pop-up when the GUI launches) whether or not the GW2 API is down [GREEN means it's up, RED means it's down]. If the API is down, THE ENITRE GUI WILL NOT WORK:

![image](https://github.com/user-attachments/assets/40537633-5ff4-44c9-9862-ec9b8b8ed710)

And here is the button you press to run everything once you have configured your inputs:

![image](https://github.com/user-attachments/assets/83997dec-915d-4810-a125-c887b0f92184)

**Inputs**

This section is where you select which salvage kit or salvage tool you plan on using to salvage the ectos you plan on buying. "CpU" stands for "Copper per Use" and means how many copper each of the listed options cost PER USE (either on a per use basis for the gem-store versions or as a function of their purhcase price for the others), and "DpE" stands for "Dust per Ecto" which means (ROUGHLY) how many Piles of Crystalline Dust you can expect per ecto salvaged. The Black Lion Salvage Kit is a bit weird because it can only be purchased with gems or through other non-coin equivalents, so in the end I just decided to treat it as if it doesn't have a cost for using it, but it should be obvious that Black Lion Salvage Kits are not easy to acquire. If you're even considering using them for getting luck and dust from ectos, you either have literally nothing better to use them for or are so rich in-game that you can afford to blow a resource like that on leveling your magic find stat:

![image](https://github.com/user-attachments/assets/3f0c8a65-22ee-4f6e-a990-2cbe87c38a9a)

This is just where you tell the GUI how many ectos you plan on purchasing, capped at 250 because that is the most the game will let you purchase from the Trading Post at once. It is up to you to use the Trading Post to find out how many you can afford, and how many are actually available at the given price (if instant-buying), the GUI will not do that for you:

![image](https://github.com/user-attachments/assets/38dc4cd1-df18-42a1-8ee8-e76f89a193bc)

If you want a prediction of what your magic find stat and luck will be at the end of the transaction, use these fields; if you don't care, you can leave them as-is. To find these values, check the bottom-right corner of your in-game "Achievements" panel. The first is capped at 300, which is the highest you can raise your magic find stat solely through consuming luck. The second is capped at 472,510 which is as high at it goes. Keep in mind that you can absolutely enter combinations of magic find and luck that are not possible in-game, so it is on you to enter the values correctly:

![image](https://github.com/user-attachments/assets/6a1999fa-00f0-4d80-a6fc-aa95100eecbb)

This is where you tell the GUI whether you want to purchase ectos through buy orders or instant-buying. The price you see updates automatically because the GUI fetches it from the GW2 API when you check or un-check a box, so just check the box to the left of the option you're going to use:

![image](https://github.com/user-attachments/assets/daef43a5-4fee-4aba-9d14-5e1dd11c3e04)

And this is where you tell the GUI how you will sell your resultant Piles of Crystalline Dust back to the Trading Post, either through listing them or instant-selling. Again, the price you see updates automatically because the GUI fetches it from the GW2 API when you check or un-check a box, so just check the box to the left of your chosen option.

![image](https://github.com/user-attachments/assets/1333950e-2d2b-44b7-965d-af8b99743a1d)

**Outputs**

Here, I have run an example scenario to illustrate how the outputs work. Let's say I want to purchase 50 ectos via buy order, I'm going to salvage them with the Silver-Fed Salvage-o-Matic, my starting magic find is 10 and my starting luck is 150:

![image](https://github.com/user-attachments/assets/abc1cf1a-2f55-4936-bdab-ad3fea737047)

This is where the GUI tells me how many of each Essence of Luck rarity and dusts I can reasonably expect from this process:

![image](https://github.com/user-attachments/assets/3ffe9bd0-c1b8-40bc-8b9e-724d7fb4dc76)

This is where the GUI tells me what my magic find and luck progress will be after eating all those Essences of Luck:

![image](https://github.com/user-attachments/assets/3901751b-7f1c-4fcb-9650-f1355b0f4aa5)

Finally, this is where the GUI tells me what I can expect the net profit of this whole endeavor to be:

![image](https://github.com/user-attachments/assets/85b7b625-9c09-4b78-ad55-616c656d42a6)

You might notice that downwards-facing red arrow next to the numerical profit. That is a visual indicator I provided, in addition to the minus sign in the numeric gold field, to indicate that the net result will be a loss compared to your starting amount of gold. There is technically a green arrow as well that appears if the GUI thinks you will actually profit from one of these transactions:

![image](https://github.com/user-attachments/assets/ccb5d767-4ed8-4342-88ff-a502b2930158)

but please DO NOT expect to ever actually make gold while doing this. I can only ever get that green arrow to appear if I specify using a Black Lion Salvage Kit, which is dubious given my earlier statements about how I deliberately neglected the kit's cost per use. You MIGHT occasionally get lucky and actually turn a profit while doing this, but that never once happened to me.
