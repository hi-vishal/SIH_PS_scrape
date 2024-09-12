from bs4 import BeautifulSoup
import pandas as pd

url = "sih.html"
with open(url, 'r', encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content, 'html.parser')

table = soup.find_all('table')
final_result = {}

col = ['Problem Statement ID', 'Category', 'Theme', 'Problem Statement Title', 'Organization']
df = pd.DataFrame(columns=col)

for t in table:
    titles = soup.find_all('th')
    table_titles = [t.text.strip() for title in titles]

    output1 = [item.replace('\n\n', '\n') for item in table_titles]
    output1 = output1[0].strip().split('\n')
    output1 = [item for item in output1 if item.strip()]
    if len(output1)%2!=0:
        if output1[-1]=='':
            output1 = output1[:-1]
        else:
            output1.append('')
    result = {output1[i]: output1[i+1] for i in range(0, len(output1), 2)}

    filtered_result = {k: v for k, v in result.items() if k in ['Problem Statement ID', 'Category', 'Theme', 'Problem Statement Title', 'Organization']}

    #print(filtered_result)
    new_row = {col: filtered_result.get(col, '') for col in df.columns}
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

df.to_excel('output.xlsx', index=False)
print("saved")