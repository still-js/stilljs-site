### Still.js Routing and Router Object

### Overview
Unlike some other framerowkrs Still.js has a built-in navitation capabilities, basically it provides with a different was of addressing it from basically jumping from one component/page to another to a more robust use cases such as passing data when navigating and URL navigation. By default the navigation won't reflect the URL in the browser navigation bar, for that we need to pass the URL para as true.

All Routing capabilities in the Framework is provided by the Router Helper/Object, it taks care of data passing, handles route name and url.

Component metadata for navigation is provided through the <b>`route.map.js`</b> file, it contains three data for each component, such metadata is added automatically when component is created using still-cli (<a href="../components/#component-creation">see here</a>), and eache component metadata has the format as follow:

```js
{
    RouteName: { path: 'path/to-the/component/folder/', url: '/component-url' }
}
```
<br>

- ***Route name*** - A component's name, used for navigation, must be unique across the project (except for vendor components) and <b style="color:red;">cannot be changed</b> unless the component itself is renamed.


- ***path*** - It's the folder path where the component is located and <b style="color:red;">cannot be changed</b> unless the component is physically moved to a different folder.

- ***url*** - It can be used in the browser navigation bar or in a regular HTML link, <b style="color:green;">it can be changed</b> as per the dev will.

<a name="route-map-file"></a>

Throughout this documentation/tutorial taking into consideration the component that will be represented, the Routing file (<b>`route.map.js`</b>), the <b>project structure</b> and the <b>`app-setup.js`</b> will be set as shown bellow, in `app-setup.js` we set the <b>`MainMenuComponent`</b> as first loading component:

=== "route.map.js"

    ```js title="Application Setup stating MainMenuComponent as the first component to load" linenums="1" hl_lines="10"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { MainMenuComponent } from "./app/navigation/MainMenuComponent.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            this.setHomeComponent(MainMenuComponent); //This will be the first component to be loaded
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
    ```

=== "route.map.js"

    ```js title="Routing mapping file which resides in the project root folder" linenums="1" hl_lines="10-21"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                /** HomeComponent won't be used, but this is generated automatically 
                 * when starting the project */
                HomeComponent: {
                    path: "app/home",
                    url: "/HomeComponent"
                },
                MainMenuComponent: {
                    path: "app/navigation",
                    url: "/main-menu"
                },
                PersonForm: {
                    path: "app/person",
                    url: "/person/register"
                },
                PersonList: {
                    path: "app/person",
                    url: "/person/list"
                }
            },
            lazyInitial: {}
        }
    }
    ```

=== ":octicons-project-roadmap-16: Project folder structure"
    ```python title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ navigation/ #-> This is component folder
    |    |   |__ MainMenuComponent.js
    |    |   |
    |    |__ person/ #-> This is component folder
    |    |   |__ PersonForm.js
    |    |   |__ PersonList.js
    |    |   |
    |__ app-setup.js
    |__ route.map.js
    |__  ... #-> Remaining files

    ```



!!! warning "Routes generation and management "
    When using still-cli to generate the components, routes are added automatically as well as the component name conflicts is checked, also, <b style="color:red;">it's not recommended</b> at all to generate components manually.

<br>

###  Navigation using goto in the <b>`(click)`</b> directive event

This example takes into consideration the <b>route mapping file</b> and <b>folder structure</b> <a href="#route-map-file">defined above</a>.

In addition to allow component method binding, the <b>`(click)`</b> directive also has a capability to provide navigation withouth any method binding, as only <b>`goto()`</b> is needed to be specified, ans pass the Route name.

=== "MainMenuComponent.js"

    ```js title="Using goto() with (click) directive to navigate to another component/page" linenums="1" hl_lines="10 11"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class MainMenuComponent extends ViewComponent {

        isPublic = true;
        template = `
            <div>
                This is the main menu, Select Your desired option
                <div>
                    <button (click)="goto('PersonForm')">Register new Person</button>
                    <button (click)="goto('PersonList')">List Persons</button>
                </div>
            </div>
        `;
    }
    ```

=== "PersonList.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="11"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonList extends ViewComponent {

        isPublic = true;
        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Here will be the list previous registered persons
                </p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

    }
    ```

=== "PersonForm.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="11"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;
        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Showing Person registration form in here
                </p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

    }
    ```
