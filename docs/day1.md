[Previous](index.md) | [Index](index.md) | [Next](day2.md)

---

## Day 1

Participants were provided Linux ([Ubuntu 22.04 LTS](https://youtu.be/REdxblQpsDE)) loaded desktops, on which [Bench version 5.14.3](https://github.com/frappe/bench) was pre-installed.

Bench is a Command Line Interface (CLI) tool to manage Frappe Deployments. It provides an easy interface to help you setup and manage multiple sites and apps based on Frappe Framework.

### Take 1: Create your user name

Participants were given a sudo user (cc3), and were asked to create a user for themselves. Choose your username (only having alphanumeric, with no space or special characters) by following steps given below, for username taken as `hsrai`:

```bash
cc3@HoDCE:~$ sudo adduser hsrai
[sudo] password for cc3: 
Adding user `hsrai' ...
Adding new group `hsrai' (1004) ...
Adding new user `hsrai' (1004) with group `hsrai' ...
Creating home directory `/home/hsrai' ...
Copying files from `/etc/skel' ...
New password: 
Retype new password: 
passwd: password updated successfully
Changing the user information for hsrai
Enter the new value, or press ENTER for the default
	Full Name []: Hardeep Singh Rai
	Room Number []: HoD Civil
	Work Phone []: 123
	Home Phone []: 
	Other []: 
Is the information correct? [Y/n] Y
cc3@HoDCE:~$ 
```

Logout from user `cc3` and login as `hsrai` (replace `hsrai` with your username, you created just now).

### Task 2: GitHub.Com account

1. To create account at github.com visit [https://github.com](https://github.com/) and click on the button named [Sign up].
1. Enter you email, then enter your proposed password, then click on [Continue].
1. Try a `username`, which is not taken by anyone else, before, and click [Continue].
1. Type "y" for yes or "n" for no for next question, which is: Would you like to receive product updates and announcements via email?, click [Continue].
1. Prove you are human being by solving a puzzle, if presented.
1. Click on [Create account] to create your account.
1. Verify you email, by entering code sent your entered email ID.
1. Skip presonilastion at the bottom, or tell how you wise use, by telling your team size, Click on teacher or student,as applicable, and click on [Continue], select fetures, select [Continue for free] or opt for a few benefits as applicable to you. 
1. Then you will be presented with your dashboard.

### Task 3: Create git repository
- Now you have to visit github.com visit [https://github.com](https://github.com/) and login with you username and password after that navigate to righmost corner on your avtar and you will see + symbol just left to your avtar click on it and you will see the dropdown where you will find `New repository`.

![Repository Create](/img/repo-create.png)

- After navigating to the new repo Type a short, memorable name for your repository. For example, "hello-world`.

![Repository Create](/img/create-repository-name.png)

- Now Optionally, add a description of your repository. For example, `My first repository on GitHub.`

![Repository Create](/img/create-repository-desc.png)

- Choose a repository visibility. For more information, see "About repositories."

![Repository Create](/img/create-repository-public-private.png)

- Select Initialize this repository with a README.

![Repository Create](/img/initialize-with-readme.png) 

- Click Create repository and you have sucessfully done with a creation of git repository.

![Repository Create](/img/create-repository-button.png)


### Task 4: Create GitHub page

- Now navigate to your repository name helllo-world/or any name you have entered you will find your repository by following below image.

![Repository Create](/img/repo-view.png)

- Now  click on your repository and navigate `Add file` and click on `Create New File`.

![Repository Create](/img/add-file.png)

- Now you will find a diloge box where you have to write your file and folder name, now write `docs/` this will create a folder name docs and now write file name as `hobby.md` this will create a file name `index.md` under docs folder.

![Repository Create](/img/file-name.png)

- Now you can write mardown here for mardown syntax you can refere following link:
![Markdown Syntax](https://www.markdownguide.org/basic-syntax/)

![Repository Create](/img/mardown-content.png)

- Commit changes as explained below.

![Repository Create](/img/commit-meessage.png)

- Navigate to `setting` and then find `pages` and click on it.

- Now change two fied under Branch set these field to `main` and `/docs` respectively and click on save button near two these option.

![Repository Create](/img/branch.png)

- After some time navigate to setting --> Pages --> and on top you will see Your site url.

### Task 5: Get repository on your computer

### Task 6: Edit web page, update on github


---

[Previous](index.md) | [Index](index.md) | [Next](day2.md)
