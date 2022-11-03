from datetime import datetime

today_is = str(datetime.now()).split()[0].split("-")


date_is = input("Enter DOB:(yyyy-mm-dd)>  ").split("-")
print(date_is)


if int(date_is[0]) < int(today_is[0]) and date_is[1] < "13" and date_is[2] <= "31":
    y = int(today_is[0]) - int(date_is[0])
    m = int(today_is[1]) - int(date_is[1])
    d = int(today_is[2]) - int(date_is[2])
    if d < 0:
        d = 31 + d

    if int(today_is[1]) <= int(date_is[1]):
        # checki
        m = int(today_is[1])

    print(f"You are {y} years, {m} months and {d} days")
