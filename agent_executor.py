import google.generativeai as genai
import requests

# ✅ Set your Google Gemini API key
genai.configure(api_key="AIzaSyBIU_8TuXWRQjhXJTU9sDZBHkIIBvHPQRQ")

class WeatherAgentExecutor:
    def __init__(self):
        # ✅ Using the light-weight Gemini flash model
        self.model = genai.GenerativeModel("models/gemini-1.5-flash")

    def get_weather_data(self, city: str) -> str:
        api_key = "c6b3386c2c6659c30df4c25ba51e9240"  # ✅ Your OpenWeatherMap API key
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        
        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200 or "main" not in data:
                return f"❌ Couldn't fetch weather for {city.title()}."

            desc = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']

            return (
                f"🌤️ Weather in {city.title()}:\n"
                f"- Description: {desc}\n"
                f"- Temperature: {temp}°C\n"
                f"- Humidity: {humidity}%\n"
                f"- Wind Speed: {wind} m/s"
            )

        except Exception as e:
            return f"❌ Error fetching weather: {str(e)}"

    def run(self, query: str) -> str:
        try:
            prompt = f"Extract only the city name from this sentence: \"{query}\". Respond with only the city."
            result = self.model.generate_content(prompt)
            city = result.text.strip().split('\n')[0]

            if not city:
                return "❌ Couldn't extract city from your query."

            return self.get_weather_data(city)

        except Exception as e:
            return f"❌ Gemini Error: {str(e)}"
