def which_day(year, month, day):
    """
    Returns the day of the week that falls on the given date
    1 January 1 AD was a MONDAY
    Sept, Apr, June and Nov have 30 days
    {Jan: 31, Feb: 28, Mar: 31, Apr: 30, May: 31, Jun: 30, Jul: 31, Aug: 31,
    Sep: 30, Oct: 31, Nov: 30, Dec: 31}
    If you take Feb 1st into consideration, it is after 31 days from the start of the year
    7*4+3, i.e. Feb 1 is 3 days ahead of Jan 1. So, if Jan 1 is Mon, then Feb 1 is Thur
    So, we build an array with these margins
    t = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]

    Every normal year has 52 weeks plus 1 day. So, each year shifts the starting day by 1 day
    (y + y/4 - y/100 + y/400 + t[m-1] + d) % 7
    """
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    # if month is less than 3 reduce year by 1
    if (month < 3):
        year = year - 1

    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7


if __name__ == '__main__':
    date = input("Enter date in this format: yyyy,mm,dd: ")
    date = date.split(',')
    date = [int(x) for x in date]
    year, month, day = date
    print(which_day(year, month, day))
