### Overview
Since Still.js is built with vanilla JavaScript, which doesn't support annotations, it uses JavaScript comments and JSDoc to enable annotation-like capabilities. Still.js defines its own specific annotation format for this purpose.

Still.js currently supports 5 annotations, 4 of which are top-level and must appear at the top. These annotations are used for specific scenarios, allowing components to have metadata available at runtime.

### Still Command Line Tool
!!! warning "Changes @Path from @Path"

    If you're using Still.js version <=0.0.17 the <b>`@Path`</b> annotation
    is named <b>`@Path`</b>.

<br/>

<br>
<table class="annotations">
    <tr>
        <td style="background: lightgrey;">Annotation</td>
        <td style="background: lightgrey;"><b>Required complement</b></td>
        <td style="background: lightgrey;"><b>Description</b></td>
        <td style="background: lightgrey;"><b>Use context</b></td>
    </tr>
    <tr>
        <td>@Prop<top-level>top-level</top-level></td>
        <td>N/A</td>
        <td>Annotates a component variables to specify that it'll be a property and not a state.</td>
        <td>
            <ul>
                <li>Component variable which does not need reactive behavior</li>
                <li>Component flags (e.g. assign true/false)</li>
                <li>Internal component business logic flow</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>@Proxy<top-level>top-level</top-level></td>
        <td>N/A</td>
        <td>Define a class property which serve as a link between Parent and a child component (embeded). JSDoc <b/>@type</b> can complement providing type hinting.</td>
        <td>
            <ul>
                <li>Provide parent with public child methods and property/states</li>
                <li>Parent-to-child communication</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>@Inject<top-level>top-level</top-level></td>
        <td>JSDoc <b>@type</b></td>
        <td>Define a class property which serve as a link between Parent and a child component (embeded)</td>
        <td>
            <ul>
                <li>Inject the defined type (@type) as dependency</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>@Controller<top-level>top-level</top-level></td>
        <td>JSDoc <b>@type</b></td>
        <td>Alternative to <b>@Inject</b> which in addition to injection adds the specified controller as the main controller of the component allowing it to be referenced as <b>controller.</b> in the template</td>
        <td>
            <ul>
                <li>Inject the defined type (@type) as dependency</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td>@Path</td>
        <td>N/A</td>
        <td>Complementary to the <b>@Inject</b> or <b>@Controller</b> annotation and recieves the path of the service being injected. If used it needs to come right after <b>@Inject</b> or <b>@Controller</b> annotation</td>
        <td>
            <ul>
                <li>Specify the folder path where the service/controller is located</li>
            </ul>
        </td>
    </tr>
</table>

<style>

    table.annotations tr td:first-child {
        width: 140px;
        font-weight: bold;
    }

    table.annotations tr:first-child {
        font-weight: bold !important;
    }

    table.annotations td {
        padding-left: 5px;
        padding-top: 5px;
        border: 1px solid rgb(193, 185, 185);
    }

    table.annotations tr:nth-child(even) {
        background:rgb(245, 239, 239);
    }

    table.annotations  { font-size:12px;, border: 1px solid; }

    top-level {
        border: 1px solid orange;
        background: yellow;
        text-align: center;
        border-radius:6px;
        margin-left: 5px;
        padding: 3px;
        font-size: 12px;
    }
</style>

<br>



<a name="example-setup"></a>
### Examples Setup

The examples in this documentation/tutorials will be base in the bellow <b>folder structure</b>, <b>Application Setup</b> (<b>`app-setup.js`</b>) and routes metadata (<b>`route.map.js`</b>)

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |   |
    |   |__ base-components/
    |   |   |__ HomeComponent.js
    |   |   |
    |   |__ person/
    |   |   |__ PersonForm.js
    |   |   |__ PersonList.js
    |   |   |
    |   |__ services/
    |   |   |__ MainService.js
    |   |   |__ user/
    |   |   |   |__ UserService.js
    |   |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"

    ```js linenums="1" title="This files stays in the project root folder" hl_lines="11"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { HomeComponent } from "./app/base-components/HomeComponent.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            // This is the service path setup
            this.setServicePath('services/')
            this.setHomeComponent(HomeComponent);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
    ```

=== "route.map.js"
	```js title="This is the where Application context aspects are setup. This file is in the root folder. " linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                HomeComponent: {
                    path: "app/base-components",
                    url: "/home"
                },
                PersonForm: {
                    path: "app/person",
                    url: "/person/register"
                },
                PersonList: {
                    path: "app/person",
                    url: "/person/register"
                }
            },
            lazyInitial: {}
        }
    }
	```


