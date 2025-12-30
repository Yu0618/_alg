import random

def generate_point(bounds, dim=0, point=None):
    if point is None:
        point = []

    if dim == len(bounds):
        return point

    a, b = bounds[dim]
    x = random.uniform(a, b)
    point.append(x)

    return generate_point(bounds, dim + 1, point)

def monte_carlo_integral(f, bounds, samples): 
    volume = 1.0
    for a, b in bounds:
        volume *= (b - a)

    total = 0.0
    for _ in range(samples):
        x = generate_point(bounds)
        total += f(x)

    return volume * total / samples

def example_function(x):
    return sum(v * v for v in x)

if __name__ == "__main__":
    n = 4
    bounds = [(0, 1)] * n
    samples = 200000

    result = monte_carlo_integral(
        example_function,
        bounds,
        samples
    )

    print(f"{n} 維蒙地卡羅積分結果 =", result)
