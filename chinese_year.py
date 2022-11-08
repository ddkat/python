def zodiac_year_qualifier(year):
    zodiacs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']
    mod_year = year % 12
    result_zodiac = zodiacs[mod_year]
    return(result_zodiac)

if  __name__ == "__main__":
    year_user = int(input())
    print(zodiac_year_qualifier(year_user))