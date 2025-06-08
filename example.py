import tz_data

print(tz_data.lookup("Atlantic/Reykjavik"))       # -> GMT0
print(tz_data.lookup("atlantic/south_georgia"))   # -> <-02>2
print(tz_data.lookup("invalid/zone"))             # -> None
