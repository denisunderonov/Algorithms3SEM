function quickSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }    

    const opElementIndex = Math.floor(arr.length / 2);
    const opElement = arr[opElementIndex];
    
    const left = [];
    const right = [];
    const equal = [];

    for (let element of arr) {
        if (element < opElement) {
            left.push(element);
        } else if (element > opElement) {
            right.push(element);
        } else {
            equal.push(element);
        }
    }

    return [...quickSort(left), ...equal, ...quickSort(right)];
}

const array = [64, 34, 25, 12, 22, 11, 90];
console.log("Исходный массив:", array);
console.log("Отсортированный массив:", quickSort(array));