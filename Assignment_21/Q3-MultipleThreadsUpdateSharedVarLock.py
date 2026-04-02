import threading


shared_counter = 0

counter_lock = threading.Lock()

def increment_task(num_increments):
    
    global shared_counter

    for i in range(num_increments):
        
        with counter_lock:             # Use the 'with' statement for automatic acquire and release
            shared_counter += 1

def main():
    threads = []
    num_threads = 5
    increments_per_thread = 100000

    # Create and start threads
    for i in range(num_threads):
        t = threading.Thread(target=increment_task, args=(increments_per_thread,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print(f"Final value of shared counter: {shared_counter}")
    print(f"Expected value: {num_threads * increments_per_thread}")

if __name__ == "__main__":
    main()
