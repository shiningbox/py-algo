from list.linked_sequence import LinkedSequence

# Sort N element with N iterations

# For each iteration i, find the max n-i-1 and put it onto n-i-1 index

# Postional based implementation

seq = LinkedSequence()
seq.insert_last(1)
seq.insert_last(3)
seq.insert_last(5)
seq.insert_last(2)
seq.insert_last(8)
seq.insert_last(5)
seq.insert_last(9)
print("Before queue...")
seq.print()

size = seq.size()
# O(2) times
for i in range(size):
    current = seq.first()
    for j in range((size - i)):
        next = seq.after(current)
        if current.element >= next.element:
            seq.swap(current, next)
        else:
            current = next
print("After queue...")
seq.print()
