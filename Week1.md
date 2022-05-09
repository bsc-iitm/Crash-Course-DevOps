# Week 1: Github-1
In this week's module, we'll be taking a glance over GitHub basics and how to clone, pull and push repositories using github, and manage conflicts. 

## Day 1 (W1-D1) : Git Fork, Clone and Pull request

### Fork (W1-D1-01)
1. Go to the repo's main page [Crash Course: DevOps](https://github.com/bsc-iitm/Crash-Course-DevOps), click on **Fork** button to fork the repo to your repository.
![image](https://user-images.githubusercontent.com/10195318/167304903-c6c13f50-ea71-4ac3-b784-0ebd8b07f978.png)

### Clone (W1-D1-02)
1. Go to the **forked repo's main page** (example https://github.com/username/Crash-Course-DevOps) and find the clone option in the Code section (Ref Pic below)
![image](https://user-images.githubusercontent.com/10195318/167304270-f20d08c2-0c1a-405a-a979-2e1cd1f1aaf7.png)

2. After you copy the git url, open your terminal, go to your workspace directory, and clone the git using the command `git clone <git url>`. See example below
```sh
cd /path/to/your/workspace
git clone https://github.com/username/Crash-Course-DevOps.git
```
![image](https://user-images.githubusercontent.com/10195318/167304858-67b0e99e-cc7a-4d0c-83c0-9b7425181c49.png)

3. Switch to this cloned directory using `cd Crash-Course-DevOps`

### Updates (W1-D1-03)
1. After cloning your forked repo to your local pc, go to `Week 1` directory (`cd "Week 1"`)
2. Create a new file in this folder, namely `<your github username>.work` and put some content in it.
3. After making some updates, track changes using the command `git status`
4. Add all the changes using the command `git add .`
5. Once you add in/stage all your changes, you have to commit them. You can use the following command to commit the changes, `git commit -m "My first commit"`
6. After commiting, push the changes to the github repository using the command, `git push origin`

Your command flow should look similar to the following

```sh
cd "Week 1"
echo "My first git update" >  my-git-username.work
git status
git add .
git commit -m "My first commit"
git push origin
```

### Pull Request (PR) (W1-D1-03)
1. After making changes to your online repository, we want it to be reflected in the main reposity under IITM. For this we have to initiate a Pull Request (PR) and ask the owners to merge your change in the current repository.
2. Find the PR button in your repository
![image](https://user-images.githubusercontent.com/10195318/167305190-87e08db7-87ce-4b29-b2b2-96a42b9ab811.png)

3. Once you verify the changes, click on Create PR button
![image](https://user-images.githubusercontent.com/10195318/167305224-0f96b09f-ab37-4b31-a953-7e4b29fa7576.png)

4. Now your PR is ready, and is waiting to be reviewed by the repo maintainers and to be merged. 
