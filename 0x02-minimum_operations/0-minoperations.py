def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    current = 1
    clipboard = 0

    while current < n:
        if n % current == 0:
            clipboard = current
            operations += 1
        current += clipboard
        operations += 1

    return operations
