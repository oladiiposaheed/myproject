def menu_is_boring(meals, L):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    lst = []
    for meal in meals:
        if meal != L:
            continue
        else:
            lst.append(meal)
        return True
print(menu_is_boring(['Rice', 'Beans', 'Garri', 'Yam'], 'Garri'))