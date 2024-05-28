original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = sorted(original_list)
print(sorted_list)  # Saída: [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(original_list)  # A lista original permanece inalterada

print(30*'-')
#sort altera lista original
original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
original_list.sort()
print(original_list)  # Saída: [1, 1, 2, 3, 4, 5, 5, 6, 9]