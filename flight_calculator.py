# Reject example:
# When first writing out this function, copilot made up its own formula for calculating flight time based on weight.
# This was not accurate, so I placed the forumula in a comment above the function, and it was created correctly.
def calculate_flight_time(weight_grams):
    """
    Calculate the flight time of a drone based on its weight in grams.

    Parameters:
    weight_grams (float): The weight of the drone in grams.

    Returns:
    float: The estimated flight time in minutes.
    """
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative.")
    
    flight_time = 180 - 0.1 * weight_grams
    return max(flight_time, 0)  # Edit: Ensure flight time is not negative by using the max function.

# Accept: Copilot did this perfectly.
def flight_time_table(max_weight_grams, step_grams):
    """
    Generate a table of flight times for drones of varying weights.

    Parameters:
    max_weight_grams (float): The maximum weight of the drone in grams.
    step_grams (float): The increment in weight for each row in the table.

    Returns:
    list of tuples: Each tuple contains (weight, flight_time).
    """
    if max_weight_grams < 0 or step_grams <= 0:
        raise ValueError("Max weight must be non-negative and step must be positive.")
    
    table = []
    for weight in range(0, int(max_weight_grams) + 1, int(step_grams)):
        flight_time = calculate_flight_time(weight)
        table.append((weight, flight_time))
    
    return table