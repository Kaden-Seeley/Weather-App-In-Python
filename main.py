import customtkinter
import python_weather
import asyncio


async def main() -> None:
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        weather = await client.get('Maine')

        for daily in weather:
            # print(daily)
            pass

        for hourly in daily:
            # print(f' --> {hourly!r}')
            pass
        
    app = customtkinter.CTk()
    app.geometry("300x300")
    app.title("Test Weather App")

    localtime_label = customtkinter.CTkLabel(app, text=f"Local Date & Time: {weather.datetime}")
    localtime_label.pack()

    country_label = customtkinter.CTkLabel(app, text=f"Current Country: {weather.country}")
    country_label.pack()

    city_label = customtkinter.CTkLabel(app, text=f"Current City: {weather.location}")
    city_label.pack()

    temp_label = customtkinter.CTkLabel(app, text=f"Current Temp: {weather.temperature}")
    temp_label.pack()

    app.mainloop()

if __name__ == '__main__':
    asyncio.run(main())

main()