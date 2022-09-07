# Discourse Annotation

This applet is meant to be the prototype platform that works locally for the annotators to perform a specific annotation task that involves Reddit conversations.

## Installation

### Usage (First Time) : 

#### Step 1: Create a virtual environment and activate it.
```bash
conda create -n <name> python=3.9
conda activate <name>
```

#### Step 2: Install the dependencies.

```bash
pip install requirements.txt
```
#### Step 3: Download the working dataset.
Please refer to the progress sheet in case you are doing your second round of annotation(sub-problem or nodes/edges).
```
Sagar Sanskar
```
#### Step 4: Run the app.

Give it a little time and then you'll see a selectbox at the left pane in the application prompting you to select an annotation type. Please make sure that you select on the work that is listed in the Gsheet to prevent any confusions later on. Just a safety measure to keep checking the sheet so that none of your work goes waste due to some silly logisitical error.

```
streamlit run app/intro.py
```

#### Step 5: Update your progress in the Gsheet
The app will not reload your progress if you leave the app in the middle of a conversation. So it is suggested to wrap up the conversation and only then end the session(close the application). The app will load from the conversation that you were supposed to do next before the break.

Make sure that you click on the exit button and wait for the success message to pop up with ballons on your screen. This suggests that the data has been updated locally. 
- If you are still left with some portions, don't worry everyone needs a little break! You don't have to do anything else.
- If you are done with the entire batch then simply upload the data folder in the gdrive[link] using the following naming conventions : TBD

TBD : 
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
