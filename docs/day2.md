[Previous](day1.md) | [Index](index.md) | [Next](day3.md)

---

## Day 2

### Task 1 Create a new site

To develop web-apps with Frappe, we need to initialise `bench` by telling which branch (version) of Frappe we wish to use and telling a name of new directory (folder). At present, latest version of Frappe is 14, which is maintaine din branch `vesion-14`, so we will specify this branch for `--frape-branch` and use `frappe-bench` as the name of new folder, in which bench will fetch code of `frappe` and do initialisation.


```bash
bench init --frappe-branch version-14 frappe-bench
cd frappe-bench/
chmod -R o+rx /home/hsrai
bench new-site hs.rai
bench --site hs.rai add-to-hosts
bench use hs.rai
bench start
```

First command is:

`bench init --frappe-branch <branch_name> <directory_name_to_be_created>`

With 2nd command `cd` which stands for `change directory` we moved from current directory to newly created directory, named `frappe-bench` where frappe is initialised.

In next command `chmod`, stands for `change mode`, we modified the permission for `HOME` folder of user `hsrai` which is current user, and home is `/home/hsrai`, so that others can read and execute files of user `hsrai`.

Next command creates a new site with name `hs.rai`.

It will ask password of `root` user of database. In the process of creating website, you will be prompted to set password of the user `administrator`. Remember this password, which you need to login to the website. 

Then we will issue command `bench start`, which start a number of services, including web server. Once that is done we can assess our web-site in browser. We can read message, where it says:

`16:57:54 web.1            |  * Running on http://127.0.0.1:8000`

This tell us that we can assess out site from:

`http://127.0.0.1:8000`

or

`http://localhost:8000`

//# In new terminal #//

```bash
bench new-app library_management
bench --site library.test install-app library_management

```


---

[Previous](day1.md) | [Index](index.md) | [Next](day3.md)
