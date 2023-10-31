################################################################################
#     ____                          __     _                          ___
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          <  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \         / / 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        / /  
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /_/   
#                                                                        
#  Question 1
################################################################################
#
# Instructions:
# The two functions below are used to tell the weather. They have some bugs that
# need to be fixed. The test suite in `question1_test.py` will verify the output.
# Read the test suite to know the values that these functions should return.


def get_city_temperature(city: str) -> int:
    """
    The function "get_city_temperature" returns the temperature of a given city.

    :Params: 
      city: The "city" parameter is a string that represents the name of a city
    :Return: 
      The temperature of the specified city.
    """
    temperatures = {
       "Quito": 22,
       "Sao Paulo": 17,
       "San Francisco": 16,
       "New York": 14,
    }

    return temperatures.get(city, None)

def get_city_weather(city: str) -> str:
    """
    The function "get_city_weather" returns the temperature and weather condition of a given city.

    :Params: 
      city: The `city` parameter is a string that represents the name of a city
    :return: 
      A string that includes the temperature and weather condition of the specified city.
    """
    sky_condition = {
       "Sao Paulo": "cloudy",
       "New York": "rainy",
       "Quito": "sunny",
    }

    temperature = get_city_temperature(city)

    if temperature is not None:
        weather = sky_condition.get(city, "unknown weather")
        return f"{temperature} degrees and {weather}"
    else:
        return "Unknown temperature and weather"