<a name="prop-annotation"></a>
<br>
### <b>@Prop</b> - Defining component property variable

This example takes into consideration the <b><a href="#example-setup">above</a></b> folder structure, app and routing setup.

By default, variables in a Still.js component are reactive state variables unless it's a special one like <b>`isPublic`</b>, <b>`template`</b>, <b>`$parent`</b>, etc. If reactivity isn't needed, it's recommended to use the <b>`@Prop`</b> annotation to define a non-reactive variable instead.
<br>


=== "HomeComponent.js"

    ```js title="This component is placed in the app/base-components/ folder" hl_lines="7-8 10 12-13 18-19 25 30" linenums="1"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** @Prop */
        retryConnectionCount = 0;

        /** @Prop */ isUserAdmin = true;

        /** @Prop */
        showDate = false;

        template = `
            <div>
                <!-- Property binding does not get reflected is changed -->
                <p>Binding User admin flag: @isUserAdmin</p>
                <button (click)="changeProp()">Update prop</button>
            </div>
        `;

        changeProp() {
            //This property is bound in line 18
            this.isUserAdmin = false;
            this.printPropNewValue();
        }

        printPropNewValue() {
            console.log(`New User Admin flag is: `, this.isUserAdmin);
        }
    }
    ```

Annotations can be defined in the same line as the variable like in <b>line 10</b> of previous example. <b>`Prop`</b> variables can also be bound (<b>line 18</b>) just as <b>`State`</b> variables, but changes to it won't reflect to binding.

Although <b>`Prop`</b> does not reactively reflect to binding, it natually have the expected reflection in the component internal flow (e.g. line 30) thereby totally suitable to be used in any business logic.

<br>

#### @Prop Special case of Reactive effect

This example takes into consideration the <b><a href="#example-setup">above</a></b> folder structure, app and routing setup.

<b>`Prop`</b> variables are made not to behave reactively, however, when combined with <a href="../directive/#the-showif-directive-example"><b>`(showIf)`</b></a> directive it will act reactively against it, follow the example with animated result right after:

=== "HomeComponent.js"
```js linenums="1" hl_lines="7 9 17 23" title="This component is placed in the app/base-components/ folder"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

	isPublic = true;

	/** @Prop */ date = new Date().toLocaleDateString();

	/** @Prop */ showDate = false;

	template = `
		<div>
			<p>Press the button to show the date</p>
			<!-- Binding a boolean property to (showIf) directive -->
			<p (showIf)="self.showDate">Today's date is <b>@date</b></p>
			<button 
                (click)="showTheDate()"
            >Show Date</button>
		</div>
	`;

	showTheDate() {
		this.showDate = !this.showDate;
	}

}
```

<b>Animated result</b>:

![Result](assets/img/ezgif.com-optimize.gif){style="display"}


<br>
<br>

###  Using <b>@Proxy</b> for Parent to child components communication

This example takes into consideration the <b><a href="#example-setup">above</a></b> folder structure, app and routing setup.

This is an approach provided in Still.js that enables ***parent-to-child components communication***, in this case, parent needs to define a <b>`@Proxy`</b> for every single child, this needs to be referenced in `<st-element proxy="myProxyVar">` tag. It's also nice to have the <b>`@type`</b> definition as it'll help with development experience in the intelicesnse and type hinting.

Bellow is a code sample with the animated result right after it:


=== "HomeComponent.js"

    ```js linenums="1" hl_lines="9-10 12-13 18-20 26 31 37 42 46" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { PersonForm } from "../person/PersonForm.js";
    import { PersonList } from "../person/PersonList.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** @Proxy @type { PersonForm } */
        personFormProxy;

        /** @Proxy @type { PersonList } */
        listPersonProxy;

        template = `
            <div>
                <p>Handle Person form from bellow buttons</p>
                <button (click)="changePersonText()">Change Person</button>
                <button (click)="callFromChild()">Call the Person</button>
                <button (click)="showMoreInList()">Handle Person List</button>
                <p>-</p>
            </div>

            <st-element 
                component="PersonForm"
                proxy="personFormProxy"
            ></st-element>

            <st-element 
                component="PersonList"
                proxy="listPersonProxy"
            ></st-element>
        `;

        changePersonText() {
            //This will update a state variable of the embeded component (PersonForm)
            this.personFormProxy.myText = `<b style="color:red;">Parent assigned value</b>`;
        }

        callFromChild() {
            //doSomething is child component method, and called througg the proxy
            this.personFormProxy.doSomething();
        }
    
        showMoreInList() {
            this.listPersonProxy.showMore = !this.listPersonProxy.showMore;
        }
    }
    ```