This is simple navigation approach, where only it's needed to go from one component/page to another, anyway, more powerfull navigation is possible using the same directive.

<br>
<br>

<a name="goto-pass-data"></a>

### Passing Data from Component to Component when navigating using <b>`goto()`</b>

This example takes into consideration the <b>route mapping file</b> and <b>folder structure</b> <a href="#route-map-file">defined above</a>.

=== "MainMenuComponent.js"

    ```js title="Passing Data to the target component to be navigated to" linenums="1" hl_lines="9-13 20 23"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class MainMenuComponent extends ViewComponent {

        isPublic = true;

        /** Value of this property will be send to PersonForm when navigating
         * it could either be a state (no annotation), would work the same was
         * @Prop 
         * */
        complexData = {
            name: 'Mayor', skills: 'Programming'
        };

        template = `
            <div>
                This is the main menu, Select Your desired option
                <div>
                    <button 
                        (click)="goto('PersonForm', self.complexData)"
                    >Register new Person</button>
                    <button 
                        (click)="goto('PersonList', 'A simple string')"
                    >List Persons</button>
                </div>
            </div>
        `;
    }
    ```

=== "PersonList.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="2 10 15 22"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class PersonList extends ViewComponent {

        isPublic = true;

        //This is a state which reactively 
        //updates in case its value gets changed
        myText = null;

        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>Here will be the list previous registered persons. State binding bellow:</p>
                <p>@myText</p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

        stOnRender() {
            //Retrieve the data by using the Router helper
            this.myText = Router.data(this);
        }
    }
    ```

=== "PersonForm.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="2 8 15 21 24"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        myObjectState = null;

        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Showing Person registration form in here, State binding bellow:
                </p>
                <p>@myObjectState</p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

        stAfterInit() {
            const myData = Router.data(this);
            /** Because data is JSON object we're stringifying 
             * reactively to print it in the page */
            this.myObjectState = JSON.stringify(myData);
        }
    }
    ```

***MainMenuComponent*** - 2 scenarios are in place, first (<b>line 20</b>) we're passing a complex data structure to another component by navigation, hence we need to assign to a variable (state or prop) in the component. The second scenario (<b>line 23</b>), we're just passing a string, hence we only need to enclose it in single quotation mark.


***PersonList*** Used state variable for reactive template binding. Data is fetched using the Router helper, which requires the target object as input. <b>`stOnRender()`</b> hook triggers this process when the component is rendering.


***PersonForm*** Used state variable for reactive template binding. in this case, because Data is a JSON object, it's being stringified before assignment. <b>`stAfterInit()`</b> hook triggers  when the component is rendered.

<br>
<br>

<a name="router-helper"></a>

### Router Helper - Routing inside a Business logic/Method

This example takes into consideration the <b>route mapping file</b> and <b>folder structure</b> <a href="#route-map-file">defined above</a>.

=== "MainMenuComponent.js"

    ```js title="Navigation whith business logic implemented with Router Helper" linenums="1" hl_lines="2 12 21 23"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class MainMenuComponent extends ViewComponent {

        isPublic = true;

        template = `
            <div>
                This is the main menu, Select Your desired option
                <div>
                    <button (click)="registerPerson()">Register new Person</button>
                </div>
            </div>
        `;

        registerPerson() {
            const myValidation = true;
            if (myValidation) {
                //Data (2nd param) can be of any type (object, string, number, array, etc.)
                Router.goto('PersonForm', { data: { name: 'Dany', skills: 'None' } });
            } else {
                Router.goto('PersonForm');
            }
        }
    }
    ```


