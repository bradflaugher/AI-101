# bootcamp

Notes and resources for [Brad Flaugher's Data-Focused Programming Bootcamp](https://bradflaugher.com/bootcamp.html)


# New Student TODOs

## Preparation

* (Preferred, but not required) Install Ubuntu Linux on your PC, if you have one [Dual Boot Guide](https://help.ubuntu.com/community/WindowsDualBoot) or if you want to wipe your entire machine or are using an old laptop use the [Fresh Install Guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview) NOTE if you have a Mac this will be almost impossible, but that's OK, just install docker (see below)
* (Required) Install Docker Desktop [Docker.com](https://www.docker.com/get-started/)
* (Required) Read [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* (Required) Read Chapters 1-6 of [Automate The Boring Stuff with Python](https://automatetheboringstuff.com/)
* (Recommended) Learn vim [via a fun game](https://vim-adventures.com/), [via exercises](https://vim.is/), [by reading documentation](https://www.vim.org/docs.php)

## Access

* get access to course moodle at [moodle.bradflaugher.com](https://moodle.bradflaugher.com)
* get ssh access to ML training rig ```ssh myname@sekret.bradflaugher.com```

# Lecture Outline

* Note 1: Lectures are a small part of the course, most bootcamper's time will be spent working on their final potrfolio projects.
* Note 2: The 6 week course is broken into numeric and alphabetical lectures. Lectures 1-6 are technical in nature, Lectures A-E are soft-skills and history.

## Lesson 1: Practical Science

### Topics
* ML vs AI, supervised, unsuperviesd, GANs and Reinforcement
* Intro to Neural Networks, Neuroscience, and Statistics
* Babies and Vision
* Single Cell Neural Network ala Excel Neural Networks
* Regression to Support Vector to Neural Network
* Jon Krohn's Hamburger/Hot Dog Classifier
* Baking a cake with positive reinforcement

### Readings (Online)
* [Understanding Infant Vision](https://www.aoa.org/healthy-eyes/eye-health-for-life/infant-vision?sso=y)
* [Intro to Deep Learning](https://www.youtube.com/watch?v=qj5gUDJ5TnU)

### Additional Readings on Modeling topics not covered in this course
* [Support Vector Machines in 2 minutes](https://www.youtube.com/watch?v=_YPScrckx28)
* [Random Forest](https://towardsdatascience.com/random-forest-classification-678e551462f5)
* [Old College Textbook on AI](https://www.goodreads.com/book/show/475758.Artificial_Intelligence)

## Lesson A: History, Impostor Syndrome and Working With Technical Professionals

### Topics
* Working in Tech: Stereotypes in Tech
* Working in Tech: Phil Jackson's Team Composition
* History: A historical perspective on technological adoption
* History: Languages, Python and C in particular. SPEED TEST!
* History: BERT, GPT3 and self-driving cars.
* History: Intro to Bias: Mugshot.com, Reggie Bush's W.A.G. Model

### Readings (Online)
* [Huge “foundation models” are turbo-charging AI progress](https://www.economist.com/interactive/briefing/2022/06/11/huge-foundation-models-are-turbo-charging-ai-progress)
* [Language Models: Past, Present, and Future](https://cacm.acm.org/magazines/2022/7/262080-language-models/fulltext)
* [The Impact of Computers on Manufacturing Productivity Growth: A Multiple-Indicators, Multiple-Causes Approach](https://www.jstor.org/stable/2951433)

### Readings (Books, Videos, Handouts)
* MIT Lectures on Managing Technical Professionals (Handout, Moodle)
* [Phil Jackson Oprah Interview, Zen Mind Beginners Mind](https://youtu.be/vKAEH_L-v98?t=98)

## Lesson 2: Docker and Environment Setup

### Topics
* What is docker?
* What does "ephemeral" mean?
* Command line usage, flags, interactive mode and bash
* SQL, what it is and why it's important (PowerBI, Tableau, Athena, BigQuery)

### Readings
* [Docker Documentaton](https://docs.docker.com/)
* [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* [Interactive SQL course @ Codecademy](https://www.codecademy.com/learn/learn-sql)

## Lesson B: Open Source, Freedom, and Stress

### Topics
* Why Linux? Why Open Source, FOSS?
* Cycling team analogy, Trek, Schwinn, Homemade Bike
* “A Generation Behind” - is it true? is it useful?
* Competition and cooperation in tech.
* Anxiety and process

### Readings
* [Free Software, Free Society](https://www.gnu.org/philosophy/fsfs/rms-essays.pdf)
* [Notes on The Software Paradox](https://baus.net/the-software-paradox/) or [The Software Paradox (Full Book)](https://www.amazon.com/Software-Paradox-Rise-Commercial-Market/dp/1491900938)

## Lesson 3: Loading Data Types, More Statistics

### Topics
* Numbers are Data
* Text is Data
* Images are Data
* Statistics for Machine Learning
* Data Collection, ETL and "glue code"

### Readings (Online)
* [Preprocessing Notebook](/3_Data_Types/data_loading_preprocessing.ipynb)
* [6 Step ETL with Airflow](https://tegardp.medium.com/the-6-step-etl-process-using-airflow-with-example-and-exercise-db46715a61f0)
* [Tensorflow Image Classification Example](https://www.tensorflow.org/tutorials/images/classification)

### Readings (Handout)
* Diving Judges Case Study UPenn (Handout, Moodle)

### Optional Readings
* [Fundamentals of Data Engineering, Chapters 1 and 3](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)

## Lesson C: Managing Technical Professionals, Managing Complex Technical Projects

### Topics
* Working with "Simon"
* Modules and Team Interaction
* Testing and Documentation
* Blending Models and Humans

### Readings (Handout, Moodle)
* MIT MTP Notes
* Wharton Model Notes

## Lesson 4: Wrangling Your Data

### Topics
* AI/ML as "Programming with data"
* Common data gathering tricks
* Open-source datasets
* "What to do when you get stuck with a horrible dataset"	

### Readings (Online)
* [How Deep Learning Works](https://www.youtube.com/watch?v=wBgW3ZtlPT8)

### Additional Resources (Optional)
* [Stanford Lectures](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
* [FreeCodeCamp](https://www.youtube.com/watch?v=NWONeJKn6kc)

## Lesson D: Practical Debugging, Hacker Ethos and Mindset

### Topics
* UNIX as IDE
* Infrastructrue as code
* Platform agnosticism
* Which Libraries should I use?
* The problem with GUIs

## Lesson 5: Model Architecture

### Topics
* Layer Types
* "Standard Models"
* Where to start, how to adjust hyperparameters
* "Stealing" ideas

### Readings
* [Modeling Natural Language](https://www.youtube.com/watch?v=rqyw06k91pA)

## Lesson E: AI Optimism and Bias

### Topics
* When will Skynet become self-aware?
* Self-Driving trolley preblems
* I can predict criminality, should I? 
* Are biased models useful? When?

### Readings
* [Google Researcher Says She Was Fired Over Paper Highlighting Bias in A.I.](https://www.nytimes.com/2020/12/03/technology/google-researcher-timnit-gebru.html)
* [Tesla’s ‘phantom braking’ problem is getting worse, and the US government has questions](https://www.theverge.com/2022/6/3/23153241/tesla-phantom-braking-nhtsa-complaints-investigation)
* [A.I. Is Not Sentient. Why Do People Say It Is?](https://www.nytimes.com/2022/08/05/technology/ai-sentient-google.html)

## Lesson 6: Model Deployment

### Topics
* Tensorflow Lite, Tensorflow Serving
* Predict is easy, train is hard (computationally)
* Docker + Flask

### Readings
* [Tensorflow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker)


# Final Projects

Bootcampers will spend a tremendous time working on final projects that are targeted to the bootcamper's career goals. For an example final presentation see [Oleh's Video (YouTube)](https://www.youtube.com/watch?v=I-KL-mWF548) and [Oleh's Repository (GitHub)](https://github.com/MorhaliukOL/ML_Project).

# Further Reading

I highly recommend the following books and resources.

* [Basic Linux Terminal Tips and Tricks](https://learning.oreilly.com/library/view/basic-linux-terminal/9781484260357/) and [Bash for beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* [Git Basics](https://rogerdudler.github.io/git-guide/)
* [Practical SQL](https://learning.oreilly.com/library/view/practical-sql-2nd/9781098129866/)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Deep Learning Illustrated](https://www.amazon.com/Deep-Learning-Illustrated-Intelligence-Addison-Wesley/dp/0135116694) and [Deep Learning with Tensorflow, Pytorch etc..](https://learning.oreilly.com/videos/deep-learning-with/9780136617617/)
* [Fundamentals of Data Engineering](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)

