import time
print("მაღვიძარა")
x1 = True
while x1:
    wami = int(input("შეიყვანეთ წამი : "))
    if -1 < wami < 60:
        x1 = False
while not x1:
    wuti = int(input("შეიყვანეთ წუთი : "))
    if -1 < wuti < 60:
        x1 = True
while x1:
    saati1 = int(input("შეიყვანეთ საათი : "))
    if saati1 > -1:
        x1 = False

my_time = (saati1*3600)+(wuti*60)+wami

for x in range(my_time, 0, -1):
    wamebi = x % 60
    wutebi = int(x/60) % 60
    saati = int(x/3600)
    print(f"{saati:02}:{wutebi:02}:{wamebi:02}")
    time.sleep(1)
print("გაიღვიძე")