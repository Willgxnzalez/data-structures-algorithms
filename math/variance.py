
data = [2, 8]

mean = sum(data) / len(data)

deviations = [x-mean for x in data]

squared_devs = [d**2 for d in deviations]

variance = sum(squared_devs) / len(data)

print(f"variance of {data}:", variance)