=== "PersonForm.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="8 15 21 24"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        myObjectState = null;

        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Showing Person registration form in here, State binding bellow:
                </p>
                <p>@myObjectState</p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

        stAfterInit() {
            const myData = Router.data(this);
            /** Because data is JSON object we're stringifying 
             * reactively to print it in the page */
            this.myObjectState = JSON.stringify(myData);
        }
    }
    ```

***MainMenuComponent*** - We've implemented a method which uses the <b>Route helper</b> for navigation through the <b>`.goto()`</b>. Unlike the (click) directive, the goto through the Helper recieves an object as second parameter, this object has varios properties, and data can be of any type.


***PersonForm*** Used state variable for reactive template binding. in this case, because Data is a JSON object, it's being stringified before assignment. <b>`stAfterInit()`</b> hook triggers  when the component is rendered.


<br><br>

### Router Helper within Lone component
This example takes into consideration the <b>route mapping file</b> and <b>folder structure</b> <a href="#route-map-file">defined above</a>.

When it comes to Microfrontend, there might be a situation where more than one Still.js microfronted is present, for this reason, when dealing with navigation it's important for the Router to know which frontend should be affected.

=== "MainMenuComponent.js"

    ```js title="Passing the serviceId event when it comes to using Router in Lone component context" linenums="1" hl_lines="2 13 21-24"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class MainMenuComponent extends ViewComponent {

        isPublic = true;


        template = `
            <div>
                This is the main menu, Select Your desired option
                <div>
                    <button (click)="registerPerson()">Register new Person</button>
                </div>
            </div>
        `;

        registerPerson() {
            const myValidation = true;
            if (myValidation) {
                Router.goto('PersonForm', {
                    data: { name: 'Dany', skills: 'None' },
                    evt: Router.serviceId
                });
            } else {
                Router.goto('PersonForm');
            }
        }
    }
    ```

=== "PersonForm.js"

    ```js title="Main menu has navigation to here, and vice-versa" linenums="1" hl_lines="8 15 21 24"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        myObjectState = null;

        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Showing Person registration form in here, State binding bellow:
                </p>
                <p>@myObjectState</p>
                <button (click)="goto('MainMenuComponent')">Go to main menu</button>
            </h1>
        `;

        stAfterInit() {
            const myData = Router.data(this);
            /** Because data is JSON object we're stringifying 
             * reactively to print it in the page */
            this.myObjectState = JSON.stringify(myData);
        }
    }
    ```

To specify which microservice is triggering the navigation, we just need to pass the <b>`evt`</b> property (<b>line 23</b>) in the second parameter which is assigned with serviceId from Router helpr, this id is generated and managed internally by the Router itself, we're just informing that the navigation event it triggered from such service.

!!! info "ServiceId without Router Helper"
    When using the <b>`goto()`</b> with the <b>`(click)`</b> directive we don't need to inform the <b>serviceId</b> as it's taken care automatically by the router helper.

<br><br>

### Making navigation reflect the browser URL in navigation Bar

As depicted above, by default the navigation won't reflect the in the browser URL, anyway, in both scenarios (using `goto()` in the `(click)` directive - <a href="#router-helper">see here</a>) as well as (`Router Helper` - <a href="#goto-pass-data">see here</a>), we can instruct the Router to put the URL by passing url parameter as true, as follow:

- ***goto() with (click) directive*** - it will be `goto('RouteName','Data',true)`, where url param is the 3rd pararmeter, and data can be passed as null if not needed.


- ***Router Helper*** - It'll be `Router.goto('RouteName', {url: true})`, and as shown in the <a href="#goto-pass-data">Router Helper example</a> data can be passed as a property of a second parameter along with the url flag.


<br><br>

### Using the URL defined in the <b>`route.map.js`</b>

This example takes into consideration the <b>route mapping file</b> and <b>folder structure</b> <a href="#route-map-file">defined above</a>.

Regular URL navigaition is in place through the component mapped URL, however, as of now it does not support data passing, this capability will be provided in the future. Follow the example:

=== "MainMenuComponent.js"

    ```js title="Navigates to another component by using its url" linenums="1" hl_lines="11"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class MainMenuComponent extends ViewComponent {

        isPublic = true;

        template = `
            <div>
                This is the main menu, Select Your desired option
                <div>
                    <a href="#/person/register">Register new Person</a>
                </div>
            </div>
        `;
    }
    ```


=== "PersonForm.js"

    ```js title="Goes back to MainMenu by using its url" linenums="1" hl_lines="11"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;
        template = `
            <h1 class="still-fresh-generated-cmp">
                <p>
                    Showing Person registration form in here
                </p>
                <a href="#/main-menu">Go to main menu</a>
            </h1>
        `;

    }
    ```
Navigation via URL requires the usage of the HTML link (&lt;a>) tag, and the URL needs to be prefixed with hash (#) character when assigning the url in the `href`.


<br>
# Enjoy your navigations!
<br>