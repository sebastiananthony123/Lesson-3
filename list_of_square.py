def filter_even(lst):
   return[x for x in lst if x % 2 == 0]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter_even(numbers)
print(f"Even numbers: {even_numbers}")

sq = [i **2 for i in range(1,11)]
print(sq)