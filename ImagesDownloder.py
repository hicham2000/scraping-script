import os
import requests
folder_name = "imagess"


url = "https://i.imgflip.com/7uumcv.gif"


for i in range (1,20):
    file_name = "image"+str(i)+".gif"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    path = os.path.join(folder_name, file_name)

    response = requests.get(url)
    if response.ok:
        with open(path, 'wb') as f:
            f.write(response.content)
            print(f"Image saved successfully in '{folder_name}' folder as '{file_name}'.")
    else:
        print("Failed to download the image.")
