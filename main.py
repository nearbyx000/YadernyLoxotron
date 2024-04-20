from roboflow import Roboflow
from colorama import *
import colorama

colorama.init()

rf = Roboflow(api_key='lLbRrC8N05TcRCsxBSvW')
project = rf.workspace().project('smoker_detection-c5aok')
model = project.version(3).model

for i in range(4):
    a = str((model.predict('img/test/' + str(i+1) + '.jpg').json()))
    print(Fore.WHITE + a)

    if 'no_smoke' in a:
        print(Fore.GREEN + 'не курит')
        print('не курит с вероятностью', float(a[a.index("confidence': ") + 13:a.index("confidence': ") + 13 + 5]) * 100, '%')
    elif 'smokers' in a:
        print(Fore.RED + 'курит')
        print('курит с вероятностью', float(a[a.index("confidence': ") + 13:a.index("confidence': ") + 13 + 5]) * 100, '%')
    else:
        print(Fore.YELLOW + 'не удалось определить')

input()