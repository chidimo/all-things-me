# Python technical interview questions (and possibly answers)

1. Find the number of swapping operations needed to sort numbers `8, 22, 7, 9, 31, 19, 5, 13` in ascending order using bubble sort. `(Options: 11, 12, 13, 14)`

```python
def bubbleSort(alist):
    """Sort a list of numbers using bubble sort"""
    swap_count = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swap_count += 1
    print("Number of swaps: ", swap_count)

bubbleSort([8, 22, 7, 9, 31, 19, 5, 13])
```

1. How many four digit whole numbers `'n'` are possible such that the last four digits of `n^2` are in fact the original number `'n'`. `(Options: 0, 1, 2, 3)`

```python
# Last four digits
def count_four_digit_whole_numbers():
    count = 0
    for n in range(1000, 9999+1):
        n_squared = str(n**2)
        if len(n_squared) == 7:
            last_four_digits_of_nsq = n_squared[-1:2:-1] # last 4 digits backward
        elif len(n_squared) == 8:
            last_four_digits_of_nsq = n_squared[-1:3:-1] # last 4 digits backward

        reverse_n = str(n)[::-1]
        if last_four_digits_of_nsq == reverse_n:
            count += 1
            print("n: ", n, "n^2", n**2)
    print("count: ", count)

count_four_digit_whole_numbers()
```

1. What is the running time of the following algorithm? `(Options: O(n), O(log n), O(log log n), O(1))`

```python
Procedure A(n)

begin
    if (n < 3)
        return 1
    else
        return A(ceiling(sqrt(n)))
    end
end
```

4. Find the number of distinct binary search trees that can be created by using 5 distinct keys. `(Options: 5, 14, 24, 42, 36)`

1. Six bells commence tolling together and toll at intervals of 2, 4, 6, 8, 10, and 12 seconds respectively. In 30 minutes, how many times do they toll together? `(Options: 4, 10, 15, 16`)

```python
# Six bells tolling
def count_synchronous_tolls():
    count=0
    toll_time = 30 * 60
    for i in range(1, toll_time+1):
        if all([i%2 == 0, i%4 == 0, i%6 == 0, i%8 == 0, i%10 == 0, i%12 == 0]):
            count += 1
    print("Synchronous toll time: ", count)
    return count

count_four_digit_whole_numbers()
count_synchronous_tolls()
```

## Reformatting dates

### Reformatting dates: Problem statement

Given a date string in the format *Day Month year*, where

1. *Day* is in the set *{"1st", "2nd", "3rd", ..."29th", "30th", "31st"}*
1. *Month* is in the set *{"Jan", "Feb", "Mar", ... "Oct", "Nov", "Dec"}*
1. *Year* is in the inclusive range *[1900, 2100]*

Convert the date string to the format *YYYY-MM-DD*, where:

1. *YYYY* denotes the *4* digit year
1. *MM* denotes the *2* digit month.
1. *DD* denotes the *2* digit day.

For example:

1. *1st Mar 1984 => 1984-03-01*
1. *2nd Feb 2013 => 2013-02-02*
1. *4th Apr 1900 => 1900-04-04*

### Reformatting dates: Constraints

1. The values of *Day*, *Month*, and *Year* are restricted to the value ranges specified above.
1. The given dates are guaranteed to be valid, so no error handling is necessary.
1. $1 \le n \le 10^4$

### Reformatting dates: Solution

