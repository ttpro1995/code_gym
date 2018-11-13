__author__ = "Thai Thien"
__link__ = "https://app.codesignal.com/challenge/5gPLgp4nMtMHZ8JJF"

from datetime import datetime


def clockHandAngle(time):
    """
    main function of code signal
    :param time: as string
    :return: angle (in degrees) between the hour and minute hands
    """

    # parse to datetime object
    date = datetime.strptime(time, '%H:%M:%S')

    hour = date.hour
    minute = date.minute
    second = date.second

    if hour >= 12:
        hour -= 12

    second_per_day = 86400/2
    second_per_hour = 3600

    second_pass = hour * 60 * 60 + minute * 60 + second
    second_pass_minute = minute * 60 + second

    result_hour = second_pass * 360 / second_per_day
    result_minute = second_pass_minute * 360 / second_per_hour

    result1 = abs(result_hour - result_minute)
    result2 = 360 - result1

    if result1 < result2:
        return result1
    else:
        return result2


if __name__ == "__main__":
    print(clockHandAngle("12:00:00"))
    print(clockHandAngle("2:00:00"))
    print(clockHandAngle("2:05:30"))