import statistics as stats


def _convert_to_floats(args):
    num_arr = []
    for numstr in args:
        try:
            num_arr.append(float(numstr))
        except:
            raise ValueError("Could not process item: %s" % numstr)
    return num_arr


def _mean(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the mean.")
    num_arr = _convert_to_floats(args)
    return stats.mean(num_arr)


def _median(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the median.")
    num_arr = _convert_to_floats(args)
    return stats.median(num_arr)


def _mode(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the mode.")
    num_arr = _convert_to_floats(args)
    return stats.mode(num_arr)


def _var(args):
    if len(args) < 2:
        raise ValueError(
            "I need at least 2 arguments to calculate the sample variance.")
    num_arr = _convert_to_floats(args)
    return stats.variance(num_arr)


def _stdev(args):
    if len(args) < 2:
        raise ValueError(
            "I need at least 2 arguments to calculate the sample standard deviation.")
    num_arr = _convert_to_floats(args)
    return stats.stdev(num_arr)


def _pvar(args):
    if len(args) == 0:
        raise ValueError(
            "I need at least 1 argument to calculate the population variance.")
    num_arr = _convert_to_floats(args)
    return stats.pvariance(num_arr)


def _pstdev(args):
    if len(args) == 0:
        raise ValueError(
            "I need at least 1 argument to calculate the population variance.")
    num_arr = _convert_to_floats(args)
    return stats.pstdev(num_arr)


_function_map = {
    "mean": _mean,
    "median": _median,
    "mode": _mode,
    # Two definitions for variance
    "var": _var,
    "variance": _var,
    # Three definitions for standard deviation
    "stdev": _stdev,
    "stddev": _stdev,
    "standard-deviation": _stdev,
    # Two definitions for population variance
    "pvar": _pvar,
    "population-variance": _pvar,
    # Three definitions for population standard deviation
    "pstdev": _pstdev,
    "pstddev": _pstdev,
    "population-standard-deviation": _pstdev,
}


def evaluate(command, args):
    function = _function_map.get(command.lower(), None)
    if function is not None:
        return str(function(args))
    return None
