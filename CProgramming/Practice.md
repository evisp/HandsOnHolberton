## 🍽️ Restaurant Menu Management – Tasks

In this exercise, you will write **modular functions** to manage a restaurant’s menu. These functions will let us add new menu items, display them, search for items, and update their details. Later, they can be combined into a bigger restaurant system.


### 1. Add a Menu Item

Write a function to add a new menu item to an array. Each item has:

* **name** (string)
* **price** (float)
* **availability** (1 = available, 0 = unavailable).

**Function Signature:**

```c
void addMenuItem(MenuItem menu[], int *size, char name[], float price, int available);
```

* `menu[]`: the array of menu items.
* `*size`: current number of items (increment it after adding).
* `name`: name of the new item.
* `price`: price of the new item.
* `available`: availability flag.


### 2. Display Menu

Write a function to print all menu items in a clear table format. Only show items marked as available.

**Function Signature:**

```c
void displayMenu(MenuItem menu[], int size);
```

* `menu[]`: array of menu items.
* `size`: current number of items in the menu.


### 3. Search Menu Item by Name

Write a function to search for a menu item by its name (case insensitive).

* Return the **index** of the item if found.
* Return **-1** if not found.

**Function Signature:**

```c
int searchMenuItem(MenuItem menu[], int size, char name[]);
```

* `menu[]`: array of menu items.
* `size`: current number of items.
* `name`: name of the item to search for.


### 4. Update Menu Item Price

Write a function to update the price of a menu item.

* If the item is found, update its price.
* If not found, do nothing.

**Function Signature:**

```c
void updateMenuItemPrice(MenuItem menu[], int size, char name[], float newPrice);
```


### 5. Mark Item as Available/Unavailable

Write a function to update the availability status of a menu item.

* Input: name of the item, new availability flag (1 or 0).

**Function Signature:**

```c
void setItemAvailability(MenuItem menu[], int size, char name[], int available);
```


## **Struct Definition**

Use this struct for menu items:

```c
#define MAX_NAME_LEN 50

typedef struct {
    char name[MAX_NAME_LEN];
    float price;
    int available; // 1 = available, 0 = unavailable
} MenuItem;
```
