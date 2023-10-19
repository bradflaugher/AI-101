# Data Wrangling 📊

---

## Scraping Data 🕷️
* Extracting data from websites
```python
import requests
from bs4 import BeautifulSoup

url = 'https://example.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find_all('div', class_='data-class')
```

---

## Working with APIs 🖥️
* Accessing data from online services
```python
import requests

api_url = 'https://api.example.com/data'
response = requests.get(api_url)
api_data = response.json()
```

---

## Python Requests 📬
* A simple HTTP library for Python
```python
import requests

response = requests.get('https://example.com/data.csv')
with open('data.csv', 'wb') as file:
    file.write(response.content)
```

---

## Combining Datasets 📚
* Merging multiple datasets into one
```python
import pandas as pd

df1 = pd.read_csv('data1.csv')
df2 = pd.read_csv('data2.csv')
merged_df = pd.merge(df1, df2, on='common_column')
```

---

## Synthetic (AI-Generated) Datasets 🤖
* Creating datasets using AI
```python
import openai
import pandas as pd

openai.api_key = 'your-api-key'

prompt = "Generate 50 positive and 50 negative sentences about a movie."

# Request to OpenAI API
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=400,
    temperature=0.7,
    n=1
)
text = response['choices'][0]['text'].strip().split('\n')
data = [(sentence, 'positive' if i < 50 else 'negative') for i, sentence in enumerate(text)]
df = pd.DataFrame(data, columns=['text', 'sentiment'])
df.to_csv('synthetic_data.csv', index=False)

```

---

## Important Data Sources 📑

---

### Free Captioned Images 🌐
* [LAION](https://laion.ai/)

---

### The Entire Web, Scraped 🕸️
* [Common Crawl](https://commoncrawl.org/) via [comcrawl](https://github.com/michaelharms/comcrawl)

---

### Specialized Data Collections 📚
* [Datahub](https://datahub.io/collections)
* [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets)
* [Huggingface Datasets](https://huggingface.co/datasets)
* [Huggingface Tutorial](https://huggingface.co/docs/datasets/tutorial)

---

# END
