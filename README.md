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

# Why does this exist?
My attempts to rapidly level my magic find stat taught me that the net cost of said process can vary wildly (up to 30 gold of difference in my experience) depending on contemporaneous market conditions and the tools used. My initial solution to estimate net cost was a hard-coded python script, but once I maxed out my magic find stat I thought there's a chance someone else might find this code useful. The result is a GUI that is (hopefully) intuitive and helpful for others who find themselves in the same situation I did.

# Installation Instructions (Method 1: Pure python, non-exe)
For those skeptical of running a random .exe from the internet, GOOD! You should always be skeptical of such a thing. For you, here is the first method. The .exe is still available, and I will explain how to access it later.

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

  You might get another pop-up from Windows warning you it doesn't recognize the file. Same advice goes this time as last time.

# Installation Instructions (Method 2: .exe File)

"Are you joking? I'm not doing all that! Just give me the file already!"

Ok, first click on this section:
