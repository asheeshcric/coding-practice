productRatings = [[4, 4], [1, 2], [3, 6]]
#productRatings.sort(key=lambda x: x[1])


def calculate_percentage(ratings):
    total = 0
    for reviews in ratings:
        total += reviews[0]/reviews[1]

    return total/len(ratings)


def min_reviews(productRatings, threshold):
    threshold /= 100
    # Sort the array based on the second element of each product review (i.e. the total element)
    productRatings.sort(key=lambda x: x[1])
    print('Original: ', productRatings)
    current_percentage = calculate_percentage(productRatings)
    addition = 0
    while current_percentage < threshold:
        # Add a five-star review
        for i, reviews in enumerate(productRatings):
            if reviews[0] < reviews[1]:
                productRatings[i][0] += 1
                productRatings[i][1] += 1
                break

        addition += 1
        # Sort based on whichever would generate the highest change in percentage, should come first
        productRatings.sort(key=lambda x: -((x[0]+1)/(x[1]+1) - x[0]/x[1]))
        print(productRatings)
        current_percentage = calculate_percentage(productRatings)

    return addition

print(min_reviews(productRatings, threshold=77))
