def zodiac_year_qualifier(year):
    year_types = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']
    year_mod = year % 12
    year_animal = year_types[year_mod]
    return(year_animal)

if  __name__ == "__main__":
    year_user = int(input())
    print(zodiac_year_qualifier(int(input()))) 