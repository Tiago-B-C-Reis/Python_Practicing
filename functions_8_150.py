# 8.12
def sandwiches(*items):
    message = f'You choose to have {items} on your sandwich'
    return message


sandwich = sandwiches("Chicken", "Egg", "Seafood", "Roast Beef",
                      "Grilled", "Ham", "Nutella")
# print(sandwich)


# 8.13
def build_profile(first, last, **user_info):

    """Build a dictionary containing everything we know about a user."""

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Tiago', 'Reis', location='Europe', field='Engineer')
# print(user_profile)


# 8.14
def car_build(manufacturer, model, **car_info):

    """Build a dictionary containing everything we know about a user."""

    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    print(car_info)


# car_build('subaru', 'impreza', color='blue', tow_package=True, rali_prepare='Yes')
