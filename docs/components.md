!!! info "Work in Progress"

    Thee is yet a work in progress in this documentation, it means that some addiotnal content, scenarios and example are yet to be brought, nevertheless the current content cover from the basics to more elaborated scenarios.


!!! failure "<u>ViewComponent</u> and <u>BaseService</u> import in <a href="../installation-and-running-cdn/">CDN/Lone component mode</a>"

	The import (e.g. `import { ViewComponent } from "@still/component/super/ViewComponent.js"`) of <b>ViewComponent</b> and <b>BaseService</b> classes is inexistent <a href="../installation-and-running-cdn/">CDN mode setup</a>, as this is already provided by CDN itself.
<br/>

### Overview
- In Still.js, a Component represents any UI output, from a full application to a widget or a microfrontend. Components can be reusable, navigable (for UI/pages), and embedded within other applications.

- A component must extend <b>`ViewComponent`</b> and define a <b>`template`</b> for rendering. If initialization logic is needed, a Special methods (lifecycle/Hook) can be implemented, if constructor is in place <b>`super()`</b> needs to be called as first line.

- For proper localization/routing, both <b>Path</b> and <b>URL</b> must be defined in <b>`route.map.js`</b>. However, this is handled automatically when creating components via <b>still-cli</b> (<a href="#component-creation">check bellow</a>). The <b>`app-setup.js`</b> manages application-level configurations, but for these tutorials we'll be touching it just to set the initial component we want to be loaded.

In Still.js, the template variable contains pure HTML, a defined WebComponent, &lt;st-element> tags, or a combination of these, as it is based on vanilla web technologies (HTML, CSS, and JavaScript).



### 1. Simple example

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ home/
    |    |   |__ HomeComponent.js
    |    |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="11 16" linenums="1"
	import { StillAppMixin } from "./@still/component/super/AppMixin.js";
	import { Components } from "./@still/setup/components.js";
	import { AppTemplate } from "./app-template.js";
	import { HomeComponent } from "./app/home/HomeComponent.js";

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
	```js title="Routes will be added and manage automatically from here when creating the component using still-cli" hl_lines="11 16" linenums="1"
	export const stillRoutesMap = {
		viewRoutes: {
			regular: {
				HomeComponent: { path: "app/home", url: "/HomeComponent" }
			},
			lazyInitial: {}
		}
	}
	```

=== "HomeComponent.js"

    ```js title="HomeComponent.js" linenums="1" hl_lines="3-17"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class HomeComponent extends ViewComponent {

        /** Need in any component as long as not dealing with parts 
         * only accessible in case of authenticated user
         * */
        isPublic = true;

        /**
         * constructor for still.js might be needed in very specific
         * situations (e.g. for using whenReady() Hook)
        */
        constructor() {
            super();
        }
    }
    ```


Conceptually, all components extends from ViewComponent, and, behide the, therefore, such extending component can serve as a whole page or a simple part of a specific page.

<a name="component-creation"></a>
<br/>
#### Component Creation

- The recommended way fo Component creation is by using the still-cli utility (<b>@stilljs/cli</b> on npm), for that we run the command as follow:

    ```
	npx still create component path/to/MyComponentName
	```
	!!! warning "Component creation folder context"
		The component creation command instruction needs to be run inside s Still.js project, or in the <b>`app/`</b> (which is inside the Still.js project) folder or a subfolder of the <b>`app/`</b> folder

    <br>

- The create command for component options also provides with aliases, in this case we can abbreviate both the comand and the type of object to be created (component in this case):

    ```
	npx st c cp path/to/UserDataTable
	```

    <br/>
    In the above example, you'll be creating a component with name UserDataTable in the specified path, there is no need to create he folders and sub-folders, as in case they don't exist it'll get created.

<br/>

#### 1.1 Component required/reserved variables (Reserved for the Framework)

- ***isPublic*** - This states if the component can be accessed without authentication or not.


- ***template*** - Declares the UI itself by using differnt murkups (HTML, Still elements, Web-Component) and stylesheets (CSS). In case the template is defined in an HTML (<a href="../get-start/#template-splitting">see here</a>) file then temlate variable should not exist in the component.


