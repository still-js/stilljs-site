### Overview
Still provides with different types of Hooks not only when it comes to component Lifecycle but for additional specific context. Services (<b>`@Inject`</b> annotation) and Proxies (<b>`@Proxy`</b> annotation) also provide a hook (<a href="#stOnUnload-hook">see this example</a>) that can be used for components to subscribe so that they get triggered/notified when the service is loaded/ready.

<br>

### Component Lifecycle Hooks/Special Methods


Essentially, in Still.js the component Lifecycle comprises 4 special methods (Hooks) as depicted in blue rectangles in the bellow diagram: <br><br>

![Component Lyfecycle](assets/img/StillJS%20component-fifecycle.png#lcycle){width="600px" border="1px solid black" style="margin: 0 auto"}.

<style>
    img[src*="#lcycle"] {
        margin 0 auto;
        display: block;
    }
</style>

<br>
<br>

<a name="example-setup"></a>

### Examples Setup

The examples in this documentation/tutorials will be base in the bellow <b>folder structure</b>, <b>Application Setup</b> (<b>`app-setup.js`</b>) and routes metadata (<b>`route.map.js`</b>)

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ base-components/
    |    |   |__ HomeComponent.js
    |    |   |
    |    |__ person/
    |    |   |__ PersonForm.js
    |    |   |
    |    |__ services/
    |    |   |__ MainService.js
    |    |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="11 16 4" linenums="1"
	import { StillAppMixin } from "./@still/component/super/AppMixin.js";
	import { Components } from "./@still/setup/components.js";
	import { AppTemplate } from "./app-template.js";
	import { HomeComponent } from "./app/base-components/HomeComponent.js";

	export class StillAppSetup extends StillAppMixin(Components) {

		constructor() {
			super();
			//Defines the first component to load
			this.setHomeComponent(HomeComponent);
		}

		async init() {
			//Loads the app container and the initial component set at line 11
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
                    url: "/person/register" //This url was changed conviniently
                }
            },
            lazyInitial: {}
        }
    }
	```

<br>
<br>

###  The <b>`stOnRender()`</b> Special method (Hook)

This example takes into consideration the <b><a href="#initial-setup">above</a></b> folder structure, app and routing setup.

This hook runs immediately after the component is instantiated. While the component isn't fully ready yet, it's suitable for actions like making API calls or showing a loading spinner.

=== "HomeComponent.js"
```js linenums="1" hl_lines="9-11" title="This component is placed in the app/base-components/ folder"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

	isPublic = true;

	template = `Hooks example`;

	stOnRender() {
		console.log(`Component was created but not ready for use yet`);
	}

}
```

<br>
<br>

###  The <b>`stAfterInit()`</b> Special method (Hook)

This example takes into consideration the <b><a href="#initial-setup">above</a></b> folder structure, app and routing setup.

This takes place whenever the component was render and it's totally available for usage, in this stage we can for example access to DOM tree of such component.

=== "HomeComponent.js"
```js linenums="1" hl_lines="9 13-16" title="This component is placed in the app/base-components/ folder"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

	isPublic = true;

	template = `
        <div 
            id="theId">
            Hooks example
        </div>`;

	stAfterInit() {
		console.log(`Component was rendered, and ready to be manipulated, printing its HTML content bellow:`);
		console.log(document.getElementById('theId').innerHTML);
	}


}
```
<br>
<br>

###  The <b>`stOnUpdate()`</b> Special method (Hook)

This example takes into consideration the <b><a href="#initial-setup">above</a></b> folder structure, app and routing setup.

This hook takes place everytime a component state gets changed since this is the change that reflects the UI. Component update triggers either the component updates itself or by another component.

=== "HomeComponent.js"

    ```js linenums="1" hl_lines="8-9 14 18 24" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { PersonForm } from "../person/PersonForm.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** @Proxy @type { PersonForm } */
        personForm;

        template = `
            <div>
                Home component which embeds another and set a proxy
                <button (click)="changePersonText()">Change Person</button>
            </div>
            <st-element 
                component="PersonForm"
                proxy="personForm"
            ></st-element>
        `;

        changePersonText() {
            //This will update a state variable of the embeded component (PersonForm)
            this.personForm.myText = 'New Value';
        }
    }

    ```

=== "PersonForm.js"

    ```js linenums="1" hl_lines="9 14 19-21" title="This component is placed in the app/person/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        //This is a state which reactively 
        //updates in case its value gets changed
        myText = 'Initial value';

        template = `
            <div>
                <p>My state is bound and will be updated by parent</p>
                <p>@myText</p>
            </div>
        `;

        //Hooks that takes place when state update happens
        stOnUpdate() {
            console.log(`I'm being updated by another component`);
        }

    }
    ```

<br><br>

<a name="stOnUnload-hook"></a>

###  The <b>`stOnUnload()`</b> Special method (Hook)

This example takes into consideration the <b><a href="#initial-setup">above</a></b> folder structure, app and routing setup.

It takes place especially when destroying a component, which happens when navigating from one component or page to another. A basic use case for it would be if we need to clear some data in a global store (Service).

=== "HomeComponent.js"

    ```js linenums="1" hl_lines="9-13 18 31-35" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { MainService } from "../services/MainService.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        /** 
         * @Inject
         * @Path services/
         * @type { MainService } 
         * */
        serviceObj;

        template = `
            <div>
                <p>This is the home, click bellow to go to Person Form</p>
                <button (click)="goto('PersonForm')">Register Person</button>
            </div>
        `;

        stOnRender() {
            // Bellow variable will hold a very bi API response data
            const apiResponse = [];
            //In here we substribe to the service onLoad hook
            this.serviceObj.on('load', () => {
                // Assigning the API response to the Store
                this.serviceObj.personStore = apiResponse;
            });
        }

        stOnUnload() {
            console.log(`BEFORE CLEARING: `, this.serviceObj.personStore.value);
            this.serviceObj.personStore = null;
            console.log(`AFTER CLEARING: `, this.serviceObj.personStore.value);
        }

    }
    ```
    
=== "PersonForm.js"

    ```js linenums="1" title="This component is placed in the app/person/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class PersonForm extends ViewComponent {

        isPublic = true;

        template = `
            <div>
                <p>This is the PersonForm content</p>
            </div>
        `;

    }
    ```

=== "MainService.js"

    ```js linenums="1" title="This service is placed in the app/services/ folder"
    import { BaseService, ServiceEvent } from "../../@still/component/super/service/BaseService.js";

    export class MainService extends BaseService {

        personStore = new ServiceEvent([]);

    }
    ```
<br>
<br>

<hr/>

###  The <b>`stWhenReady()`</b> Special method (Hook)

This example takes into consideration the <b><a href="#initial-setup">above</a></b> folder structure, app and routing setup.

This is a hook that works the same way as the <b>`stAfterInit()`</b>, the only different is that it's not called in the class level but inside a method in the class (e.g. `constructor`). A use case for this hook would be when the implementing component needs to run something on top of another unrelated (nor sibling or child) component gets loaded/rendered since it would never have controle over it.



=== "HomeComponent.js"

    ```js linenums="1" hl_lines="7 14-16" title="This component is placed in the app/base-components/ folder"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;

        myStateVariable = 'My Initial value';

        template = `Hooks example using stWhenReady()`;

        constructor() {
            super();

            this.stWhenReady(() => {
                console.log(`My State value is: `, this.myStateVariable.value)
            });
        }

    }
    ```

<br>
<br>