```python
def format_single_date(date):
    months = {
        "Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04", "May" : "05", "Jun" : "06",
        "Jul" : "07", "Aug" : "08", "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}
    days = {"1st" : "01", "2nd" : "02", "3rd" : "03", "4th" : "04", "5th" : "05", "6th" : "06",
            "7th" : "07", "8th" : "08", "9th" : "09", "10th" : "10", "11th" : "11", "12th" : "12",
            "13th" : "13", "14th" : "14", "15th" : "15", "16th" : "16", "17th" : "17", "18th" : "18",
            "19th" : "19", "20th" : "20", "21st" : "21", "22nd" : "22", "23rd" : "23", "24th" : "24",
            "25th" : "25", "26th" : "26", "27th" : "27", "28th" : "28", "29th" : "29", "30th" : "30", "31st" : "31",}

    parts = date.split()
    r = parts[2] + "-" + months[parts[1]] + "-" + days[parts[0]]
    return r
assert(format_single_date("1st Mar 1984") == "1984-03-01")
assert(format_single_date("2nd Feb 2013") == "2013-02-02")
assert(format_single_date("4th Apr 1900") == "1900-04-04")

dates = [
    "20th Oct 2052", "6th Jan 1933", "26th May 1960", "20th Sep 1958", "16th Mar 2058",
    "25th May 1912", "16th Dec 2018", "26th Dec 2061", "4th Nov 2030", "28th Jul 1963"]
reformatted_dates = [
    "2052-10-20", "1933-01-06", "1960-05-26", "1958-09-20", "2058-03-16",
    "1912-05-25", "2018-12-16", "2061-12-26", "2030-11-04", "1963-07-28"]

def reformatDates(date_array):
    """
    dates is an array of date strings in the format dates[0], dates[1], ... dates[n]

    Return
    ---------
    String array of converted date strings in the order presented in dates
    """
    r = []
    for date in date_array:
        r.append(format_single_date(date))
    return r

assert(reformatDates(dates) == reformatted_dates)
for k, v in zip(reformatDates(dates), reformatted_dates):
    assert(k == v)
```

## Stock Open Close Price on Particular Weekdays

### Stock Open Close Price on Particular Weekdays: Problem statement

Write a program to retrieve and report various stock information for given days.

Query for stock information using one of the following queries:

1. `https://jsonmock.hackerrank.com/api/stocks:` This query returns all available stock information. The response is paginated so you may need to query `https://jsonmock.hackerrank.com/api/stocks/?page=pageNumber`, where `pageNumber` is an integer that describes the page number to view (e.g., 1, 2, etc.)
2. `https://jsonmock.hackerrank.com/api/stocks/?key=value`: This query returns all results where the searched key has exact matching value. The response is paginated, so you may need to query `https://jsonmock.hackerrank.com/api/stocks/?key=value&page=pageNumber`, where `pageNumber` is an integer that describes the page number to view (e.g., 1, 2, etc.)
1. `https://jsonmock.hackerrank.com/api/stocks/search?key=value`: This query returns all results where the searched key has values that contains `value` as a substring. The response is paginated, so you may need to query `https://jsonmock.hackerrank.com/api/stocks/search?key=value&page=pageNumber`, where `pageNumber` is an integer that describes the page number to view (e.g., 1, 2, etc.)

Each of the queries returns a JSON response with the following *five* fields:

1. `page`: The current page number.
1. `per_page`: The maximum number of results per page.
1. `total`: The total number of response.
1. `total_pages`: The total number of pages which must be queried to get all the results.
1. `data`: An array of JSON objects that contains the stock information. The JSON contains the following *five* fields, which could be used as a *key* to query:

    1. `date`: A string that describes the date on which the stock information is provided. The date format is `d-mmm-yyyy`, where `d` describes a valid day of the month, `mmm` describes the complete name of the month (e.g., `January`, `February`, `March`, etc.), and `yyyy` describes the year. The date is in the range `5-January-2000` to `1-January-2014` inclusive. There could be no information provided for some of the dates and the information is available for `Monday` to `Friday` only.
    1. `open`: A float value that describes the stock open price on the given date.
    1. `close`: A float value that describes the stock close price on the given date.
    1. `high`: A float value that describes the stock highest price on the given date.
    1. `low`: A float value that describes the stock lowest price on the given date.

