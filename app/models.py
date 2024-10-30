class Staff:
    def __init__(self, name, preferences, max_hours):
        self.name = name
        self.preferences = preferences  # e.g., {'shift': 'morning'}
        self.max_hours = max_hours  # e.g., 40 hours per week
        self.schedule = []  # This will store the generated shifts
