# Text Summarization Project

## Summary:

This project leverages Samsun text dataset to train generative artifical intelligence model Google pegasus-cnn_dailymail for text summarization purposes. Within the Swagger UI you can submit a snippet of text, the model will output a summarized version of text. This model was created to gain experience in end to end machiine learning model creation with deployement.


## WorkFlow

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. update the main.py
8. Update the app.py

## How to run?

### STEPS:

Clone the repository


```bash
git@github.com:fkokro/Text_Summarization_Project.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n summary python=3.8 -y
```

```bash
conda activate summary
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

####
Author: Flomo Kokro <br/>
Data Scientist <br/>
Email: fkokro@yahoo.com

###
Credits to Krish Naik, full training can be found here: <br/>
youtube: https://www.youtube.com/watch?v=p7V4Aa7qEpw&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=19 <br/>
github: https://github.com/krishnaik06/Text-Summarization-NLP-Project/tree/main