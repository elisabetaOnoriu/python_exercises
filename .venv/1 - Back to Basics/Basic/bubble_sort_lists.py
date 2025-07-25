def bubble_sort_lists():
    received_list = input("Enter a comma separated list that you would like to sort: ").split(", ")
    n = len(received_list)
    for i in range(n):
        for j in range(0, n- 1 - i):
            if received_list[j] > received_list[j + 1]:
                received_list[j], received_list[j + 1] = received_list[j + 1], received_list[j]
    print(f"Sorted list: {received_list}")

bubble_sort_lists()