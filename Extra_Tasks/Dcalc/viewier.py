import dcalc


def create_list_degrees(*args, **kwargs):
    points = {}
    for i in range(len(args)):
        points[f"Point_{i}"] = args[i]

    points.update(kwargs)

    lst = []

    for k, v in points.items():
        lst.append(f"{k} = {dcalc.deg_to_gms(v)}")

    return lst


print(create_list_degrees(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
