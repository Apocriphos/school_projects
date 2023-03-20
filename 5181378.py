def function(a_0548):
    week_0548 = 0
    while a_0548 > 75:
        a_0548 = a_0548-(a_0548/100*1.5)
        week_0548 = week_0548 + 1
        if a_0548 < 75:
            break
    return print("To get", a_0548, "kilograms it takes", week_0548, "weeks")

function(287)