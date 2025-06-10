def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def main():
    user_input = input("Enter numbers separated by spaces: ")
    arr = list(map(int, user_input.split()))
    sorted_list = bubble_sort(arr)
    print("Sorted array is:", sorted_list)
if __name__ == "__main__":
    main()