=== "PersonForm.js"

    ```js linenums="1" hl_lines="10 15 20-22" title="This component is placed in the app/person/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        //This is a state which reactively 
        //updates in case its value gets changed
        //And parent component will be changing it
        myText = 'Initial value';

        template = `
            <div>
                <p>I'm ParsonForm. My state is bound and will be updated by parent</p>
                <p>@myText</p>
            </div>
            <hr/><br/>
        `;

        doSomething() {
            this.myText = `<b style="color:green;">New value from the method</b>`;
        }
    }
    ```

=== "PersonList.js"

    ```js linenums="1" hl_lines="7 13" title="This component is placed in the app/person/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonList extends ViewComponent {

        isPublic = true;
        //Parent component is changing this Prop value
        /** @Prop */ showMore = false;

        template = `
            <div>
                <p>
                    I have additional content.
                    <div (showIf)="self.showMore">
                        This is Person more content
                    </div>
                </p>
            </div>
        `;

    }
    ```
<b>Animated result</b>

![Proxy Annotation](assets/img/proxy-annot-ezgif.com-optimize.gif)

<br>
<br>

<a name="inject-example"></a>
### <b>@Inject</b> - Use Services for Global store and HTTP services

This example takes into consideration the <b><a href="#example-setup">above</a></b> folder structure, app and routing setup.

It allows Service dependency injection offering a centralized way to handle data processing and bsiness logic. Services also provide Global Storage and are ideal for implementing HTTP calls.

Still.js uses a setter method at the application level (e.g., in <b>`app-setup.js`</b>) to define the folder for services. If services are located elsewhere, the <b>`@Path`</b> annotation can be used to speficy it in the example after this one.
<br>


=== "HomeComponent.js"

    ```js linenums="1" hl_lines="9-12 18 22-30" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { MainService } from "../services/MainService.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** 
         * @Inject
         * @type { MainService } 
         * */
        serviceObj;

        template = `
            <div>
                <p>Bellow Person List is being embeded</p>
                <!-- ParsonList also injects the MainService -->
                <st-element component="PersonList"></st-element>
            </div>
        `;

        stAfterInit() {
            //Register to the service onLoad hook
            this.serviceObj.on('load', async () => {
                // Assigning the API response to the Store
                const todos = await this.serviceObj.getTodos();
                // Update the todos Store with API response
                this.serviceObj.storeTodos(todos);
            });
        }

    }
    ```
    
=== "PersonList.js"

    ```js linenums="1" title="This component is placed in the app/person/ folder" hl_lines="9 11 19 26 29 36 38 41"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { MainService } from "../services/MainService.js";

    export class PersonList extends ViewComponent {

        isPublic = true;

        //This state will be updated with API response
        top2List = null;

        /** @Inject @type { MainService } */ servc;

        template = `
            <div>
                <p>
                    <br>
                    <b>The top 5 tasks are:</b>
                    <hr>
                    <div>@top2List</div>
                </p>
            </div>
        `;

        stAfterInit() {
            //Register to the service OnLoad hook
            this.servc.on('load', () => {
                //Assigning data from API, since this data is set by parent
                //component, it might be available once child gets rendered
                const apiResponse = this.servc.todosStore.value.slice(0, 5);

                let result = '';
                for (const user of apiResponse) {
                    result += '<p>' + JSON.stringify(user) + '</p>';
                }

                this.top2List = result;

                this.servc.todosStore.onChange((newResult) => {
                    //This will update the state in whenever service todosStore
                    //gets upated from anywhere
                    this.top2List = newResult;
                });
            });
        }

    }
    ```

=== "MainService.js"

    ```js linenums="1" title="This service is placed in the app/services/ folder" hl_lines="7 19"
    import { $still } from "../../@still/component/manager/registror.js";
    import { BaseService, ServiceEvent } from "../../@still/component/super/service/BaseService.js";

    export class MainService extends BaseService {

        // This store is being accessed in the PersonList
        todosStore = new ServiceEvent([]);

        // get todos from online Fake API, Called in the HomeComponent
        async getTodos() {
            const result = await $still
                .HTTPClient
                .get('https://jsonplaceholder.typicode.com/todos');
            return result;
        }

        // Set new todos to the store. Called in the HomeComponent
        storeTodos(todos) {
            this.todosStore = todos;
        }
    }
    ```


<b>Result picture:</b>

![Result](assets/img/inject-example1.png){style="display"}

<br>


