def exception_handling():
    try:
        car = {"make": "BMW", "model": "550i", "year": "2018"}
        print(car["color"])

    except:
        print("Key not found")
        raise Exception("This is an exception")

    else:
        print("No exception occurred")

    finally:
        print("PLease select the keys available in the list")


exception_handling()
