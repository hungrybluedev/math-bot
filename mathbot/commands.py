from mathbot.main import COMPACT_FORMAT, DOCUMENTATION_LINK
import random
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


def _convert_to_positive_int(num_str):
    try:
        value = int(num_str)
        if value > 0:
            return min(value, GENERATOR_LIMIT)
        else:
            raise ValueError("%d is not positive.")
    except:
        raise ValueError(
            "Expected a positive integer. Got %s instead." % num_str)


def _uniform(args):
    n = len(args)
    if n == 0:
        # 1. No arguments provided; return 1 uniform variate from [0, 1)
        return random.uniform(0, 1)
    elif n == 1:
        # 2. One argument provided - count; ensure that it is positive
        # return "count" uniform variates from [0, 1)
        count = _convert_to_positive_int(args[0])
        return " ".join([str(COMPACT_FORMAT % random.uniform(0, 1)) for _ in range(count)])
    elif n == 2:
        # 3. Two arguments provided - upper (float) and count (positive integer)
        lower = 0
        upper = _convert_to_floats([args[0]])[0]
        # Ensure that lower < upper
        if upper < lower:
            temp = lower
            lower = upper
            upper = temp
        count = _convert_to_positive_int(args[1])
        return " ".join([str(COMPACT_FORMAT % random.uniform(lower, upper)) for _ in range(count)])
    elif n == 3:
        # 4. Three arguments provided - lower (float), upper (float) and count (positive integer)
        bound = _convert_to_floats(args[0:2])
        lower = bound[0]
        upper = bound[1]
        # Ensure that lower < upper
        if upper < lower:
            temp = lower
            lower = upper
            upper = temp
        count = _convert_to_positive_int(args[2])
        return " ".join([str(COMPACT_FORMAT % random.uniform(lower, upper)) for _ in range(count)])
    else:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation: %s" % DOCUMENTATION_LINK)


_function_map = {
    # ========================
    # DISTRIBUTION SIMULATIONS
    # ========================
    "uniform": _uniform,
    # ==========
    # STATISTICS
    # ==========
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
