# Docker
## How to make development environments safe and portable, and feel amazing about yourself too!

---

# History
* Virtual environments are nice
* [FreeBSD-style jails are cool too](https://en.wikipedia.org/wiki/FreeBSD_jail)
* VirtualBox VMs ore cool, but hard to document

---

# Goals
* Don't give your computer cancer by installing crazy shit locally
* Don't mess up your other projects dependencies by installing crazy shit locally
* Document everything
* Allow anyone to recreate your precise environments
* "Future proofing" to enable complex deployments (Lambda, ECS, beanstalk, ec2, kubernetes etc...)

---

# Feelings
* Smart (installing things via an installer makes me feel dumb, think Xcode)
* Safe (environments are sandboxed)
* Productive (my code is also documentation, right Les?)
* Independent (don't need plugins and IDEs)
* 31337 H4X0R (I'm in a command line all day)

---

# Aside: Win/Mac/Linux are now all the same
* WSL allows for low-level interaction with windows
* Mac = Unix and plays nice
* (x86/64) Linux is best for this, but generally not necessary

---

# Who uses this?
* [Tensorflow standard install](https://www.tensorflow.org/install/)
* [Python official images](https://hub.docker.com/_/python/)
* Many linux distros
* Redis, many databases etc...
* Why isn't there a flask image?

---

# Brad's usage
* Always Start with docker
* Sharing directories 
``` 
-v $(pwd):/tf
```
* Getting to a bash prompt 
```
 -it {image_name} bash 
```
* I always think of it as if I'm sshing into a new box... feels nice

---

# Let's play with haskell

```
sudo docker pull haskell:8.10
sudo docker run -it haskell:latest bash
ghci
f x = x + x
```


--------

# The ML Starter project
* [here](https://github.com/Inoxoft/ml-template-repo/)

--------

# Developing your dockerfile
* Start simple
* Get better at bash
* Hack away!
* Experiment with versions, almost instantly

--------

# Next level
* Hook containers together with compose
* Deploy with EC2, beanstalk, ECS, lambda, k8s
* Edit someone's huge dockerfile

---

# END
