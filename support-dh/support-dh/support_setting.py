color_dic = {
    'BLACK': "\033[30m",
    'RED' : "\033[31m",
    'GREEN' : "\033[32m",
    'BROWN' : "\033[33m",
    'BLUE' : "\033[34m",
    'PURPLE' : "\033[35m",
    'CYAN' : "\033[36m",
    'LIGHT_GRAY' : "\033[0;37m",
    'DARK_GRAY' : "\033[1;30m",
    'LIGHT_RED' : "\033[1;31m",
    'LIGHT_GREEN' : "\033[1;32m",
    'YELLOW' : "\033[1;33m",
    'LIGHT_BLUE' : "\033[1;34m",
    'LIGHT_PURPLE' : "\033[1;35m",
    'LIGHT_CYAN' : "\033[1;36m",
    'LIGHT_WHITE' : "\033[1;37m",
    'BOLD' : "\033[1m",
    'FAINT' : "\033[2m",
    'ITALIC' : "\033[3m",
    'UNDERLINE' : "\033[4m",
    'BLINK' : "\033[5m",
    'NEGATIVE' : "\033[7m",
    'CROSSED' : "\033[9m",
    'END' : "\033[0m"}

def printd(text: str, color: str = 'LIGHT_GRAY', more_parameter: list = []) -> None:
    """
    지원되는 색상       
    |red|green|blue|
    |---|---|---|
    |빨간색|초록색|파란색|
    """
    result = f'{color_dic[color.upper()]}{text}'
    if 0 != len(more_parameter):
        for p in more_parameter:
            result = f'{color_dic[p.upper()]}{result}'
    result += color_dic["LIGHT_GRAY"]
    print(result)




if __name__ == "__main__":
    printd('text', color='red')
    printd('test', color='green', more_parameter=['bold'])