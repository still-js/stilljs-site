

###  Creating a Still.js Project
<hr/>



#### 1. Installation

```
npm install @stilljs/cli -g
```

In pricinple, still.js application development process is tied to the NPM, therefore, for it to be available in our machine we need to make a global (-g) installation.

Once installed, still-cli can be invoked from the terminal by typing `npx still` to see the available commands and ooptions.

<br>

#### 2. Creating a project
Create a folder for you project (e.g. project-name) and from inside such folder init the project as the bellow instruction
```
npx still init
```

After initiating the project the framework structure and files are download to the folder.


<br>

#### 3. Acessing the project (Project structure)

```js
    project-name/ //My project folder
    |__ @still/ // Still.js framework
    |__ app/ // Folder which holdes to app files
    |     |__ HomeComponent.js //Component generated automatically when creating project
    |__ config/ //Folder which holds application configuration files
    |     |__ app-setup.js //App configuration file/class
    |     |__ app-template.js //App template scheleton
    |     |__ route.map.json //Component routing and path file
    |__ index.html //Application container
    |__ jsconfig.js //Basic configuration for vscode
    |__ package.json // Regular package JSON

```

In the above picture we have the project structure open in the code editor, everything concerning the project will be created inside the <a><b>app</b></a> folder. Inicially the <a><b>app</b></a> folder comes with one component which path is <a><b>app/home/HomeComponent.js</b></a> as also depicted in the picture.


<br>

#### 4. Running the project

`npx still app serve`

The above command needs to bu run in the terminal from the project folder as dipicted bellow:

![Project Structure](assets/img/running-project-doc.png)

<br/>
After typing for serving the project it gets oppened automatically in the browser as in the bellow picture:

![Project Structure](assets/img/project-open-in-browser-doc.png)

<h2>You're all set! enjoy your coding.</h2>
<br/>