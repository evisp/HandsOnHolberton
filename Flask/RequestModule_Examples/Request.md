# Python Exercises Using JSONPlaceholder API

## Overview
This set of exercises will help you practice working with APIs, data structures, and file handling in Python. You'll start with basic API requests and move on to more advanced tasks involving dictionaries, sorting, and JSON file manipulation.

---

## 1️⃣ Fetch and Print User Posts (Basic API Request)
**Objective:** Learn how to make a basic API request and extract specific data.

### Requirements:
- Fetch all posts for `userId=1` from the API.
- Print only the titles of the posts.
- Use the `requests` library.

**API Endpoint:** `https://jsonplaceholder.typicode.com/posts?userId=1`

---

## 2️⃣ Count Comments per Post (Dictionaries, API)
**Objective:** Work with JSON data and count occurrences using a dictionary.

### Requirements:
- Fetch all comments from the API.
- Count how many comments exist for each `postId`.
- Store the results in a dictionary where keys are `postId` and values are the number of comments.
- Print the result.

**API Endpoint:** `https://jsonplaceholder.typicode.com/comments`

---

## 3️⃣ Save Users to a File (File Handling, API)
**Objective:** Fetch and store data in a text file.

### Requirements:
- Fetch all users from the API.
- Save their names and emails in a text file (`users.txt`).
- Each line in the file should be formatted as:
  
  ```plaintext
  Name: Leanne Graham, Email: Sincere@april.biz
  ```

**API Endpoint:** `https://jsonplaceholder.typicode.com/users`

---

## 4️⃣ Find the Most Active User (Sorting, Dictionaries, API)
**Objective:** Process API data and find a specific pattern.

### Requirements:
- Fetch all posts from the API.
- Determine which user (`userId`) has written the most posts.
- Print the user ID and the number of posts.

**API Endpoint:** `https://jsonplaceholder.typicode.com/posts`

---

## 5️⃣ Fetch and Merge User Data (JSON, Advanced API Handling)
**Objective:** Combine data from multiple API endpoints and store it in JSON format.

### Requirements:
- Fetch all users from the API.
- Fetch all posts from the API.
- Create a JSON file (`user_posts.json`) where each user has:
  - Their `id`, `name`, and a list of their post titles.
- Example JSON structure:
  
  ```json
  [
    {
      "id": 1,
      "name": "Leanne Graham",
      "posts": ["Post Title 1", "Post Title 2"]
    }
  ]
  ```

**API Endpoints:**  
- Users: `https://jsonplaceholder.typicode.com/users`  
- Posts: `https://jsonplaceholder.typicode.com/posts`

---

