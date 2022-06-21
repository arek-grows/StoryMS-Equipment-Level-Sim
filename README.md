# About
This command line app was made for a game mechanic in a certain MapleStory private server. The game mechanic is equipment levelling. All equipment in this game is able to be levelled up, therefore allowing them to have higher stats and making your character more powerful. The stat gain from level ups weren't uniform or predictable so it was easily inferred that there's some sort of formula involved. This formula was not known by the playerbase so a friend scanned through the public source code and found the formula. I then built this app to better understand how the formula affects equipment level ups and to provide a useful analyzation of either what to expect from your equipment or how well your items ended coming out after levelling them. 

# The Formula
```
This formula is for one level up for one stat.

variables:
mod = stat modifier. if the stat is STR, DEX, INT, or LUK then mod=4, for all other stats mod=16
stat = the value of the stat

x = 1 + floor(stat / mod)
y = (x * (x + 1) / 2) + x
z = a random number between 0 and floor(y)

if z < x: 
  the stat is +0 on level up, aka it skips a level
otherwise the stat gains this number on level up:
  1 + floor((-1 + sqrt((8 * (z - x)) + 1)) / 2)

* to floor() means to round down. e.g. floor(9.6) = 9
* the number inside sqrt() is square rooted. e.g. sqrt(4) = 2
* for figuring out Speed and Jump, if the Speed/Jump stat doesn't skip a level, the level up will always be +1

if an item skips all stats on a level up then all the stats are rerolled. this is why items with one stat line never skip levels.
```

# App Features
There are two text files in the folder: "base_equipment.txt" and "levelled_equipment.txt". In "base_equipment.txt", you input the stats of the lv1 equipment you want to simulate. This is required before using the app. "levelled_equipment.txt" is an optional text file to fill out with the equipment you levelled in-game if you want to see how good your levelled equipment came out.

1.
```
[c]reate a new equipment sim from "base_equipment.txt"
```
This takes the stats you input in the relevant text file and simulates the equipment 100,000 times. All the simulations are saved to a file in the data folder. It then shows the 50th percentile (median) for the stats on the equipment. You are then asked if you want to see an analyzation (#2) or return to the main menu.

2.
```
[a]nalyze existing equipment sim
```
Shows all the previously done equipment simulations with their stats and a corresponding number. Type the number to see the 50th percentile of the stats and to choose that equipment for analysis. 

Analysis options:
```
find out what [p]ercentile your equipment's stats fall in
plot the [d]istribution of a specific stat
```
The first option shows the percentiles that the stats in your in-game equipment landed in. "levelled_equipment.txt" is required to be filled out.

The second option takes the simulation numbers and plots them on a plot graph using the Python library matplotlib. You will notice that there is a normal distribution.

```
[r]eset "base_equipment.txt" and "levelled_equipment.txt" to original
```
Resets to stats in the text files to all be 0 for convenience.
