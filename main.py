import tomllib

try:
    required_keys = ['name', 'url', 'mode', 'version', 'output_mode', 'substring_filter']
    required_keys_flags = [False] * 6
    with open("config.toml", 'rb') as config:
        data = tomllib.load(config)

    for key, param in data.items():
        if key not in required_keys:
            raise ValueError("Ошибка конфигурационного файла: неверное имя параметра!")
        required_keys_flags[required_keys.index(key)] = True
    
    if not all(required_keys_flags):
        raise ValueError("Ошибка конфигурационного файла: отсутствует параметр " + required_keys[required_keys_flags.index(False)] + "!")

except tomllib.TOMLDecodeError:
    print("Ошибка формата TOML-файла!")

for x,y in data.items():
    if(y):
        print(f"{x}: {y}")