# Guild Wars 2: Cost Estimator of Leveling Magic Find GUI
Python version: 3.11.10

This is a GUI for estimating the cost of leveling one's Magic Find through the most direct and time-efficient method of purchasing Globs of Ectoplasm from the Trading Post, salvaging said Ectos, eating the resultant Luck, and selling the resultant Piles of Crystalline Dust back on the Trading Post. It is designed to provide a reasonable estimate (based on the information from various relevant https://wiki.guildwars2.com/ articles listed below) of said costs as a reflection of CURRENT MARKET CONDITIONS.

Non-exhaustive testing has so far determined the GUI's predictions regarding the net cost of the process are accurate to within +/- 1%.

Assumptions:
  1) The user will salvage 100% of the Globs of Ectoplasm they purchase from the Trading Post.
  2) The user will sell 100% of the resultant Piles of Crystalline Dust back to the Trading Post.
  3) Any Buy/Sell orders made buy the user will successfully buy/sell without the need for re-listing.

Disclaimer:
Please understand that a perfect prediction simply is not possible. I have used the research compiled by dozens of users (see the Relevant Wiki Articles section below) to inform my code, but such values have been derived from the combined results of thousands of data points. Such values will most likely continue to be accurate when working with a significant quantity of ectos, but will most likely become increasingly innacurate as the user works with smaller and smaller quantities of resources. This is not to be taken as an admonishmnet to only use this GUI if you're comfortable purchasing hundreds of ectos at a time, but rather that the risks of using this method AT ALL to level your Magic Find should be considered before you put any of your hard-earned gold at risk. Always determine how much gold your are comfortable putting at risk before using this method, and to quote GW2 YouTuber Abree: "If you can't afford to go that long without the gold, that's a sign the cost or risk was too high for you." (https://youtu.be/9-cn9Wa9agQ?si=MMYQgCuHWDGR72z6 @7:41)

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

  Go to the Microsoft Store and download Python 3.11 [I know this is technically version 3.11.9, but it works regardless]: https://www.microsoft.com/store/productId/9NRWMJP3717K?ocid=pdpshare
  ![image](https://github.com/user-attachments/assets/97e585b1-7c25-40ab-888e-cd501f8d2194)