### <b>@Controller</b> - Sharing UI feature between components

Just like the <a href="#inject-example"><b>`@Inject`</b></a>, the <b>`@Controller`</b> annotation allow to inject a controller to a component where a special situation as well as a constraint takes place as follow:

- ***Special case***: The controller annotated with <b>`@Controller`</b> is marked as the main controller of the component, which can be referenced in the template for HTML event binding using `controller.methodName()`.

- ***Contraint***: Only one controller can be annotate with <b>`@Controller`</b>, if more than one, the last one will take precedence. In contrast <b>`@Inject`</b> can be used more than one.

<br>

Example:
```js linenums="1" hl_lines="3-6" title="The controller"

//The controller
export class NameOfController extends BaseController {
    getInputValue(){
        const value = document.getElementById('inputId').value;
        return value;
    }
}
```

```js linenums="1" title="Injection in the component"

/**
 * @Controller
 * @Path path-to/controller-folder/
 * @type { NameOfController }
 */
 mainController;
```

```html linenums="1" hl_lines="3-4" title="Referencing in the component template"
<div>
    <form>
        <input type="text" id="inputId">
        <button onclick="controller.getInputValue()">Get Value</button>
    </form>
</div>
```

```html linenums="1" hl_lines="3" title="Referencing in anoter component template which didn't annotate with @Controller, or didn't inject at all"
<!-- This should be a child or adjacent component -->
<div>
    <button onclick="controller('NameOfController').getInputValue()">Get Value</button>
</div>
```


Controllers are a way for components to share features whereas the Services are for Data sharing, therefore, the use case for it is for when we have a component which can have different child or sibling, but, only the main component should inject as <b>`@Controller`</b>, other components will inject it normally or only reference in the template.

<br>
<br>

### <b>@Path</b> - Specifying service path when <b>@Inject</b>ing

This example takes into consideration the <b><a href="#example-setup">above</a></b> folder structure, app and routing setup.


<b>`@Path`</b> is a second level annotation that might to come hence that have to come right after @Inject. It recieves the path to the folder where the service is located. Follow the code sample with the animated result:



=== "HomeComponent.js"

    ```js linenums="1" hl_lines="2 9-13 22 28-32" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { UserService } from "../services/user/UserService.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** 
         * @Inject
         * @Path services/user/
         * @type { UserService } 
         * */
        serviceObj;

        //This prop is bound to the form input (line 21)
        searchParam;

        template = `
            <div style="padding: 10px;">
                <form onsubmit="return false;">
                    <input (value)="searchParam" placeholder="Type the user ID">
                    <button (click)="searchUser()">Search</button>
                </form>
                <st-element component="PersonList"></st-element>
            </div>
        `;

        async searchUser() {
            const userId = this.searchParam.value;
            const user = await this.serviceObj.getUserById(userId);
            console.log(user);
        }
    }
    ```
    
=== "PersonList.js"

    ```js linenums="1" title="This component is placed in the app/person/ folder" hl_lines="2 11 19 26 29 36 38 41"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { UserService } from "../services/user/UserService.js";

    export class PersonList extends ViewComponent {

        isPublic = true;

        //This state will be updated with API response
        foundUser;

        /** @Inject @type { UserService } */ servc;

        template = `
            <div>
                <p>
                    <br>
                    <b>Search result is:</b>
                    <hr>
                    <div>@foundUser</div>
                </p>
            </div>
        `;

        stAfterInit() {
            this.servc.on('load', () => {
                this.servc.userSearchResult.onChange((newResult) => {
                    //This will update the state in whenever service todosStore
                    //gets upated from anywhere (e.g. parent component)
                    this.foundUser = newResult;
                });
            });
        }

    }
    ```

=== "UserService.js"

    ```js linenums="1" title="This service is placed in the app/services/user/ folder" hl_lines="6 10-14"
    import { $still } from "../../../@still/component/manager/registror.js";
    import { BaseService, ServiceEvent } from "../../../@still/component/super/service/BaseService.js";

    export class UserService extends BaseService {

        userSearchResult = new ServiceEvent();

        // This is being called by the HomeComponent, and
        // because the store gets updated, PersonLis get nofitied
        async getUserById(userId) {
            const url = 'https://jsonplaceholder.typicode.com/users/' + userId;
            const user = await $still.HTTPClient.get(url);
            this.userSearchResult = `Name: ${user.name} - email: ${user.email}`;
        }
    }
    ```

<b>Animated Result:</b>

![Result](assets/img/svcpath-annot-ezgif.com-optimize.gif){style="display"}

<br>
<br>
<br>

