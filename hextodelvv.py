def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

print(hex_to_rgb("#ffffff"))
print(hex_to_rgb("#ffffffffffff"))
print(rgb_to_hex((255, 255, 255)))
print(rgb_to_hex((65535, 65535, 65535)))
