# bootcamp

Lecture notes, readings, code samples and resources for [Brad Flaugher's Data-Focused Programming Bootcamp](https://bradflaugher.com/bootcamp.html)


# Course Outline

## Preparation

* (Required) Install Ubuntu Linux on your PC, [Install Guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview), and [additional notes for dual-booting with Windows](https://linuxconfig.org/how-to-install-ubuntu-20-04-alongside-windows-10-dual-boot) NOTE if you have an M1 Mac this will be almost impossible, so sell that thing or talk to Brad.
* (Required) Install Docker [Install docker Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
* (Required) Read [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* (Required) If you are not a proficient Python coder please do the entire futurecoder.io course, it's free! [Futurecoder.io](https://futurecoder.io/course/)
* (Required) if you have never used a Jupyter notebook before, please read [Jupyter Notebooks Getting Started Tutorial](https://jupyter.org/try)
* (Required) learn how to use git if you never have before. [Git and GitHub for beginners crash course](https://www.youtube.com/watch?v=RGOj5yH7evk)
* (Required)if you do not have experience with SQL please take the [Interactive SQL course @ Codecademy](https://www.codecademy.com/learn/learn-sql)

## Intro - The 30,000 foot view of Data and AI 

### Topics
* Definitions: Data Scientist, Data Engineer, Data Analyst, Data Janitor
* Definitions: Machine Learning and Artificial Intelligence
* Why Neural Networks? Single Cell Neural Network aka Regression in Excel
* Intro to Fundation Models: ImageNet, BERT, LLaMA and Stable Diffusion
* Why Python? Python and C Speed Test
* Why SQL? SQL, what it is and why it's important (PowerBI, Tableau, Athena, BigQuery)
* Why Open Source? [The FSF](https://www.fsf.org/) and [Richard Stallman](https://stallman.org/) and [Buy vs Build Philosophy](B_FOSS/AI_Tool_Providers.png)
* Why Linux and Docker? [Why use Docker for Machine Learning Development?](https://aws.amazon.com/blogs/opensource/why-use-docker-containers-for-machine-learning-development/)

### Readings
* [Intro to Deep Learning](https://www.youtube.com/watch?v=qj5gUDJ5TnU)
* [Is it all just a big regression?](https://www.reddit.com/r/MachineLearning/comments/xrge5d/d_is_neural_network_really_smart_or_just_some/)
* [9 Reasons why you'll never be a data scientist](https://towardsdatascience.com/9-reasons-why-youll-never-become-a-data-scientist-c8c5b75503cf)

## Foundations - "You've got to have a setup" David Lynch 

### Pop Quiz: can you?
* [ ] Start a Github Project?
* [ ] Commit from the command line?
* [ ] Run a docker container?
* [ ] Load a csv file into pandas?
* [ ] Inspect a large csv file in the command line?
* [ ] Start and close vim?

### Topics
* Buying Computers
* Linux and Docker Setup
* IDEs vs Vim
* Git and Github
* Notebooks and ```.py``` files
* ```ssh``` and ```scp```
* Stackoverflow, ChatGPT, Copilot etc...
* Cloud providers and [Spotty](https://github.com/spotty-cloud/spotty)

## Picking Projects and Reading Code

### Possible Bootcamp Projects
* ⭐ [Contribute to data collection for Open-Assistant](https://github.com/LAION-AI/Open-Assistant#contributing-to-data-collection)
* ⭐⭐[Instruct-tune LLaMA on consumer hardware](https://github.com/tloen/alpaca-lora)
* ⭐⭐⭐ [Tensorflow Text Classifier Tutorial](https://www.tensorflow.org/tutorials/keras/text_classification) or [Tensorflow Image Classifier Tutorial](https://www.tensorflow.org/tutorials/keras/classification)
* ⭐⭐⭐⭐ [PyTorch Text Classifier](https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html)
* ⭐⭐⭐⭐[Fine-Tune a Pretrained Model](https://huggingface.co/docs/transformers/training)
* ⭐⭐⭐⭐⭐[Replicate a Winning Model from Kaggle](https://www.kaggle.com/code?types=competitions)

## The Universal Machine Learning Workow

### Readings
* [The Universal Machine Learning Workflow](https://www.oreilly.com/library/view/deep-learning-with/9781617296864/Text/06.xhtml)
* [How Deep Learning Works](https://www.youtube.com/watch?v=wBgW3ZtlPT8)

## ETL and "It's all numbers, man" 

### Topics
* ETL: aka Download, change, upload... give command line example with wget csv, python change units, s3 upload.
* Why is it hard to learn ETL? is ETL a legacy problem? How many data sources can there possibly be?
* Demonstration: Numbers are Data
* Demonstration: Text is Data
* Demonstration: Images are Data
* Pandas: what is it and why do we use it?
* Discussion: Data Collection, ETL and "glue code"

### Code Reading
* [Preprocessing Notebook](/3_Data_Types/data_loading_preprocessing.ipynb)

### Useful Tutorials 
* [Freecodecamp Pandas 10 hour course](https://www.freecodecamp.org/news/how-to-analyze-data-with-python-pandas/)
* [Airflow Tutorial for Beginners](https://www.youtube.com/watch?v=K9AnJ9_ZAXE)

## Data Wrangling 

### Topics
* Scraping Data
* APIs
* Python Requests
* Combining datasets

### Data Sources
* Free captioned images from the web, [LAION](https://laion.ai/)
* The entire web, scraped for you, [Common Crawl](https://commoncrawl.org/) via [comcrawl](https://github.com/michaelharms/comcrawl)
* More specialized data... [Datahub](https://datahub.io/collections) and [Awesome pubilc datasets](https://github.com/awesomedata/awesome-public-datasets) and [Huggingface Datasets](https://huggingface.co/datasets) and (Huggingface)[https://huggingface.co/docs/datasets/tutorial]

### Readings
* [Python Requests Tutorial](https://www.geeksforgeeks.org/python-requests-tutorial/)

## Neural Network Model Architecture

### Topics
* Definition: [Accuracy](https://medium.datadriveninvestor.com/accuracy-trap-pay-attention-to-recall-precision-f-score-auc-d02f28d3299c), [Precision, Recall, F1](https://emkademy.com/research/toolbox/2020-03-02-accuracy-precision-recall), [AUC](https://paulvanderlaken.com/2019/08/16/roc-auc-precision-and-recall-visually-explained/)
* Definition: [Confusion Matrix](https://www.statology.org/confusion-matrix-python/)... [in Tensorflow too](https://www.tensorflow.org/tutorials/audio/simple_audio#display_a_confusion_matrix)
* Discussion: Loss functions vs model metrics?
* Discussion: How do you measure model performance with other ML techniques? (Back to Excel Nerual Net for a moment) then [Custom Loss Functions](https://stackoverflow.com/questions/53980031/pytorch-custom-loss-function) and [Custom Loss Functions #2](https://discuss.pytorch.org/t/custom-loss-functions/29387/3)
* Discussion: "The Price is Right" Loss Function?
* Discussion: Layer Types and Standard or Template Models
* Discussion: Where to start, how to adjust hyperparameters
* Discussion: How can you steal ideas?

### Current Events and Discussions in the Community
* [When was the last time you wrote a custom neural net?](https://www.reddit.com/r/MachineLearning/comments/yto34q/d_when_was_the_last_time_you_wrote_a_custom/)
* [Do you think there is a competitive future for smaller, locally trained/served models?](https://www.reddit.com/r/MachineLearning/comments/yon48p/d_do_you_think_there_is_a_competitive_future_for/)
* [What are the major general advances in ML techniques?](https://www.reddit.com/r/MachineLearning/comments/ylixp5/d_what_are_the_major_general_advances_in/)

### Readings
* [Modeling Natural Language](https://www.youtube.com/watch?v=rqyw06k91pA)

# Final Projects

Bootcampers will spend a tremendous time working on final projects that are targeted to the bootcamper's career goals. For an example final presentation see [Oleh's Video (YouTube)](https://www.youtube.com/watch?v=I-KL-mWF548) and [Oleh's Repository (GitHub)](https://github.com/MorhaliukOL/ML_Project).

You can also see more final project presentations and source code on [Brad's Youtube Channel](https://www.youtube.com/@bradflaugher2452/videos).

# After The Bootcamp

## Recommended courses, videos and books

### Computer Science Fundamentals
* [OSSU Computer Science Curriculum](https://github.com/ossu/computer-science)
* [Learn Python Basics withGoogle](https://learndigital.withgoogle.com/digitalgarage/course/learn-python-basics-for-data-analysis)

### Data Janitoring
* [Fundamentals of Data Engineering](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
* [Python Data Cleaning Cookbook](https://learning.oreilly.com/library/view/python-data-cleaning/9781800565661/)

### Model Training
* [Tensorflow Tutorials](https://www.tensorflow.org/tutorials)
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [Microsoft ML For Beginners](https://github.com/microsoft/ML-For-Beginners)
* [Deep Learning Illustrated](https://www.amazon.com/Deep-Learning-Illustrated-Intelligence-Addison-Wesley/dp/0135116694) and [Deep Learning with Tensorflow, Pytorch etc..](https://learning.oreilly.com/videos/deep-learning-with/9780136617617/)
* [Machine Learning Crash Course with Google](https://learndigital.withgoogle.com/digitalgarage/course/machine-learning-crash-course)
* [HuggingFace Course on Transformers](https://huggingface.co/course/chapter0/1?fw=pt)
* [Natural Language Programming Demystified](https://www.nlpdemystified.org/course)
* [Neural Networks: Zero to Hero](https://karpathy.ai/zero-to-hero.html)

### Background Math
* [Stanford ML Lectures, 2018](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
* [Math for Machine Learning](https://learning.oreilly.com/playlists/b1c03a16-8f1d-44af-b97b-67aed9bace2e/)

### Operationalizing ML with MLFlow and MLOps tools
* [Practical MLOps](https://learning.oreilly.com/library/view/practical-mlops/9781098103002/)
* [Practical Deep Learning with MLFlow](https://learning.oreilly.com/library/view/practical-deep-learning/9781803241333/)

### Ethics and AI
* [Ethical Machines](https://www.reidblackman.com/ethical-machines/)
* [The Alignment Problem](https://brianchristian.org/the-alignment-problem/)

## Recommended Mailing lists and online groups
* [Deep Learning Weekly](https://www.deeplearningweekly.com/)
* [Reddit Machine Learning](https://www.reddit.com/r/MachineLearning/)
* [Hacker News (it's less focused on ML, but worth your time generally)](https://news.ycombinator.com/)
* [Reddit Programming (same as above)](https://www.reddit.com/r/programming/)

## Recommended Professional Groups
* [ACM](https://www.acm.org/)
* [Women in Data](https://www.womenindata.org/)

## Recommended (in-person) Conferences
* [Ai4](https://ai4.io/)
* [NeurIPS](https://neurips.cc/)

## Highly Recommended Job Boards
* [LinkedIn](https://www.linkedin.com/)
* [Wellfound](https://wellfound.com/role/r/machine-learning-engineer)
* Hacker News "Who's Hiring" Thread [Sample Post](https://news.ycombinator.com/item?id=33818037) and [Collection of all posts](https://hnhiring.com/)
* [Turing](https://www.turing.com/)

## Salary Comparison Tools
* [Levels.fyi](https://www.levels.fyi)

## Useful Job Boards that sometimes suck
* [Indeed](https://www.indeed.com/)
* [Toptal](https://www.toptal.com/)
* [RemoteOK](https://remoteok.io/)
* [StackOverflow Jobs](https://stackoverflow.com/jobs/)

## Gigs (Freelance work)
* [TopCoder](https://www.topcoder.com/)
* [Experfy](https://www.experfy.com/)
* [Upwork](https://www.upwork.com/)
* [Codementor](https://www.codementor.io/)

## On-Demand Help
* [Patreon](https://www.patreon.com/bradflaugher)
* [Wyzant](https://www.wyzant.com/)

## Competitions
* [Kaggle](https://www.kaggle.com/competitions)
* [ML Safety Competitions](https://safe.ai/competitions)
