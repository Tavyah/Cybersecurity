##Oppgave Straba
Note: The challenge solution does not involve finding any people/locations from the visuals of the picture. You can treat all the pictures as if they are all ai generated. (A few pictures turned out to be real, this is not part of the solution. The author has been bonked with a stick for their crimes.)

We are looking for location of some soldiers. We have received a tip-off that they use Straba to post their runs. However, Straba has a policy of not disclosing any information, so we have to see if we can find something ourselves. Go to straba.hkn and see if you can find anything in the images.

The flag is the name of the city near the military base they are at.

Solution: 
Go into the website provided
Find the soldiers that you think we are trying to sniff
Take a look at the picture, open in normal picture viewer and I can't find anything special
So i will try to look at the meta data using srch_strings 

Commando srch_strings <picture>

Alot of output, but all the way on the top of the output, u can see a GPS cooridnate
Put it into google maps and u will see that the closest military base is skrydstrup

FLAG: DDC{skrydstrup}