In adition to isPublic and template, there are other features which can be used inside the javaScript part of the component such as the special method/Hooks (see hooks section), follow an example:

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ components/
    |    |   |__ user/
    |    |   |   |__ UserForm.js
    |    |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="11 16" linenums="1"
	import { StillAppMixin } from "./@still/component/super/AppMixin.js";
	import { Components } from "./@still/setup/components.js";
	import { AppTemplate } from "./app-template.js";
	import { UserForm } from "./app/components/user/UserForm.js";

	export class StillAppSetup extends StillAppMixin(Components) {

		constructor() {
			super();
			//Defines the first component to load
			this.setHomeComponent(UserForm);
		}

		async init() {
			//Loads the app container and the initial component set at line 11
			return await AppTemplate.newApp();
		}

	}
	```

=== "route.map.js"
	```js title="Routes will be added and manage automatically from here when creating the component using still-cli" hl_lines="11 16" linenums="1"
	export const stillRoutesMap = {
		viewRoutes: {
			regular: {
				UserForm: { path: "app/components/user", url: "/user/create" }
			},
			lazyInitial: {}
		}
	}
	```


=== "UserForm.js"
	```js title="Defining the template" hl_lines="8-16" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class UserForm extends ViewComponent {

		isPublic = true;

		 template = `
		 	<section>
				<article>
					<header>This is my title</header>
					<div>
						My article content with relevant summary
					</div>
					<button>Learn more</botton>
				</article>
		 	</section>
		 `;
	}
	```
The template (HTML) content will be display accordingly once the template as rendered. Again, template can also contain Web-component and/or Still component which would be a child component in this case.



<br>

### 2. Component State vs Property

Those are 2 of the existing ways for the component to hold data, therefore, they serve different purpose, as State is reactive and takes affect on the component lifecycle, whereas Property does not. Follow the example:


=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ components/
    |    |   |__ user/
    |    |   |   |__ UserForm.js
    |    |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="11 16" linenums="1"
	import { StillAppMixin } from "./@still/component/super/AppMixin.js";
	import { Components } from "./@still/setup/components.js";
	import { AppTemplate } from "./app-template.js";
	import { UserForm } from "./app/components/user/UserForm.js";

	export class StillAppSetup extends StillAppMixin(Components) {

		constructor() {
			super();
			//Defines the first component to load
			this.setHomeComponent(UserForm);
		}

		async init() {
			//Loads the app container and the initial component set at line 11
			return await AppTemplate.newApp();
		}

	}
	```

=== "route.map.js"
	```js title="Routes will be added and manage automatically from here when creating the component using still-cli" hl_lines="11 16" linenums="1"
	export const stillRoutesMap = {
		viewRoutes: {
			regular: {
				UserForm: { path: "app/components/user", url: "/user/create" }
			},
			lazyInitial: {}
		}
	}
	```

=== "UserForm.js"
	```js title="Defining Properties and States" hl_lines="9-12 16-17 19-20 22 24-26 28-30 32-34" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class UserForm extends ViewComponent {

		isPublic = true;

		/* Those states and have
		 * reactive feature/behavior */
		firstName;
		age;
		gender;
		department;

		/* Those Property, they have to be annotated with @Prop and anotation
		 * ca be in the same or in a different line as the property itself */
		/** @Prop */ 
		showCredentialsTab = false;

		/** @Prop */ 
		myHtmlContainerId;
		
		/** @Prop */ saveButtonLabl = 'Save User';

		printUserFirstName(){
			console.log(this.firstName.value);
		}

		assigneUserFirstName(newName){
			this.firstName = newName;
		}

		printContainerId(){
			console.log(this.myHtmlContainerId)
		}

	}
	```

When it comes to retrieve the value from a property we need to reference the `.velue` (line 25), but this is not the case for property (line 33). 

To listen to a State change reactively, some ways are provided, but more recurrent are binding it to the template, and subscribing to it as follows in the side code snippets:


```js title="Listening to changes" hl_lines="3-4 8-12"
	// Via property binding in the template it automatically listen to changes reactively
	template = `
		<div>User Name: @firstName
		<button> @saveButtonLabl </button>
	`;

	// This is a Special method/Hook which can be declared in the component
	stAfterInit(){
		this.firstName.onChange(newValue => {
			console.log(`User first name changed to ${newValue}`);
		});
	}

```
A component can subscribe to itself just like any other component can as we see in the lines 8 to 10, therefore, a good place to declare subsription is in a Hook method like stAfterInit.



<br/>

### 3. Nested Component

It's possible to put one component inside another, nevertheless, in order to guarantee the better performance, Still.js only allow 2 levels of nested component as follow:

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ components/
    |    |   |__ bidding/
    |    |   |   |__ BiddingDisplay.js
    |    |   |   |__ BidOffersComponent.js
    |    |   |   |__ BiddersList.js
    |    |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="Definition of the service folder" linenums="1" hl_lines="10"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { BiddingDisplay } from "./app/components/bidding/BiddingDisplay.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            this.setHomeComponent(BiddingDisplay);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
	```

=== "route.map.js"
	```js title="" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                BiddingDisplay: {
                    path: "app/components/bidding",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/bidding",
                    url: "/bid/offer"
                },
                BiddersList: {
                    path: "app/components/bidding",
                    url: "/bid/bidder"
                }
            },
            lazyInitial: {}
        }
    }
	```

=== "BiddingDisplay.js"
	```js title="Parent Component" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;
		template = `
            <st-element component="BidOffersComponent"></st-element>
            <st-element component="BiddersList"></st-element>
		`;

	}
	```

=== "BidOffersComponent.js"
	```js title="Child Component" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;
		template = `
			Hhere I'll have my code which provide the UI output concerning
            the offfers of the Bid.
		`;

	}
	```

=== "BiddersList.js"
	```js title="Another Child Component" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddersList extends ViewComponent {

		isPublic = true;
		template = `
			Here goes the list of bidders.
		`;

	}

	```

Above we have to parent component, which has one level of offsprings, additional level is not allowed using `<st-element></st-element>`, anyway it can be achieved by using Web-component or regular HTML. (see best preactices sectio).


!!! abstract "Nesting Component considerations"

    Unlike Still.js component, Web-component and HTML tags are handled directly by the Browser, which means less burden and more performant UI, therefore, the concept in Still.js is that you have to design well the component and use &lt;st-element>&lt;/st-element> to handle the complex parts of your UI, and 3+ level of nested component for dealing with visual/formating aspects, this definitely will guarantee better performance.


<br/>

<a name="st-element-parent-child-communication"></a>
### 4. Component to Component communication

Covering from the most basic to the most complex scenarios, Still.js provides wide different means of providing communication from component to component (e.g. Parent to child, Sibling to Sibling, any component to any other(s)). (see to the <a href="../components-communication">Component Communication for more details</a>)

<br>

#### 4.1 Parent to Child communication


=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ components/
    |    |   |__ bidding/
    |    |   |   |__ BiddingDisplay.js
    |    |   |   |__ BidOffersComponent.js
    |    |   |   |
    |__ config/
    |    |__ app-setup.js
    |    |__ route.map.js
    |__  ...

	```

