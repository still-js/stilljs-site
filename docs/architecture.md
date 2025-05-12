# Still.js Architecture and Folder Structure


## SCV Architecture
Still.js follow it's own architecture approach named <b>Service, Controller and View</b>, as it is quite peculiar on the way it handles and process the components since it does not have bundle/building process, follow the representation diagram:

![SVC Arcchitecture](assets/img/svc-architecture.png)

<br>

### Service <a href="../components-communication/#3-global-state-management-reactively-components-communication-with-service" style="font-size:13px;">see example</a>
Serves/Provide data to the <b>View</b>, it also takes care of transactions like HTTP requests as well has Global state management. 

Services are injected (via <b>`@Inject`</b> annotation) into the component(s) that needs to use it, for this reason they are singleton and are managed by the application container.



### Controller
Serves the View with behavior and DOM logic. Especially when it comes to complex applications, this is the right place to make large and shared behavior thereby offloading the View.

Controllers can be either injected (as singletons) or directly used within components or other controllers. While injection uses a singleton pattern, it's also possible to create new instances manually.


### View (UI Component)
A component itself, hence it implements all the visual aspects of the Application, and to some extent some very specific/localized behavior skipping the controller. 

In small application the View can concentrae everything, from Visual things, to Transactions and Data (like Service), to behavior and DOM manipulation (like Controller).


<br>
<br>



## Project Folder Structure

When created a Still.js projects, it generates the necessary folder structure and files needed for building the application according to it.

=== ":octicons-project-roadmap-16: Still.js project folder structure"
	```js title="Still.js project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |    |__ app-template.js
    |    |
    |__  index.html
    |__  ...

	```

The presente folder and files represents the core of the Framework itself, which are needed for building the App:

- ***@still/*** Folder with the Framework files to handle all the available features
- ***app/*** Folder with the Framework files to handle all the available features. Normally the dev will organize the app in different sub-folders according to what layers and files type it'll have, an example would be as follow:

<ul style="padding-left: 30px; color: grey;" type="square">
    <li><b>components</b> - to hold UI components oranized in sub-folders</li>
    <li><b>services</b> - to hold services for the components</li>
    <li><b>controllers</b> - to hold controllers for the components</li>
    <li><b>assets</b> - to hold differents assets (e.g. images) organized in sub-folders</li>
    <li><b>libs</b> - to hold external libraries (e.g. jquery)</li>
</ul>

- ***config/app-setup.js*** File for setting generic application and context configuration
- ***config/route.map.js*** File managed by the framework to handle navigation and routes
- ***config/app-template.js*** File for setting up the application skeleton if needed

<br>