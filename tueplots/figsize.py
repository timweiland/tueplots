# Double-column formats


def icml(*, column="half", nrows=1):

    height_per_width = golden_ratio()
    if column == "half":
        width = 234.8775 / 72.27
        height = height_per_width * width * nrows
        return width, height

    width = 487.8225 / 72.27
    height = width * height_per_width / 2.0 * nrows
    return width, height


def cvpr(*, column="half", nrows=1):
    height_per_width = golden_ratio()
    if column == "half":
        width = 237.13594 / 72.27
        height = height_per_width * width * nrows
        return width, height
    width = 496.85625 / 72.27
    height = width * height_per_width / 2.0 * nrows
    return width, height


# Single-column formats


def jmlr(*, nrows=1):
    """JMLR figure size"""
    width = 433.62 / 72.27
    height = 0.5 * width * golden_ratio() * nrows
    return width, height


def neurips(*, nrows=1):
    width = 397.48499 / 72.27
    height = golden_ratio() * width * nrows
    return width, height


def golden_ratio():
    return (5.0 ** 0.5 - 1.0) / 2.0


def inches_per_point():
    return 1.0 / 72.27