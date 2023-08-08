import dishes
import menu
import discount
import order
import ds_exception


try:
    banana = dishes.Dish("banana", "fruit", 21)
    apple = dishes.Dish("apple", "fruit", 32)
    meat = dishes.Dish("steak", "meat", 150)
    order_1 = menu.MenuCategory()
    order_1.add_dishes("fruits", banana)
    order_1.add_dishes("fruits", apple)
    order_1.add_dishes("steak", meat)
    print(order_1)

    e = order.Order()
    e.add_item(banana)
    e.add_item(apple)
    e.add_item(meat)
    e.remove_item("banana")
    e.calculate_total(discount.GoldDiscount())
    print(e)
except ds_exception.DiscountException as err:
    print(err)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)
