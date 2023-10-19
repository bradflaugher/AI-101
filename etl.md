# ETL and "It's all numbers, man" 🧮

---

## ETL Overview ⬇️⬆️
* ETL: Extract, Transform, Load
* Download, change, upload... The cycle of data handling

---

## ETL Example: Command Line 🖥️
```bash
# Download CSV
wget https://example.com/data.csv -O data.csv

# Transform: Change units using Python
python transform.py data.csv transformed_data.csv

# Upload to S3
aws s3 cp transformed_data.csv s3://my-bucket/transformed_data.csv
```

---

## Why is ETL Hard? 🤔
* Learning curve
* Is ETL a legacy problem?
* Numerous data sources... endless possibilities

---

## Demonstrations: Data Types 🔄

---

### [Numbers are Data](/data_types/data_loading_preprocessing.ipynb) 🔢

---

### [Text are Data](/data_types/data_loading_preprocessing.ipynb) 📜
```
from sklearn.preprocessing import LabelEncoder 

CATEGORICAL_COLUMNS = ['name']

for column in CATEGORICAL_COLUMNS:
    number = LabelEncoder()
    lang_df[column] = number.fit_transform(lang_df[column].astype('str')).astype(float)
    print(column)
    
    #Save your encodings!!!!
    le_name_mapping = dict(zip(number.classes_, number.transform(number.classes_)))
    with open(column+'_encoding.txt', 'w') as f:
        counter = 0
        for item in le_name_mapping:
            f.write("%s\n" % (item + ": " + str(counter)))
            counter+=1
    print(le_name_mapping)

name
{'Cristiano': 0, 'Jimbo': 1, 'Josef': 2, 'Maria': 3}

```

---

### [Images are Data](/data_types/data_loading_preprocessing.ipynb)
```python
image_df = pd.DataFrame([["zelensky.jpg"],["biden.jpg"]], columns=["filename"])
image_df.head()
PIL.Image.open(os.path.join(os.getcwd(), str(image_df.filename[0])))
img_height = 200
img_width = 200

images = []
for image_path in list(image_df.filename):
    full_path = os.path.join(os.getcwd(),image_path)
    image = tf.keras.preprocessing.image.load_img(full_path,color_mode='rgb',target_size=(img_height,img_width))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    images.append(input_arr)

x = images
print(x)
```

---

### An "Image"
```
[array([[[ 13.,  53., 167.],
        [ 11.,  53., 173.],
        [ 17.,  60., 198.],
        ...,
        [ 35., 100., 252.],
        [ 35., 100., 252.],
        [ 35., 100., 252.]],

       [[ 13.,  53., 175.],
        [ 13.,  54., 180.],
        [ 19.,  62., 200.],
        ...,
        [ 35., 100., 252.],
        [ 35., 100., 252.],
        [ 35., 100., 252.]],
```

---

### Another "Image"

```
  11111  
 1 0 0 1 
1  1 1  1
1 11111 1
 1     1 
  11111  
```

---

## Introduction to Pandas 🐼
* Data manipulation and analysis library
* Why do we use it?

```python
import pandas as pd
df = pd.read_csv('data.csv')
df.head()
```

---

## Discussion: Data Collection, ETL, and "Glue Code" 🗂️
* The glue that holds data projects together
* Bridging the gap between raw data and actionable insights

---

# END
