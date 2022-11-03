time = input("Enter time H:MM:AM/PM >> ").lower().split(":")
print(time)


def time_of_day():
    if time[2] == "am":
        print("Good morning")
    elif time[2] == "pm":
        print("Good Night")
    else:
        print("Wrong input")


time_of_day()
