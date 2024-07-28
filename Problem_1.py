class Sensor:
    comfort_temperature_range = (20, 24)  

    def __init__(self, sensor_id, sensor_type, current_reading):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.current_reading = current_reading

    def get_reading(self):
        return self.current_reading

    def update_reading(self, new_reading):
        self.current_reading = new_reading

    @staticmethod
    def get_average_temperature(sensors):
        temp_sensors = [sensor for sensor in sensors if sensor.sensor_type == 'temperature']
        if not temp_sensors:
            raise ValueError("Input list must contain only Temperature sensors")
        
        total_temp = sum(sensor.get_reading() for sensor in temp_sensors)
        average_temp = total_temp / len(temp_sensors)
        return average_temp

# Example usage
if __name__ == "__main__":
    sensors = [
        Sensor(1, 'temperature', 22),
        Sensor(2, 'temperature', 23),
        Sensor(3, 'temperature', 21),
        Sensor(4, 'light', 150),
        Sensor(5, 'humidity', 45)
    ]
    
    try:
        average_temp = Sensor.get_average_temperature(sensors)
        comfort_min, comfort_max = Sensor.comfort_temperature_range
        
        if average_temp < comfort_min:
            print("Temperature is low")
        elif average_temp > comfort_max:
            print("Temperature is high")
        else:
            print("Comfortable temperature")
    except ValueError as e:
        print(e)
