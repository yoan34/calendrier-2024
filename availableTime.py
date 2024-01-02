

class AvailableTime:
    
    def __init__(self):
        self.times = {
            "MORNING_EARLY": {
                "project_ids": [1, 2, 6, 7],
                "available": 150,
            },
            "MORNING_TT": {
                "project_ids": [1, 2, 3, 4, 7, 8, 10],
                "available": 90,    
            },
            "MORNING_OS": {
                "project_ids": [8],
                "available": 30,    
            },
            "MIDI_OS": {
                "project_ids": [3, 6],
                "available": 45,    
            },
            "AFTERNOON_TT": {
                "project_ids": [1, 2, 6, 7],
                "available": 60,    
            },
            "AFTERNOON_OS": {
                "project_ids": [3, 8],
                "available": 45,
            },
            "TONIGHT": {
                "project_ids": [9, 10, 7, 4],
                "available": 30,    
            },
            "NIGHT": {
                "project_ids": [3, 6, 7, 9, 10],
                "available": 60,
            },
            "DAY_OFF": {
                "project_ids": [9, 10, 7, 4],
                "available": 120,    
            },
        }
        
    def get_available_by_week(self):
        total = 0
        for key, data in self.times.items():
            total += data["available"]
        return total
    
    def show_available_by_week(self):
        total = self.get_available_by_week()
        hour = total//60
        m = total - (60*hour)
        print(f"Total available by week {hour}h{m}")
    
if __name__ == "__main__":
    
    available_time = AvailableTime()
    total = available_time.get_available_by_week()
    available_time.show_available_by_week()