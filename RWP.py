import requests

print ("------------------------------------")
print ("This is the Rayburn Weather Program.")
print ("------------------------------------")
print ("")
print ("")
print ("")

# Welcome screen


def cityname(): # This function is when the user wants to input a city name
    city = input('Please type the city name: ')
    url = 'https://api.openweathermap.org/data/2.5/weather?q={0},us&appid=9606f4bb9438be0741e3d2ddee18a04d&units=imperial'.format(city)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Would you like to check another city? Type 1 for Yes or 2 for No: ')
    if question == '1':
        main()
    if question == '2':
        print("Goodbye!")
        exit()




def zipcode(): # This function is when the user wants to input a zip code
    zip_code = int(input('Please type the zip code: '))
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={0},us&units=imperial&appid=9606f4bb9438be0741e3d2ddee18a04d'.format(zip_code)
    res = requests.get(url)
    data = res.json()
    show_data(data)

    question = input('Would you like to check another city? Type 1 for Yes or 2 for No: ')
    if question == '1':
        main()
    if question == '2':
        print("Goodbye!")
        exit()




def show_data(data): # This displays and formats the weather
    temp = data['main']['temp']
    hightemp = data['main']['temp_max']
    lowtemp = data['main']['temp_min']
    wind_speed = data['wind']['speed']
    humid = data['main']['humidity']
    description = data['weather'][0]['description']

    print('Current Temperature : {} degree fahrenheit'.format(temp))
    print('High Temperature : {} degree fahrenheit'.format(hightemp))
    print('Low Temperature : {} degree fahrenheit'.format(lowtemp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Humidity : {} %'.format(humid))
    print('Description : {}'.format(description))





def main(): #This is the main function for dealing with checking input
    while True:
        answer = input("Press 1 to look up weather by city name, press 2 for zip code: ")
        if answer == '1':
            try:
                print("Input accepted.")
                cityname()

            except Exception:
                print("Please only type valid names")
                cityname()

        if answer == '2':
            try:
                print("Input accepted")
                zipcode()

            except Exception:
                print("Please only type valid zip codes")
                zipcode()

        else:
            print("Please only select valid options")


main()

