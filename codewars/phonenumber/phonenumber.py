def create_phone_number(n):
    num = [str(d) for d in n]
    nums = "".join(num)
    return "("+nums[:3]+") "+nums[3:6]+"-"+nums[6:]

