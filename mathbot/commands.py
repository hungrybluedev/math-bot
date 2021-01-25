from mathbot.main import COMPACT_FORMAT, GENERATOR_LIMIT
import random
import statistics as stats


def _obtain_floats(args):
    num_arr = []
    for numstr in args:
        try:
            num_arr.append(float(numstr))
        except:
            raise ValueError("Could not process item: %s" % numstr)
    return num_arr


def _obtain_count(num_str):
    try:
        value = int(num_str)
        if value > 0:
            return min(value, GENERATOR_LIMIT)
        else:
            raise ValueError("%d is not positive." % value)
    except:
        raise ValueError(
            "Expected a positive integer. Got %s instead." % num_str)


def _obtain_non_negaitive_float(num_str):
    try:
        value = float(num_str)
        if value >= 0:
            return value
        else:
            raise ValueError("%s is not positive." % num_str)
    except:
        raise ValueError(
            "Expected a positive float. Got %s instead." % num_str)


def _mean(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the mean.")
    num_arr = _obtain_floats(args)
    return stats.mean(num_arr)


def _median(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the median.")
    num_arr = _obtain_floats(args)
    return stats.median(num_arr)


def _mode(args):
    if len(args) == 0:
        raise ValueError("I need at least 1 argument to calculate the mode.")
    num_arr = _obtain_floats(args)
    return stats.mode(num_arr)


def _var(args):
    if len(args) < 2:
        raise ValueError(
            "I need at least 2 arguments to calculate the sample variance.")
    num_arr = _obtain_floats(args)
    return stats.variance(num_arr)


def _stdev(args):
    if len(args) < 2:
        raise ValueError(
            "I need at least 2 arguments to calculate the sample standard deviation.")
    num_arr = _obtain_floats(args)
    return stats.stdev(num_arr)


def _pvar(args):
    if len(args) == 0:
        raise ValueError(
            "I need at least 1 argument to calculate the population variance.")
    num_arr = _obtain_floats(args)
    return stats.pvariance(num_arr)


def _pstdev(args):
    if len(args) == 0:
        raise ValueError(
            "I need at least 1 argument to calculate the population variance.")
    num_arr = _obtain_floats(args)
    return stats.pstdev(num_arr)


def _uniform(args):
    n = len(args)
    if n == 0:
        # 1. No arguments provided; return 1 uniform variate from [0, 1)
        return random.uniform(0, 1)
    elif n == 1:
        # 2. One argument provided - count; ensure that it is positive
        # return "count" uniform variates from [0, 1)
        count = _obtain_count(args[0])
        return " ".join([str(COMPACT_FORMAT % random.uniform(0, 1)) for _ in range(count)])
    elif n == 2:
        # 3. Two arguments provided - upper (float) and count (positive integer)
        lower = 0
        upper = _obtain_floats([args[0]])[0]
        # Ensure that lower < upper
        if upper < lower:
            temp = lower
            lower = upper
            upper = temp
        count = _obtain_count(args[1])
        return " ".join([str(COMPACT_FORMAT % random.uniform(lower, upper)) for _ in range(count)])
    elif n == 3:
        # 4. Three arguments provided - lower (float), upper (float) and count (positive integer)
        bound = _obtain_floats(args[0:2])
        lower = bound[0]
        upper = bound[1]
        # Ensure that lower < upper
        if upper < lower:
            temp = lower
            lower = upper
            upper = temp
        count = _obtain_count(args[2])
        return " ".join([str(COMPACT_FORMAT % random.uniform(lower, upper)) for _ in range(count)])
    else:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation.")


def _bernoulli_variate(p):
    return 1 if random.uniform(0, 1) < p else 0


def _bernoulli(args):
    n = len(args)
    if n == 0:
        # 1. If there are no arguments, return one variate with p=0.5
        return _bernoulli_variate(0.5)
    elif n == 1:
        # 2. One argument: count (positive integer)
        count = _obtain_count(args[0])
        return " ".join([str(_bernoulli_variate(0.5)) for _ in range(count)])
    elif n == 2:
        # 3. Two arguments: p (nonnegative float) and count (positive integer)
        p = _obtain_non_negaitive_float(args[0])
        # Normalize p to be in the range [0, 1)
        while p >= 1:
            p /= 10
        count = _obtain_count(args[1])
        return " ".join([str(_bernoulli_variate(p)) for _ in range(count)])
    else:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation.")


def _binomial(args):
    if len(args) != 3:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation.")
    count = _obtain_count(args[0])
    p = _obtain_non_negaitive_float(args[1])
    # Normalize p to be in the range [0, 1)
    while p >= 1:
        p /= 10
    m = _obtain_count(args[2])
    return " ".join([str(sum([_bernoulli_variate(p) for _ in range(count)])) for _ in range(m)])


def _normal(args):
    n = len(args)
    if n == 0:
        # 1. No arguments. Return 1 variate from Normal(0, 1)
        return random.normalvariate(0, 1)
    elif n == 1:
        # 2. 1 argument: count (positive integer).
        # Return "count" variates from Normal(0, 1)
        count = _obtain_count(args[0])
        return " ".join([str(COMPACT_FORMAT % random.normalvariate(0, 1)) for _ in range(count)])
    elif n == 2:
        # 3. 2 arguments: sigma (nonnegative float) and count (positive integer)
        # Return "count" variates from Normal(0, sigma)
        sigma = _obtain_non_negaitive_float(args[0])
        count = _obtain_count(args[1])
        return " ".join([str(COMPACT_FORMAT % random.normalvariate(0, sigma)) for _ in range(count)])
    elif n == 3:
        # 4. 3 arguments: mu (float), sigma (nonnegative float) and count (positive integer)
        # Return "count" variates from Normal(mean, sigma)
        mu = _obtain_floats([args[0]])[0]
        sigma = _obtain_non_negaitive_float(args[1])
        count = _obtain_count(args[2])
        return " ".join([str(COMPACT_FORMAT % random.normalvariate(mu, sigma)) for _ in range(count)])
    else:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation.")


def _exponential(args):
    n = len(args)
    if n == 1:
        # 1. One argument: _lambda (non-negative float)
        _lambda = _obtain_non_negaitive_float(args[0])
        return random.expovariate(_lambda)
    elif n == 2:
        # 2. Two arguments: _lambda (non-negative float) and count (positive integer)
        _lambda = _obtain_non_negaitive_float(args[0])
        count = _obtain_count(args[1])
        return " ".join([str(COMPACT_FORMAT % random.expovariate(_lambda)) for _ in range(count)])
    else:
        raise ValueError(
            "Incorrect number of arguments. Refer to the documentation.")


_function_map = {
    # ========================
    # DISTRIBUTION SIMULATIONS
    # ========================
    "uniform": _uniform,
    # Two definitions for Bernoulli
    "flip": _bernoulli,
    "bernoulli": _bernoulli,
    # Three definitions for binomial
    "nflip": _binomial,
    "binom": _binomial,
    "binomial": _binomial,
    # Three definitions for Gaussian
    "gauss": _normal,
    "gaussian": _normal,
    "normal": _normal,
    # Three definitions for Exponential
    "exp": _exponential,
    "exponential": _exponential,
    "poisson": _exponential,
    # ==========
    # STATISTICS
    # ==========
    # Three definitions for mean
    "mean": _mean,
    "avg": _mean,
    "average": _mean,
    "median": _median,
    "mode": _mode,
    # Two definitions for variance
    "var": _var,
    "variance": _var,
    # Three definitions for standard deviation
    "stdev": _stdev,
    "stddev": _stdev,
    "standard-deviation": _stdev,
    # Three definitions for population variance
    "pvar": _pvar,
    "pvariance": _pvar,
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
