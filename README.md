# Discourse Annotation

This applet is meant to be the prototype platform that works locally for the annotators to perform a specific annotation task that involves Reddit conversations.

## Installation

### Usage (First Time) : 

#### Step 1: Create a virtual environment and activate it.
It is better to have a virtual env set up so that the other versions on your machine don't lead to nasty errors when working with this repo. You can do so using : 
Option 1 : `Conda` - Follow the steps listed [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
Option 2 : `Terminal` - Follow the stpes listed [here](https://realpython.com/intro-to-pyenv/)  
#### Step 2: Install the dependencies.
```bash
pip install requirements.txt
```
#### Step 3: Download the working dataset.

Please delete all the sample data from the data folder first before downloading the new data.Make sure that you download the data in the `data` folder and not elsewhere.

```
Sagar Sanskar
```
#### Step 4: Run the app.
```
streamlit run app/intro.py
```
Please be careful in selecting the kind of annotation you would be performing. 

1. The `sub_problem` page in the app is dedicated to the sub-problem identification
2. The `nodes_edge` page in the app is dedicated  to the node and edge identification
3. The `info` page contains all the guidlines needed for the annotation process. It is recommned to refer to this tab every once in a while after each conversation so that you get acquainted with the schema quickly.
#### Step 5: Update your progress in the Gsheet

Color code the ones that are done as "Green" in your specific column for the specific conversation. Link :  Sagar Sanskar

### Resuming your previous work : 
These are the steps for when you have already done the steps above but are already how you to utilize the app but you had to take a pause and now you're back to it.

#### Step 6: Always activate the virtual environment 
```
code
```
#### Step 7: Use the app as intended.
Follow the same convention i.e. Step 4 followed by Step 5.

### What next, when done with one batch?
Upload it to the drive - Here
Use the nomenclature based on the scheme from other members - `<Your initials>_<Batch_Code>`. For example, Arpit Patel would have a file name `AP_A32`. 

Follow the annotation scheme to pick up the next batch. - Here


## Roadmap
TBA

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. I will soon update some pointers on how we could refine this platform for better accessibility and scalability.
