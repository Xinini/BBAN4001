call_sat = [92,92,89,91,79,75,80,84,84,81,77,91,89,87]
drop = [14,13,11,13,11,27,15,5,7,17,7,3,6,4]
lvl = [25,45,67,56,47,87,94,63,53,89,94,34,45,35]
print(sum(call_sat)/len(call_sat))
for i in range(0, len(call_sat)):
    if lvl[i] > 80:
        call_sat[i] = float((lvl[i] - 80) * 0.4) + call_sat[i]

print(call_sat)

print(sum(call_sat)/len(call_sat))