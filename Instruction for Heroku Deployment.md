# How to deploy the web app to Heroku

**Step 1.** For deploying the vms web app to heroku, you will need heroku cli.

   For Installing Heroku CLI refer to this [Heroku Installation Documentation](https://devcenter.heroku.com/articles/heroku-cli) for different installation methods.
   

**Step 2.** Create Procfile for Heroku Deployment
   
   You will need to create a Procfile which will provide the instruction for Heroku Deployment,make sure Procfile should be created inside the `vms` directory.
   
   Procfile should look like:
   
   ```
   web: gunicorn vms.wsgi --log-file -
   ```
   
**Step 3.** Edit the requirements.txt file
 
   Add `gunicorn` inside the requirements.txt below all packages.
   
**Step 4.** Create a .env file which is same as .env.example
  
**Step 5.** Run the following cmd's to deploy the web app to heroku.

  **Note:** Make sure you are inside `vms/vms` directory during deployment process

  ``` 
  $ git init
  $ heroku git:clone -a vms-r 
  $ git add .
  $ git commit -m "commits"
  $ git push heroku master
  $ heroku ps:scale web=1
  ```
  Check logs using `heroku logs --tail`
  
  **Note:** vms-r is the name of the web app created in the heroku for deployment.
  
  **Note:** Procfile and .env should be created inside main vms folder as metioned in Step 2 refer to below file structure.
  
  ```
  vms
  |___ Procfile
  |___ requirements.txt
  |___ .env
  |___ vms 
  |     |__ wsgi.py
  |     |__ manage.py
  |     |__ ...other files
  |
  |__ ...other files
  ```
  
  
  
  
  
   
   