=== "app-setup.js"
	```js title="" linenums="1" hl_lines="10"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { BiddingDisplay } from "./app/components/bidding/BiddingDisplay.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            this.setHomeComponent(BiddingDisplay);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
	```

=== "route.map.js"
	```js title="" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                BiddingDisplay: {
                    path: "app/components/bidding",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/bidding",
                    url: "/bid/offer"
                },
            },
            lazyInitial: {}
        }
    }
	```

=== "BiddingDisplay.js"
	```js title="Parent Component" hl_lines="10-11" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;
        
		template = `
            <st-element 
                component="BidOffersComponent"
                hieghestOffer="30"
                leadBidderName="Gregor"
            ></st-element>
		`;
	}
	```

=== "BidOffersComponent.js"
	```js title="Child Component called inside BiddingDisplay" hl_lines="11-12 7-8" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

        hieghestOffer = 0;
        leadBidderName = null;

		template = `
			<span>Hier Offer</span> @hieghestOffer
			<span>The leading Bidder is @leadBidderName</span>
		`;

	}
	```


    
Parent component is passing 2 (hieghestOffer, leadBidderName) properties 
when referencing the child, those are states variables in the child whichwill be overriden.


Just like it's possible to update child state by passing if as property in `<st-element>` tag, we can also pass method as follow:

=== "BiddingDisplay.js"
	```js title="Parent Component" hl_lines="12 16-18" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;
        
		template = `
            <st-element 
                component="BidOffersComponent"
                hieghestOffer="30"
                leadBidderName="Gregor"
                (myMethodSignature)="alertMyChild()"
            ></st-element>
		`;

        alertMyChild(){
            alert('Hello my child')
        }
	}
	```

=== "BidOffersComponent.js"
	```js title="Child Component" hl_lines="13 17" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

        hieghestOffer = 0;
        leadBidderName = null;

		template = `
			<span>Hier Offer</span> @hieghestOffer
			<span>The leading Bidder is @leadBidderName</span>
            <button (click)="myMethodSignature()">Call Parent Function</button>
		`;


        myMethodSignature(){}

	}
	```

Unlike state and property variables, method on the `<st-element>` component need to be references in paranthesis (), also, normally in the child we'll have the method signature, nevertheless we can also have it's own scope.

It's also possible for the child to pass values to parent when executing method signature, follow the example:

=== "BiddingDisplay.js"
	```js title="Parent Component" hl_lines="13-15 9" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;
        
		template = `
            <st-element 
                (processMyData)="alertMyChild()"
            ></st-element>
		`;

        printChildDetailes(age, name){
            console.log(`Hello ${name} you're ${age} years old!`)
        }
	}
	```

=== "BidOffersComponent.js"
	```js title="Child Component" hl_lines="8 13" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

		template = `
            <button (click)="processMyData(30, 'John')">
                Call Parent Function
            </button>
		`;

        myMethodSignature(age, name){}

	}

In addition to using `<st-element>` component props, there are other means available for component to component communication such as `Pub/Sub`, both <a href="../components-communication#proxy-example"><b>`@Proxy`</b></a> and <a href="../components-communication#reference-example"><b>`ref`</b></a> which is done to through `<st-element>` again, and the <a href="../components-communication#service-example"><b>`Service`</b></a> which is a global kind. (see to the <a href="../components-communication">Component Communication</a>).

<br>


!!! Note "Embieding component in your regular HTML or within other Frameworks"

    When it comes to components, Still.js provides the Lone Component which only require to reference the CDN for both CSS and JavaScript files thereby not needing to create a Still.js project, therefore, this approach can be followed either for small use case as well as for complex ones such as Microfrontend. (follow do documentation here)

<br>
<br>


