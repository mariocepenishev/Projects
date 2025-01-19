def boarding_passengers(capacity, *groups):
    benefit_programs = {}
    total_boarded = 0

    for group in groups:
        num_passengers, program = group
        if num_passengers <= capacity:
            if program not in benefit_programs:
                benefit_programs[program] = 0
            benefit_programs[program] += num_passengers
            capacity -= num_passengers
            total_boarded += num_passengers
        if capacity == 0:
            break

    sorted_benefit_programs = sorted(benefit_programs.items(), key=lambda x: (-x[1], x[0]))

    result = "Boarding details by benefit plan:\n"
    for program, num_passengers in sorted_benefit_programs:
        result += f"## {program}: {num_passengers} guests\n"

    if total_boarded == sum(group[0] for group in groups):
        result += "All passengers are successfully boarded!"
    elif capacity == 0:
        result += "Boarding unsuccessful. Cruise ship at full capacity."
    else:
        result += f"Partial boarding completed. Available capacity: {capacity}."

    return result


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
