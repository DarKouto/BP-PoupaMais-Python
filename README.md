# BP-PoupaMais-Python
A discount calculator for Gas, now made with Python

My first (small and humble) Python project, after just reading a few documents regarding this language. It's the same as the JS one, but in Python. I always found this programming languague to be very interesting, so I decided to learn a few things and test it out.

![Honest Work](https://i.kym-cdn.com/entries/icons/mobile/000/028/021/work.jpg)

## The Problem this solves
BP had a partnership with Pingo Doce which provided gas discounts (through a Pingo Doce card).<br/>
Example: you spent 25€ in gas, and you had 5€ bonus on the card. So at the end you would only pay 20€.<br/>
However, the discount could only be applied if at least 20 liters where pumped into a veihicle.<br/>
Unfortunately my motorcycle only fits 14 liters, rendering this whole promotion discount invalid.<br/>

The Solution? Get another person with another bike, go to the gas station at the same time, and pump gas into both motorcyles as if it was only one, therefore breaking the 20 liters threshold.<br/>
The Problem? We get the discount, but now we don't know how much the each one of us has to pay, especially after the discount.<br/>
This app solves this problem, it asks how much Driver 1 pumped in €, asks the total value of the bill without the discount, and the value with the discount, then it proceeds to calcultate the percentages of each one and how much each owes in €.

## How to use
 - Download the bp.py file to your machine
 - Open a terminal in the same directory as the bp.py file and type:
```
python bp.py
```
