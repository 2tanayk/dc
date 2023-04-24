#Multithreading
import threading

# Create thread functions to calculate squares and cubes
def cubes(num):
    print(num**3)

def square(num):
    print(num**2)
    
# Create and start threads 
square_thread = threading.Thread(target=square, args=(100000,))
cube_thread = threading.Thread(target=cubes, args=(200000,))
square_thread.start()
cube_thread.start()

# Wait for the threads to finish
square_thread.join()
cube_thread.join()
