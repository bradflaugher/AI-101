# bootcamp

Notes and resources for [Brad Flaugher's Data-Focused Programming Bootcamp](https://bradflaugher.com/bootcamp.html)


# New Student TODOs

## Preparation

* (Preferred, but not required) Install Ubuntu Linux on your PC, if you have one [Install Guide](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview), and [additional notes for dual-booting with Windows](https://linuxconfig.org/how-to-install-ubuntu-20-04-alongside-windows-10-dual-boot) NOTE if you have a Mac this will be almost impossible, but that's OK, just install docker (see below)
* (Required) Install Docker Desktop [Docker.com](https://www.docker.com/get-started/)
* (Required) Read [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* (Required) Read Chapters 1-6 of [Automate The Boring Stuff with Python](https://automatetheboringstuff.com/)
* (Recommended) Learn vim [via a fun game](https://vim-adventures.com/), [via exercises](https://vim.is/), [by reading documentation](https://www.vim.org/docs.php)
* (Recommended) Join the bootcampers [LinkedIn Group](https://www.linkedin.com/groups/12707793/)

# Lecture Outline

* Note 1: Lectures are a small part of the course, most bootcamper's time will be spent working on their final potrfolio projects.
* Note 2: The 6 week course is broken into numeric and alphabetical lectures. Lectures 1-6 are technical in nature, Lectures A-E are soft-skills and history.

## Lesson 1: Practical Science

### Topics
* Definitions: Data Scientist, Data Engineer, Data Analyst
* Definitions: Machine Learning and Artificial Intelligence
* History: What kind of ML is used today? [How much of this book is practically useless?](https://github.com/sukantatiger/Artificial_Intelligence/blob/master/Artificial_Intelligence_by_Rich_and_Knight.pdf) 
* Neural Networks: [Babies and Vision](https://www.aoa.org/healthy-eyes/eye-health-for-life/infant-vision?sso=y)
* Neural Networks: Single Cell Neural Network aka Regression in Excel
* Neucal Networks: [Name and Height "Regression"](https://beta.openai.com/playground/p/z9Jkesb3QnQhym1jxHiw9o3X)
* Neural Networks: When will GPT-3 "insights" become stale? Is this learning? is this engineering? is this science?
* Neural Networks: [Correllating words and images](https://www.craiyon.com/)
* Final Project Intro: [Huggable Model](https://github.com/daspartho/is-it-huggable)

### Introduction to Portfolio projects
* [VIDEO: Oleh's Car Price Predictor](https://www.youtube.com/watch?v=I-KL-mWF548) and [Source Code](https://github.com/MorhaliukOL/ML_Project)
* [VIDEO: Fall 2022 Bootcampers Presentation WARNING LARGE FILE](https://stack.bradflaugher.com/Videos/Final_Presentations_Audigent_Bootcamp.webm) and [Hanna's Source Code](/5_Model_Architecture/Profitable_Visitor_Classification_With_Notes.ipynb)

### Project Ideas
* [ML Safety Competitions](https://safe.ai/competitions)
* [Medusa](https://github.com/predbrad/medusa)
* [Kaggle](https://www.kaggle.com/competitions)

### Readings (Online)
* [Understanding Infant Vision](https://www.aoa.org/healthy-eyes/eye-health-for-life/infant-vision?sso=y)
* [Intro to Deep Learning](https://www.youtube.com/watch?v=qj5gUDJ5TnU)

## Lesson A: History, Impostor Syndrome and Working With Technical Professionals

### Topics
* Impostors: Talk about ME Professors teaching AI, and ML Leads at big companies
* What does MIT Say? A review of "Managing Technical Professionals".
* History: A historical perspective on technological adoption, is it fast or slow?
* "Lateral Thinking With Withered Technology"
* History: Languages, Python and C in particular. SPEED TEST!
* History: BERT, GPT3, DALLE, Stable Diffusion and self-driving cars.


### Readings (Online)
* [9 Reasons why you'll never be a data scientist](https://towardsdatascience.com/9-reasons-why-youll-never-become-a-data-scientist-c8c5b75503cf)
* [Huge “foundation models” are turbo-charging AI progress](https://www.economist.com/interactive/briefing/2022/06/11/huge-foundation-models-are-turbo-charging-ai-progress)
* [Language Models: Past, Present, and Future](https://cacm.acm.org/magazines/2022/7/262080-language-models/fulltext)
* [Have Computers Made Us More Productive?](https://www.stlouisfed.org/publications/regional-economist/october-1998/have-computers-made-us-more-productive-a-puzzle)
* [Lateral Thinking With Withered Technology](https://www.forbes.com/sites/tomokoyokoi/2021/01/24/how-the-philosophy-of-nintendos-game-boy-inventor-is-ripe-for-these-times/?sh=4d2983d04de4)

### Optional Readings
* [History of C](https://en.wikipedia.org/wiki/C_(programming_language))
* [History of Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [History of SQL](https://en.wikipedia.org/wiki/SQL)
* [Keynes on Next-Day Delivery](https://nn.m.wikiquote.org/wiki/The_inhabitant_of_London_could_order_by_telephone,_sipping_his_morning_tea_in_bed,_the_various_products_of_the_whole_earth)


### Readings (Books, Videos, Handouts)
* MIT Lectures on Managing Technical Professionals (Handout)

## Lesson 2: Docker, DevOps/MLOps, and Environment Setup

### Topics
* What is docker?
* What does "ephemeral" mean?
* Command line usage, flags, interactive mode and bash
* SQL, what it is and why it's important (PowerBI, Tableau, Athena, BigQuery)
* How to think about the cloud, Big Providers (AWS, GCP, Azure) and Small (Linode, Oracle, etc...)
* What are Kaggle and Colab?
* "Head of Data" interview question, how fast can you spin up an environment?

### Readings
* [Docker Documentaton](https://docs.docker.com/)
* [Command Line for Beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* [Interactive SQL course @ Codecademy](https://www.codecademy.com/learn/learn-sql)
* [Cloud Computing Business Overview (Sep 2022)](https://www.economist.com/business/2022/08/29/the-cloud-computing-giants-are-vying-to-protect-fat-profits)

### Optional Readings
* [Docker on AWS](https://aws.amazon.com/getting-started/hands-on/deploy-docker-containers/), or the [TLDR version](https://medium.com/geekculture/deploy-to-aws-docker-in-10-minutes-68a60724dcb9)
* [Docker on GCP](https://cloud.google.com/compute/docs/containers), or the [TLDR version](https://www.howtogeek.com/devops/how-to-run-docker-containers-on-google-cloud-platform/)
* [Docker on Azure](https://azure.microsoft.com/en-us/services/kubernetes-service/docker/)
* [Spotty](https://github.com/spotty-cloud/spotty)
* [Tensordock](https://www.tensordock.com/)

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
* [NLP in 5 Minutes with Tensorflow](https://codesearchonline.com/natural-language-processing-with-tensorflow-cheat-sheet/)
* [Tensorflow Image Classification Example](https://www.tensorflow.org/tutorials/images/classification)
* [Few-shot classification with SetFit...](https://rubrix.readthedocs.io/en/master/tutorials/few-shot-classification-with-setfit.html)

### Readings (Handout)
* UPenn Stats Lectures (Handout)

### Optional Readings
* [Fundamentals of Data Engineering, Chapters 1 and 3](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
* [6 Step ETL with Airflow](https://tegardp.medium.com/the-6-step-etl-process-using-airflow-with-example-and-exercise-db46715a61f0)
* [Airflow vs Luigi vs Kubeflow etc..](https://www.datarevenue.com/en-blog/airflow-vs-luigi-vs-argo-vs-mlflow-vs-kubeflow)

## Lesson C: Managing Technical Professionals, Managing Complex Technical Projects

### Topics
* Working with "Simon"
* Modules and Team Interaction
* Testing and Documentation
* Blending Models and Humans

### Readings (Handout)
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
* [MLFlow Intro](https://www.youtube.com/watch?app=desktop&v=daBTYQP23-A&feature=youtu.be)
* [Stanford ML Lectures, 2018](https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU)
* [FreeCodeCamp ML Course in 10 hrs](https://www.youtube.com/watch?v=NWONeJKn6kc)

## Lesson D: Practical Debugging, Hacker Ethos and Mindset

### Topics
* UNIX as IDE
* Infrastructrue as code
* Platform agnosticism
* Which Libraries should I use?
* The problem with GUIs

### Readings
[Unix is my IDE](https://blog.sanctum.geek.nz/series/unix-as-ide/)
[Unix is my IDE (discussion)](https://news.ycombinator.com/item?id=12653028)


## Lesson 5: Model Architecture

### Topics
* Layer Types
* "Standard Models"
* Where to start, how to adjust hyperparameters
* "Stealing" ideas
* Metrics: Accuracy, Precision, Recall, Loss, AUC etc...

### Readings
* [Modeling Natural Language](https://www.youtube.com/watch?v=rqyw06k91pA)

## Lesson E: AI Optimism and Bias

### Topics
* When will Skynet become self-aware?
* Self-Driving trolley preblems
* I can predict criminality, should I? 
* Are biased models useful? When?
* AI Ethics Big 3: Explainability, Bias, and Privacy (Story about skin cancel detector model and stock trading models)

### Readings
* [Google Researcher Says She Was Fired Over Paper Highlighting Bias in A.I.](https://www.nytimes.com/2020/12/03/technology/google-researcher-timnit-gebru.html)
* [Tesla’s ‘phantom braking’ problem is getting worse, and the US government has questions](https://www.theverge.com/2022/6/3/23153241/tesla-phantom-braking-nhtsa-complaints-investigation)
* [A.I. Is Not Sentient. Why Do People Say It Is?](https://www.nytimes.com/2022/08/05/technology/ai-sentient-google.html)
* [The Long Road to Driverless Trucks](https://www.nytimes.com/2022/09/28/business/driverless-trucks-highways.html)
* [Stuck on the Streets of San Francisco in a Driverless Car](https://www.nytimes.com/2022/09/28/technology/driverless-cars-san-francisco.html)
* [Is it all just a big regression?](https://www.reddit.com/r/MachineLearning/comments/xrge5d/d_is_neural_network_really_smart_or_just_some/)

### Optional Readings
* [The Alignment Problem](https://en.wikipedia.org/wiki/The_Alignment_Problem)

## Lesson 6: Model Deployment and MLOps

### Topics
* Tensorflow Lite, Tensorflow Serving
* Predict is easy, train is hard (computationally)
* Docker + Flask
* DevOps vs MLOps, what is special? what is the same?

### Readings
* [Tensorflow Serving with Docker](https://www.tensorflow.org/tfx/serving/docker)


### Optional Readings
* [Practical MLOps Chapters 1-4](https://learning.oreilly.com/library/view/practical-mlops/9781098103002/)
* [Create an MLOps Pipeline with github and docker in minutes](https://heartbeat.comet.ml/create-an-mlops-pipeline-with-github-and-docker-hub-in-minutes-4a1515b6a551)
* [AI Template (github)](https://github.com/facebookincubator/AITemplate)

# Final Projects

Bootcampers will spend a tremendous time working on final projects that are targeted to the bootcamper's career goals. For an example final presentation see [Oleh's Video (YouTube)](https://www.youtube.com/watch?v=I-KL-mWF548) and [Oleh's Repository (GitHub)](https://github.com/MorhaliukOL/ML_Project).

# Recommended Books and Articles

* [Basic Linux Terminal Tips and Tricks](https://learning.oreilly.com/library/view/basic-linux-terminal/9781484260357/) and [Bash for beginners](https://towardsdatascience.com/basics-of-bash-for-beginners-92e53a4c117a)
* [Git Basics](https://rogerdudler.github.io/git-guide/)
* [Practical SQL](https://learning.oreilly.com/library/view/practical-sql-2nd/9781098129866/)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [Deep Learning Illustrated](https://www.amazon.com/Deep-Learning-Illustrated-Intelligence-Addison-Wesley/dp/0135116694) and [Deep Learning with Tensorflow, Pytorch etc..](https://learning.oreilly.com/videos/deep-learning-with/9780136617617/)
* [Fundamentals of Data Engineering](https://learning.oreilly.com/library/view/fundamentals-of-data/9781098108298/)
* [Practical MLOps](https://learning.oreilly.com/library/view/practical-mlops/9781098103002/)

# Recommended Learning Resources and Professional Groups
* [Women in Data](https://www.womenindata.org/)
* [O'Reilly Learning](https://www.oreilly.com/)

# Recommended (in-person) Conferences
* [Ai4](https://ai4.io/)
* [Pytorch Dev Day](https://pytorch.org/events) or [Tensorflow Dev Summit (if it comes back)](https://www.tensorflow.org/dev-summit/)

