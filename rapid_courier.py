from collections import deque

packages_to_be_delivered = list(map(int, input().split()))
couriers = deque(map(int, input().split()))

total_weight_delivered = 0

while packages_to_be_delivered and couriers:
    package = packages_to_be_delivered[-1]
    courier = couriers[0]

    if courier >= package:
        total_weight_delivered += package
        couriers.popleft()
        packages_to_be_delivered.pop()

        if courier > package:
            new_capacity = courier - 2 * package
            if new_capacity > 0:
                couriers.append(new_capacity)
    else:
        total_weight_delivered += courier
        packages_to_be_delivered[-1] -= courier
        couriers.popleft()

print(f"Total weight: {total_weight_delivered} kg")

if not packages_to_be_delivered and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")
elif packages_to_be_delivered and not couriers:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: {', '.join(map(str, packages_to_be_delivered))}")
elif couriers and not packages_to_be_delivered:
    print(f"Couriers are still on duty: {', '.join(map(str, couriers))} but there are no more packages to deliver.")