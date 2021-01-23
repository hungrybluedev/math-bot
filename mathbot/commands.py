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
    return stats.median(args)


_function_map = {
    "mean": _mean,
    "median": _median,
}


def evaluate(command, args):
    function = _function_map.get(command.lower(), None)
    if function is not None:
        return str(function(args))
    return None