To solve this challenge, complete the function `openAndClosePrices`, which has three string parameters: `firstDate`, `lastDate`, and `weekDay`. Query for the stock `open` and `close` prices on each date when the weekday is `weekDay` if the stock information is available. The stock information on each date should be printed on a new line that contains the three space separated values that describe the date, the open, and the close price respectively. The order of the dates in the output does not matter.

### Stock Open Close Price on Particular Weekdays: Solution

```python
import json
import datetime

import requests

from collections import OrderedDict
from dateutil import parser

def get_weekday(date):
    """Get weekday"""
    date = date.split("-")
    date = "{} {} {}".format(date[1], date[0], date[2])
    return parser.parse(date).strftime("%A")

def date_string_to_datetime(date_string):
    months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6,
             "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}
    s = date_string.split("-")
    return datetime.datetime(int(s[2]), months[s[1]], int(s[0]))

def get_stock_price_list():
    """Get a list of all stock price data"""
    resp = requests.get("https://jsonmock.hackerrank.com/api/stocks/").text
    r = json.loads(resp)

    ordered_prices = OrderedDict() #[date, open, high, low, close]
    total_pages = int(r["total_pages"])
    data = r["data"]

    for each in data:
        date = each["date"]
        ordered_prices[date_string_to_datetime(date)] = [
            each["date"], each["open"], each["high"], each["low"], each["close"]
        ]

    for i in range(2, total_pages+1): # start from page 2
        url = "https://jsonmock.hackerrank.com/api/stocks/?page={}".format(i)
        json_resp = json.loads(requests.get(url).text)

        for each in json_resp["data"]:
            date = each["date"]
            ordered_prices[date_string_to_datetime(date)] = [
                each["date"], each["open"], each["high"], each["low"], each["close"]
            ]
    return ordered_prices

ordered_stock_prices = get_stock_price_list()

def openAndClosePrices(firstDate, lastDate, weekDay):
    allowed_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    firstDate = date_string_to_datetime(firstDate)
    lastDate = date_string_to_datetime(lastDate)

    for date, val in ordered_stock_prices.items():
        if (date >= firstDate) & (date <= lastDate):
            week_day = get_weekday(val[0])
            if (week_day == weekDay) & (week_day in allowed_weekdays):
                print("{} {} {}".format(val[0], val[1], val[-1]))
#                 print(week_day, date, val)
```

## Work Schedule

### Work Schedule: Problem statement

You just got a new job where you have to work exactly as many hours as you are told each work, working no more than a daily maximum number of hours per day. Some of the days, they'll tell you how many hours you will work. You get to choose the remainder of your schedule, within the limits.

A completed schedule consists of exactly 7 digits in the range *0* to *8* representing each day's hours to be worked. You will get a pattern string similar to the schedule, but with some of the digits replaced by a question mark, *?, (ascii 63 decimal)*. Given a maximum number of hours you can work in a day, replace the question marks with digits so that the sum of the scheduled hours is exactly the hours you must work in a week. Return a string array with all possible schedules you can create, ordered lexicographically.

For example, your partial schedule, *pattern = 08??840*, your required hours, *work_hours = 24*, and you can only work, at most, *day_hours = 4* hours per day during the two days in question. You have two days on which you  must work *24 - 20 = 4* more hours for the week. All of your possible schedules are listed below:

    0804840
    0813840
    0822840
    0831840
    0840840

### Work Schedule: Function Description

Complete the function *findSchedules* in the editor below. The function must return an array of strings that represents all possible valid schedules. The strings must be ordered lexicographically.

findSchedules has following parameter(s):
    *work_hours*: an integer that represents the hours you must work in the week
    *day_hours*: an integer that represents the maximum hours you may work in a day
    *pattern*: a string that represents the partially completed schedule

## Work Schedule: Constraints

1. $1 \le work_hours \le 56$
1. $1 \le day_hours \le 8$
1. $|pattern| = 7$
1. Each character of pattern $\belongs 0, 1, ..., 8$
1. There is at least one correct schedule
