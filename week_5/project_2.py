print ("Welcome to Yega Services")
print ("We are a delivery and logistics company that provides the best and affordable delivery services.")

weight = float(input("What is the weight of the package?: "))
location = str(input("What is the delivery location of the package? (Choose an option between Ibeju-Lekki or Epe): "))
def services (str):

    if weight >= 10.0 and location == "Ibeju-Lekki":
        print ("The delivery price is NGN 2,000")

    elif weight < 10.0 and location == "Ibeju-Lekki":
        print ("The delivery price is NGN 1,500")

    elif weight >= 10.0 and location == "Epe":
        print ("The delivery price is NGN 5,000")

    elif weight < 10.0 and location == "Epe":
        print ("The delivery price is NGN 4,000")

    else:
        print ("Invalid Input")
    print ("Thank you for using Yega's Services")
    return

services (str)