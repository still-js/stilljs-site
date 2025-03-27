!!! info "Work in Progress"

    Thee is yet a work in progress in this documentation, it means that some addiotnal content, scenarios and example are yet to be brought, nevertheless the current content cover from the basics to more elaborated scenarios.

<br/>

### StillJS Routing and Routing Object



#### Overview
- In Still.js Component is a way of handling just anything that results in a UI out put, can be a whole page/UI, a widget, an autonomos application part (e.g. Form, Grid, Datatable, Button, etc.), or even whole application (Micro-Fronted which can be put inside a regular page or HTML), plus, it can be resuable and navegable (in case of UI/page components).

- The component anatomy normally consider 2 required aspects, first it has to extend from ViewComponent and second it has to define the template variable which will be used to render the visual part of it, in some situations, a third aspect is to be taken into consideration which is the constructor definition (in case there is something we want to run when starting running the component) which in turn requires the super() method from parent class (.e.g ViewComponent, BaseService) to be called inside.

Since Still.js is based on Vanilla Web Technologies (HTML, CSS and JavaSCript) the content of the template variable will naturally be pure HTML, a defined WebComponent, a set of <st-element> or a combination of any or all of them.



### Simple example

=== "HomeComponent.js"

    ```js title="HomeComponent.js" linenums="1" hl_lines="12 19-21"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class HomeComponent extends ViewComponent {

        /** Need in any component as long as not dealing with parts 
         * only accessible in case of authenticated user
         * */
        isPublic = true;

        /**
         * constructor for still.js might be needed in very specific
         * situations (e.g. for using whenReady hook)
        */
        constructor() {
            super();
        }
    }
    ```

Conceptually, all components extends from ViewComponent, and, behide the, therefore, such extending component can serve as a whole page or a simple part of a specific page.

<br/>
#### Component Creation

- The recommended way fo Component creation is by using the still-cli utility (@stilljs/cli on npm), for that we run the command as follow:

    `npx still create component path/to/MyComponentName`

    <br>

- The create command for component options also provides with aliases, in this case we can abbreviate both the comand and the type of object to be created (component in this case):

    `npx st c cp path/to/UserDataTable`

    <br/>
    In the above example, you'll be creating a component with name UserDataTable in the specified path, there is no need to create he folders and sub-folders, as in case they don't exist it'll get created.

<br/>

#### Component required variables

- ***isPublic*** - This states if the component can be accessed without authentication or not.


- ***template*** - Declares the UI itself by using differnt murkups (HTML, Still elements, Web-Component) and stilesheets (CSS). Not declaring it will make the component not to load.


In adition to isPublic and template, there are other features which can be used inside the javaScript part of the component such as the speciall method/Hooks (see hooks section)

<br/>

#### Nested Component

It's possible to put one component inside another, nevertheless, in order to guarantee the better performance, Still.js only allow 2 levels of nested component as follow:


=== "Father Component"
	```js title="BiddingDisplay.js" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;
		template = `
            <st-element component="BidOffersComponent"></st-element>
            <st-element component="BiddersList"></st-element>
		`;

	}
	```

=== "Child Component"
	```js title="BidOffersComponent.js" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;
		template = `
			Hhere I'll have my code which provide the UI output concerning
            the offfers of the Bid.
		`;

	}
	```

=== "Anothe Child Component"
	```js title="BiddersList.js" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddersList extends ViewComponent {

		isPublic = true;
		template = `
			Here goes the list of bidders.
		`;

	}

	```

Above we have to father component, which has one level of offsprings, additional level is not allowed using `<st-element></st-element>`, anyway it can be achieved by using Web-component or regular HTML. (see best preactices sectio).


!!! abstract "Nesting Component considerations"

    Unlike Still.js component, Web-component and HTML tags are handled directly by the Browser, which means less burden and more performant UI, therefore, the concept in Still.js is that you have to design well the component and use &lt;st-element>&lt;/st-element> to handle the complex parts of your UI, and 3+ level of nested component for dealing with visual/formating aspects, this definitely will guarantee better performance.


<br/>

#### Component to Component communication

Covering from the most basic to the most complex scenarios, Still.js provides wide different means of providing communication from component to component (e.g. Parent to child, Sibling to Sibling, any component to any other(s)). (see)

<br>

##### Parent to Child


=== "Father Component"
	```js title="BiddingDisplay.js" hl_lines="10-11" linenums="1"
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

=== "Child Component"
	```js title="BidOffersComponent.js" hl_lines="11-12 7-8" linenums="1"
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

=== "Father Component"
	```js title="BiddingDisplay.js" hl_lines="12 16-18" linenums="1"
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

=== "Child Component"
	```js title="BidOffersComponent.js" hl_lines="13 17" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

        hieghestOffer = 0;
        leadBidderName = null;

		template = `
			<span>Hier Offer</span> @hieghestOffer
			<span>The leading Bidder is @leadBidderName</span>
            <button (click)="myMethodSignature()">Call Father Function</button>
		`;


        myMethodSignature(){}

	}
	```

Unlike state and property variables, method on the `<st-element>` component need to be references in paranthesis (), also, normally in the child we'll have the method signature, nevertheless we can also have it's own scope.

It's also possible for the child to pass values to parent when executing method signature, follow the example:

=== "Father Component"
	```js title="BiddingDisplay.js" hl_lines="13-15 9" linenums="1"
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

=== "Child Component"
	```js title="BidOffersComponent.js" hl_lines="8 13" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

		template = `
            <button (click)="processMyData(30, 'John')">
                Call Father Function
            </button>
		`;

        myMethodSignature(age, name){}

	}
	```