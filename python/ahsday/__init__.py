import check50
import random
import check50.py
import os

@check50.check()
def exists():
    """ Check that file exists """
    check50.exists("days.py")

@check50.check(exists)
def nodt():
    """ Not using datetime module """
    with open("days.py") as f:
        file = f.read()

    if "datetime" in file:
        raise check50.Failure("Oops, looks like you might be using the datetime module", help = "Someday this will be cool, but not today")

@check50.check(nodt)
def run():
    """ File runs without syntax errors"""
    check50.include("data.csv","test.csv")
    out = check50.run("python days.py").stdout(timeout=30)
    check50.log(out)
    if 'error' in out.lower():
        raise check50.Failure("Make sure your program has no errors")
    #days = check50.internal.import_file("days", "days.py")

@check50.check(run)
def strday():
    """ Checking dunder __str__ for Day class """
    days = check50.py.import_("days.py")
    d = random.randint(2,28)
    weekend = days.Day(month=1,day=d,year=2024).__str__()
    if not (weekend == f"January {d}, 2024"):
        raise check50.Mismatch(f"January {d}, 2024", weekend, help="Make sure you define a good __str__ method for your Day")

@check50.check(run)
def strahsday():
    """ Checking dunder __str__ for AHSDay class """
    days = check50.py.import_("days.py")
    d = random.randint(4,8)
    weekend = days.AHSDay(daynum = d - 2, month=2,day=d,year=2024).__str__()

    if f"February {d}, 2024" not in weekend:
        raise check50.Mismatch(f"February {d}, 2024", weekend, help="Make sure your __str__ method for AHSDay includes the date")

    if f"{d - 2}" not in weekend.replace("2024",""):
        raise check50.Mismatch(f"Day {d - 2}", weekend, help="Make sure your __str__ method for AHSDay includes the AHS Day #")

@check50.check(run)
def between():
    """ Checking days_between for Day class """
    days = check50.py.import_("days.py")

    if int(days.Day.days_between({'month':2,'day':1,'year':2024},{'month':3,'day':1,'year':2024})) != 29:
        raise  check50.Mismatch(str(29), str(days.Day.days_between({'month':2,'day':1,'year':2024},{'month':3,'day':1,'year':2024})))


@check50.check(run)
def week_day():
    """ Checking Day's static method get_week_day"""
    days = check50.py.import_("days.py")
    if days.Day.get_week_day(month=1,day=27,year=2024) != "Saturday":
         raise  check50.Mismatch(days.Day.get_week_day(month=1,day=27,year=2024), "Saturday")

@check50.check(week_day)
def day_week():
    """ Checking Day's instance method day_of_week """
    days = check50.py.import_("days.py")
    if days.Day(month=2,day=6,year=2024).day_of_week() != "Tuesday":
         raise  check50.Mismatch(days.Day(month=2,day=6,year=2024).day_of_week(), "Tuesday")

@check50.check(run)
def jorge():
    """ Checking days_meet"""
    days = check50.py.import_("days.py")
    days.AHSDay.load(file = "data.csv")
    fblock_left = days.AHSDay.days_meet('F', startdt = {'month':2, 'day':9, 'year':2024})
    if len(fblock_left) != 46:
        raise check50.Mismatch(str(46), str(len(fblock_left)), help="Starting Feb 9, Juniors should have 46 more F blocks")

    days.AHSDay.load(file = "test.csv")
    fblock_left = days.AHSDay.days_meet('F', startdt = {'month':10, 'day':9, 'year':2023})
    if len(fblock_left) != 11:
        raise check50.Mismatch(str(11), str(len(fblock_left)), help="Jorge Cham postulates there's an alternate universe where you would only have 11 AP CSPs left :'(")


@check50.check(run)
def periods():
    """ Checking AHSDay static method get_periods"""
    days = check50.py.import_("days.py")
    fblocks = days.AHSDay.get_periods('F')
    if fblocks != [0, 3, 5, 0, 3, 4, 0, 4]:
        raise check50.Mismatch("[0, 3, 5, 0, 3, 4, 0, 4]",str(days.AHSDay.get_periods('F')))
    if days.AHSDay.get_periods('B') != [0, 1, 0, 1, 2, 0, 1, 2]:
        raise check50.Mismatch("[0, 1, 0, 1, 2, 0, 1, 2]",str(days.AHSDay.get_periods('B')))