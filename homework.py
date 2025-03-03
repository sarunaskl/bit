import requests  # Import the requests library to handle HTTP requests

def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"  # URL of the API that provides TODO data
    response = requests.get(url)  # Send an HTTP GET request to the API and store the response
    
    if response.status_code == 200:  # Check if the request was successful (status code 200 means OK)
        todos = response.json()  # Parse the response JSON data into a Python list
        for todo in todos[:10]:  # Loop through the first 10 TODO items
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")  # Print TODO details
    else:
        print("Failed to fetch data")  # Print an error message if the request was not successful

if __name__ == "__main__":  # Ensure the script runs only when executed directly, not when imported as a module
    fetch_todos()  # Call the function to fetch and display TODO items
