In this step you have to make the analog clock work and show the current time.

You have make use of the `Date` object of JavaScript to access the current Time. Once you have the hours, minute and second as integers; We have to now work on rotating the hands.

### Hour hand

hour value will lie in between 0 - 12. To convert it into degrees We will multiply it by 30 (as 30 \* 12 = 360) But this will make it instantly move 30deg every hour (not smooth). To fill those 30 degrees we can use the minute value (60 minutes in an hour so we can get 30 by dividing 60 by 2, adding this will move the hour hand half degree every minute)

```
hour * 30 + (minute / 2) deg
```

Similarly find formulas for Minute and Second hand.
