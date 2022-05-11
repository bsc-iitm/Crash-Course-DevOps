# Week 1: Github-1
In this week's module, we'll be taking a glance over GitHub basics and how to clone, pull and push repositories using github, and manage conflicts. 

## Day 1 (W1-D1) : Git Fork, Clone and Pull request
<details>
<summary>Click to expand/collapse</summary>

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

</details>

## Day 2 (W1-D2) : VSCode, Git Extension, Git conflict resolution
  
<details open>
  <summary> Click to expand/collapse </summary>  

### VScode setup (W1-D2-01)
VSCode is a recommended Text Editor to use with your workspace. It also comes with various useful extension, which makes development process easier.
You can follow the tutorial in the below link to setup your VSCode in your workspace. 

[Setup VSCode & Python virtualenv workspace](https://discourse.onlinedegree.iitm.ac.in/t/setting-up-python-virtualenv-and-a-workspace-along-with-helpful-notes-on-setting-up-vscode-text-editor/)

It is then recommended to install **GitLens** extension to VSCode. Git integration comes by default with VSCode and should work out of the box. 

### Open your workspace in VSCode (W1-D2-02)
Once VSCode is setup, follow any of the below steps to open up your workspace in VSCode

#### WSL / Linux environment
```sh
cd /path/to/Crash-Course-DevOps
code .
```

#### Windows / using the GUI
- Open up VSCode
- Click on `Open Folder`, and select the `Crash-Course-DevOps` folder to add it to your workspace.
![image](https://user-images.githubusercontent.com/10195318/167861685-5e453ca1-6445-4278-8103-46b87c0fd9a4.png)

### Creating conflicts in git repository (W1-D2-03)
1. Go to your forked repository, eg: https://github.com/username/Crash-Course-DevOps
2. Go to `Week 1` folder, and click on your working file you created in Week1-Day1. 
3. Click on the edit button (refer below)
![image](https://user-images.githubusercontent.com/10195318/167862307-d653d515-4ca2-474a-b79b-436e100ef02a.png)
4. Add extra 5 lines of text to your file (`username.work`), (see example below)
![image](https://user-images.githubusercontent.com/10195318/167862965-4bc39759-7995-4629-a5b0-71e1e9892c71.png)
5. Scroll down to commit your changes
![image](https://user-images.githubusercontent.com/10195318/167863102-6a2b251d-fd81-4fc0-9fac-d9c3604cb7d2.png)
6. Now **close the online git repository, and open your local folder in VSCode**
```sh
cd /path/to/Crash-Course-DevOps
code .
```
7. Open the same file, (`Week 1/username.work`) in VSCode
  
![image](https://user-images.githubusercontent.com/10195318/167863429-42c8119f-81dc-41ce-9b5d-e9ad38b471c7.png)
  
8. Now edit the same file in your VSCode, add extra 5 lines of code to your file (see example below)
  
![image](https://user-images.githubusercontent.com/10195318/167863859-e29e2004-1186-4f40-8dfe-357848c1ecac.png)
  
9. Now let's use VSCode's built in source control to try stage and commit the changes (refer images below)
  
![image](https://user-images.githubusercontent.com/10195318/167864028-b230e4f0-1c02-4cfd-bada-cc63000a8722.png)
  
10. Click on the `+` button to add/stage your files to commit. Clicking `+` is same as running the command `git add .`
  
![image](https://user-images.githubusercontent.com/10195318/167864251-84f5cd01-df66-4846-a1d0-8a1dc2105d92.png)
  
11. Now your file should appear under the **Staged** section,
  
![image](https://user-images.githubusercontent.com/10195318/167864413-bca0e60b-da29-4d34-a2cb-4f5f699de613.png)
  
12. Give your commit a comment, and click on Tick button to commit. This process is same as running the command `git commit -m "Week 1 - Day 2 Conflicts"`
  
![image](https://user-images.githubusercontent.com/10195318/167864549-0ed0f879-8fce-4408-a489-bdfea8d6c6f2.png)
  
13. Once the changes are staged and commited, it's time to push it to online Github repo, click on the `Sync Changes` button
  
![image](https://user-images.githubusercontent.com/10195318/167864908-9ab5a457-b656-4050-929f-b519ff674be1.png)
![image](https://user-images.githubusercontent.com/10195318/167864889-ba0c425c-47d7-4e0d-9a15-8413beed4ec0.png)
  
14. As the online repo has a change which has not been synced/refected in your local repo, and now the same file is being updated from local pc, you are presented with a message stating the file has conflicts which needs to be resolved
  
![image](https://user-images.githubusercontent.com/10195318/167865417-2eff62ac-cd62-45c2-b140-cdd34a1c2e19.png)
  
15. You can either choose to keep the update your did in your online git repo, or the local one, or also keep both.
  
![image](https://user-images.githubusercontent.com/10195318/167865565-39e651af-1307-4b0f-9409-a5cb893c1191.png)
  
16. Let's say for this example we want to keep both, your output should look similar to the pic below
  
![image](https://user-images.githubusercontent.com/10195318/167865677-165f71e2-4ceb-4dd3-9399-fb1f78dfda7b.png)
  
17. Save the file, and stage the changes
  
![image](https://user-images.githubusercontent.com/10195318/167865795-ef5892d6-8627-4eb9-b773-36a1029626bc.png)
  
18. Commit your changes after resolving the conflicts
  
![image](https://user-images.githubusercontent.com/10195318/167865907-ed174bdb-da95-40ec-a95b-ba0c7e5f4884.png)
  
19. Sync your changes, and now your updates will be pushed successfuly to your online repo, you can verify the same by visiting the file in your github repo. 
  
20. Create a **PR** `Refer Pull Request (W1-D1-03) exercise, in Week 1` for this new update.

</details>


