"""
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature, set_temperature)


class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

"""
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.__temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value


if __name__ == '__main()__':
    c = Celsius()
    c.set_temperature(-333)
    c.temperature = -332
    print(c.temperature)
    print(c.__temperature)

"""
export PROJECT_ID=spatial-range-235523
export MODEL_PATH=gs://ai_platform_output
export MODEL_NAME=quake
export VERSION_NAME=v1
export REGION=us-central1

gsutil cp gs://dataprep-staging-2a3e2ace-5f3b-4ea7-8329-25547cdcd64b/starcraft2@protonmail.com/clean_slate/train_labels_clean.csv
./earthquake_data
"""