# Guild Wars 2: Cost Estimator of Leveling Magic Find GUI
Python version: 3.9.19

This is a GUI for estimating the cost of leveling one's Magic Find through the most direct route of purchasing Globs of Ectoplasm from the Trading Post, salvaging said Ectos, eating the resultant Luck, and selling the resultant Piles of Crystalline Dust back on the Trading Post. It is designed to provide a reasonable estimate (based on the information from various relevant https://wiki.guildwars2.com/ articles listed below) of said costs as a reflection of CURRENT MARKET CONDITIONS.

Assumptions:
  1) The user will salvage 100% of the Globs of Ectoplasm they purchase from the Trading Post.
  2) The user will sell 100% of the resultant Piles of Crystalline Dust back to the Trading Post.
  3) Any Buy/Sell orders made buy the user will successfully buy/sell without the need for re-listing.

# Relevant Wiki Articles
Glob of Ectoplasm/salvage research:
https://wiki.guildwars2.com/wiki/Glob_of_Ectoplasm/salvage_research

Luck:
https://wiki.guildwars2.com/wiki/Luck

Salvage Kits:
https://wiki.guildwars2.com/wiki/Salvage_kit

# Why does this exist?
My attempts to rapidly level my magic find stat taught me that the net cost of said process can vary wildly (up to 30 gold of difference in my experience) depending on contemporaneous market conditions and the tools used. My initial solution to estimate net cost was a hard-coded python script, but once I maxed out my magic find stat I thought there's a chance someone else might find this code useful. The result is a GUI that is (hopefully) intuitive and helpful for others who find themselves in the same situation I did.

# Instructions
For those skeptical of running a random .exe from the internet, GOOD! You should always be skeptical of such a thing. For you, here is the first method. The .exe is still available, and I will explain how to access it later.

Step 1: Download Python

    Go to this website: https://www.python.org/downloads/windows/
    and download Python 3.11.10 - Sept. 7, 2024
    ![image](https://github.com/user-attachments/assets/48fe1946-47e1-4405-b06f-775814370d2d)

