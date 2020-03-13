# Find the sum of the first 1000 perfect squares, starting with 1
def sum_upto_n(number):
    # return sum([booked_item * booked_item for booked_item in range(1, number+1)])
    """
        It’s making a list of every perfect square you’ve requested and summing them all.
        A list with 1000 perfect squares may not be large in computer-terms,
        but 100 million or 1 billion is quite a bit of information and can easily overwhelm
        your computer’s available memory resources. That’s what’s happening here.

        Thankfully, there’s a quick way to solve the memory problem.
        You just replace the brackets with parentheses:
    """
    return sum((i * i for i in range(1, number + 1)))


if __name__ == '__main__':
    print(sum_upto_n(1000))

