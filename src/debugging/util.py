"""Utility for tracking and debugging
"""
import sys, time

_TIME_CHECK = {}


def check_time(func):
    """Collect the period while executing function 

    Parameters
    ----------
        func : function

    Examples
    --------
    >> from util import check_time
    >> @check_time
       def hello(name):
           print(f"Hello Guys, I'm {name}")
    >> hello("Wola")
    >> print_func_time()
    """

    def _check_time(*args, **kwargs):
        global _TIME_CHECK
        curr_time = time.perf_counter()
        result = func(*args, **kwargs)
        if func not in _TIME_CHECK.keys():
            _TIME_CHECK[func] = time.perf_counter() - curr_time
        else:
            _TIME_CHECK[func] = (
                _TIME_CHECK[func] + time.perf_counter() - curr_time
            ) / 2
        # print(f"Time: {func}, {time.perf_counter() - curr_time}")

        return result

    return _check_time


def print_func_time():
    """Print the period while executing function with @check_time

    Examples
    --------
    >> from util import check_time
    >> @check_time
       def hello(name):
           print(f"Hello Guys, I'm {name}")
    >> hello("Wola")
    >> print_func_time()
    """
    global _TIME_CHECK
    for key, value in zip(_TIME_CHECK.keys(), _TIME_CHECK.values()):
        print(
            key, str(round(value * 1000, 3)) + " ms",
        )
    _TIME_CHECK = {}


def print_progress(iteration, total, prefix="", suffix="", decimals=1, barLength=100):
    """Progress Bar

        This library provides an easy progress bar implementation for refence in the
        terminal. This function should be called everytime the value needs to be 
        updated, since it only provides the graphical part of the progress bar

        Parameters
        ----------
        iteration: the current state (n or i) of the progress
        total: the total number of interactions
        prefix: what will be shown before the progress bar (in the same line)
        suffix: what will be shown after the progress bar (in the same line)
        decimals: the number of fractional digits shown as progress
        barLength: the number of characters used in the progress bar

        Notes
        -----
        You can edit the function for different characters

        Examples
        --------
        >> from util import print_progress
        >> total = 10e3
        >> for i in range(int(total)):
        >>     print_progress(i, total)

    """
    formatstr = "{0:." + str(decimals) + "f}"
    percent = formatstr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = "#" * filledLength + "-" * (barLength - filledLength)
    sys.stdout.write("\r%s |%s| %s%s %s" % (prefix, bar, percent, "%", suffix)),
    if iteration == total:
        sys.stdout.write("\n")
    sys.stdout.flush()
