# LS 190, Assignment 4: "Small bot"

## Table of contents


* [Assignment](#Assignment)
* [Accepting the assignment](#Accepting-the-assignment)
* [Overview](#Overview)
  * [Evaluation](#Evaluation)
* [Wrap-up](#Wrap-up)

## Assignment

Today, I'm assigning you something that should serve as a kind of watermark in the class -- you're going to build something that incorporates various `JSON` files (at least two -- though you could use more) to create a bot that tweets various `random`ized statements. 

Here, you can go as complicated or simplistic as you'd like, but my only requirements:

* use `2` `JSON` files from the `_data` directory
  * this directory is in the `src` folder of this assignment
  * you may need to navigate it to figure out a bit of the structure
* incorporate some operations of `random`
* the program must tweet to our test bot account ([@chomp_bot](https://twitter.com/chomp_bot))
  * this code is provided for you, all you need to do is "wire it up"
* you must write about the concept you've chosen to implement in response to the questions in [the reflection file](writing/reflection.md).

## Accepting the assignment

---

- [ ] Click the link provided for the lab assignment and accept it in GitHub classroom
- [ ] Once the assignment finishes building, click the link to go to your personal repository assignment

## "Cloning" a repository

### Using the correct download link

- [ ] On this repository's page, click the `Clone or download` button in the upper right hand corner
* You may need to scroll up to see it
- [ ] In the upper right corner of the box that appears, click `Use SSH`
- [ ] Copy the link that appears in the textbox below the phrase "Use a password with a protected key."

#### Cloning

* [ ] Type `ls` in your terminal window
* You should be in your `~` directory
- [ ] Once there, "clone" the repository using the link copied above
* If I (the instructor) were to clone my own repository, I'd enter (your link will look different):

```
git clone git@github.com:allegheny-college-ls-190-fall-2021/ls-190-assignment-3a-small-bot
```

## Wrap-up

---

### Submitting the assignment/saving progress

The GitHub platform is a place to store your work. So, it makes some sense that should be able to _clone_ (download) from it, and push back (upload) to it. Here, we'll learn this second part.

- [ ] `cd` to your `~` folder
- [ ] Locate the `ls-190-assignment-3a-small-bot` folder and `cd` to it.

Once in this folder, we need to tell git that there have been changes.

- [ ] Type `git add .` and press `Enter`
* This tells git to look through the _entire_ folder structure for new changes and "stage" them

- [ ] Type `git commit -m "{Commit message}"` to "label" the commit
* This is typically something like `git commit -m "Fixing a typo"` -- the message in quotes should be as descriptive as possible, while still remaining somewhat short

- [ ] To send all changes to the server, type `git push`
- [ ] At the prompt, input the password associated with the `SSH Key` you created in the opening week of class

Once the process finishes successfully, we're done!

#### A strong warning

<div class="alert alert-block alert-danger">
    <p><strong>While we may use this server to store code, <u>you</u> are responsible for using GitHub as your main backup.</strong></p>
    <p>While I back this server up on a regular basis, I cannot guarantee that I'll have the ability to restore up-to-the-minute data for your work.</p>
    <p>Remember: to err is human; to back up your work is divine.</p>
</div>
