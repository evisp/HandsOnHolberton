# Shopping Cart System (Python OOP Project)  

## Project Overview  
This project is a simple shopping cart system to help you practice key Object-Oriented Programming (OOP) concepts.  

### Concepts Covered  
✅ Private variables (`__var`)  
✅ Property getters (`@property`)  
✅ `__init__` constructor  
✅ `__str__` for string representation  
✅ `__dict__` for object dictionary representation  
✅ Exception handling  
✅ Connecting multiple classes  



## Your Tasks

### **1. Develop the `Product` class**  
The `Product` class represents an item that can be purchased.  

1. The class must have **two private attributes**:  
   - `__name`: Stores the name of the product.  
   - `__price`: Stores the price of the product.  
2. The constructor (`__init__`) must:  
   - Accept `name` and `price` as parameters.  
   - Raise a `ValueError` if the price is **zero or negative**.  
3. Implement **getter methods** using `@property`:  
   - `name`: Returns the product name.  
   - `price`: Returns the product price.  
4. Implement the `__str__` method:  
   - Returns a formatted string like: `"Product: Laptop - Price: $1200.99"`.  
5. Implement the `__dict__` method:  
   - Returns a dictionary representation of the product:  
     ```python
     {"name": "Laptop", "price": 1200.99}
     ```

---

### **2. Develop the `User` class**  
The `User` class represents a customer who registers in the store.  

1. The class must have **two private attributes**:  
   - `__username`: Stores the user's name.  
   - `__email`: Stores the user’s email.  
2. The constructor (`__init__`) must:  
   - Accept `username` as a parameter.  
   - Generate an email using the format: `username@example.com`.  
3. Implement **getter methods** using `@property`:  
   - `username`: Returns the username.  
   - `email`: Returns the email.  
4. Implement the `__str__` method:  
   - Returns a formatted string like: `"User: Alice - Email: alice@example.com"`.  
5. Implement the `__dict__` method:  
   - Returns a dictionary representation of the user:  
     ```python
     {"username": "Alice", "email": "alice@example.com"}
     ```

---

### **3. Develop the `ShoppingCart` class**  
The `ShoppingCart` class manages products added by the user.  

### **Requirements:**  
1. The class must have **one private attribute**:  
   - `__items`: A list that stores `Product` objects.  
2. The constructor (`__init__`) must:  
   - Initialize an empty list for `__items`.  
3. Implement an `add_product` method:  
   - Accepts a `Product` object and adds it to `__items`.  
4. Implement a `remove_product` method:  
   - Accepts a product name as a parameter.  
   - Removes the first matching product from `__items`.  
   - If no matching product is found, do nothing.  
5. Implement a `total_price` method:  
   - Iterates through all products in `__items` and calculates the total price.  
6. Implement the `__str__` method:  
   - Returns a formatted list of all products in the cart, followed by the total price.  
7. Implement the `__dict__` method:  
   - Returns a dictionary representation of the cart:  
     ```python
     {"items": [{"name": "Laptop", "price": 1200.99}], "total": 1200.99}
     ```

---

### **4. Develop the `Store` class**  
The `Store` class manages users, products, and interactions.  

### **Requirements:**  
1. The class must have **two attributes**:  
   - `products`: A list containing `Product` objects available for purchase.  
   - `users`: A dictionary storing `User` objects with usernames as keys.  
2. The constructor (`__init__`) must:  
   - Initialize `products` with a few sample products.  
   - Initialize an empty dictionary for `users`.  
3. Implement a `register_user` method:  
   - Accepts a `username` as input.  
   - If the username already exists, print `"Username already exists!"`.  
   - Otherwise, create a new `User` object, store it in `users`, and print the details.  
4. Implement a `show_products` method:  
   - Prints all available products.  
5. Implement a `run` method:  
   - Runs a menu-driven interface allowing users to:  
     - Register a new user.  
     - View available products.  
     - Add a product to their shopping cart.  
     - View the cart and total price.  
     - Exit the program.  

---

### **Expected Menu Output**
```
1. Register User
2. Show Products
3. Add Product to Cart
4. View Cart
5. Exit
Enter your choice: 1
Enter username: Alice
User registered successfully!
User: Alice - Email: alice@example.com
```

