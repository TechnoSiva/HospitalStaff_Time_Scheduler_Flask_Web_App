import random
import math

# Function to evaluate how good a schedule is (lower score is better)
def evaluate_schedule(schedule, staff_list):
    cost = 0
    for staff, shift in schedule.items():
        # Penalize if the shift is not their preferred shift
        preferred_shift = next(s.preferences['shift'] for s in staff_list if s.name == staff)
        if shift != preferred_shift:
            cost += 10  # Higher penalty for not matching preference
    return cost

def random_schedule(staff_list):
    shifts = ['morning', 'afternoon', 'night']
    return {staff.name: random.choice(shifts) for staff in staff_list}

def neighbor_schedule(current_schedule):
    # Modify the current schedule slightly to generate a neighboring solution
    new_schedule = current_schedule.copy()
    random_staff = random.choice(list(current_schedule.keys()))
    shifts = ['morning', 'afternoon', 'night']
    new_schedule[random_staff] = random.choice(shifts)
    return new_schedule

def acceptance_probability(current_energy, new_energy, temperature):
    if new_energy < current_energy:
        return 1
    return math.exp((current_energy - new_energy) / temperature)

def simulated_annealing_schedule(staff_list):
    # Simulated Annealing Parameters
    initial_temperature = 1000
    cooling_rate = 0.95
    min_temperature = 1

    # Start with a random initial schedule
    current_schedule = random_schedule(staff_list)
    best_schedule = current_schedule
    current_temperature = initial_temperature

    while current_temperature > min_temperature:
        # Generate a neighboring schedule
        new_schedule = neighbor_schedule(current_schedule)

        # Calculate the cost (energy) of current and new schedules
        current_energy = evaluate_schedule(current_schedule, staff_list)
        new_energy = evaluate_schedule(new_schedule, staff_list)

        # Accept the new schedule based on probability
        if new_energy < current_energy or random.uniform(0, 1) < acceptance_probability(current_energy, new_energy, current_temperature):
            current_schedule = new_schedule

        # Keep track of the best schedule found
        if evaluate_schedule(current_schedule, staff_list) < evaluate_schedule(best_schedule, staff_list):
            best_schedule = current_schedule

        # Cool down
        current_temperature *= cooling_rate

    return best_schedule

def generate_schedule(staff_list):
    return simulated_annealing_schedule(staff_list)
