**Token Healing Algorithm**

I have written a token healing algorithm which performs two major tasks of context aware spell check using Spark NLP and grammer check using GingerIt. I had worked on Colab notebook throughout the entire process but have also compiled the work locally.

Just a heads up, only go with cloning this repo and working on your local system if you have Pyspark installed and setup. It is really a hassle to get it to work properly. Although I believe the local version works as intended, I haven't checked it since I was having a really bad time figuring out Pyspark. The colab version works perfectly fine.

To begin with, please make yourself a Python venv.
```
python -m venv venvname
```
Or if you're a conda enthusiast, go ahead with that.

Activate your venv with commands corresponding to your OS. Check [this](https://docs.python.org/3/library/venv.html#creating-virtual-environments) for more info on how to.

Once your virtual environment is activated, go ahead and install all the dependencies.
Run
```
pip install -r requirements.txt
```
this should install all the dependencies required.

NOTE: this does not include Pyspark as I'm hoping you have it installed and setup in your local machine already.

Just to make sure we're on the same path, you can perform
```
pip list
```

and you would find something like this

![image](https://github.com/9dubs/token-healing/assets/103320629/46545b58-3742-4f05-bb7b-aa307aa28416)

Okay now cd into **tokenhealing** and open main.py in your preferred IDE. On line 23, you could see the **'text'** variable. Assign any string to it. Make sure you have included some intentionally misspelled words!

Once you have done that, go ahead and run main.py by
```
python main.py
```

Just for the sake of it, I'll leave an example below,
```
text = "I will gone tomorow"
```
and the output is,

![image](https://github.com/9dubs/token-healing/assets/103320629/f6c08730-a24c-49ba-97a1-038cf114e6ba)

Go ahead and give it a try!

Note: The pipeline is really basic and would not be able to handle complex sentences.

On regards to how I have built the Spark NLP pipeline, visit my [colab file](https://colab.research.google.com/drive/1bkUl3Dtb2wu7dbNfV2qmNb2SvrM9PdL6?usp=sharing) where I have documented every single line. You can go ahead, create a copy and run each of those cells to see the same result!

