def r(arr, length, index, flip, even, count):
        if index >= length:
            return count
        a = arr[index]
        b = arr[index+1]
        print(a, b)
        if flip:
            if even:
                if a < b:
                    count += 1
                else:
                    return count
            else:
                if a > b:
                    count += 1
                else:
                    return count
        else:
            if even:
                if a > b:
                    count += 1
                else:
                    return count
            else:
                if a < b:
                    count += 1
                else:
                    return count
        count += r(arr, length, index+1, flip, not even, 0)
        return count
