function insertionSort(arr) {
    for (let i = 1; i < arr.length; i++) {
        let current = arr[i];
        let j = i - 1;
        
        while (j >= 0 && arr[j] > current) {
            arr[j + 1] = arr[j];
            j--;
        }
        
        arr[j + 1] = current;
    }
    return arr;
}

const array = [64, 34, 25, 12, 22, 11, 90];
console.log("Исходный массив:", array);
console.log("Отсортированный массив:", insertionSort(array));