def unique_in_order(sequence):
    return [sequence[i] for i in range(len(sequence)) if i == 0 or sequence[i] != sequence[i-1]]

print(unique_in_order("AAssddaAAssaaa"))