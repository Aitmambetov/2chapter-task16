"""
If you were on the moon now, your weight will be 16,5% of your earth weight.
To calculate it you have to multiple to 0,165. If next 15 years your weight will
increase 1 kg each year. What will be your weight each year on the moon next
15 years?
"""

earth_w = float(input('введите Ваш вес на земле '))
year = 0
while year < 15:
    earth_w += 1.0
    print((earth_w)*0.165)
    year += 1


