def human_years_cat_years_dog_years(num):
     if num <= 2:
        return [num, 6 + 9 * num, 6 + 9 * num]
     else:
        return [num, 16 + 4 * num, 14 + 5 * num]

print(human_years_cat_years_dog_years(10))