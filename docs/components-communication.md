### Private Component

!!! info "Work in Progress"

    Thee is yet a work in progress in this documentation, it means that some addiotnal content, scenarios and example are yet to be brought, nevertheless the current content cover from the basics to more elaborated scenarios.

<br/>

### Overview

In order to provide ways from components to communicate to each other, Still.js provade with different options thereby covering all scenarios such as Parent to child, Sibling to Sibling, any component to any other(s), follow the documentation.

<a name="proxy-example"></a>

### 1. Component State change Subscription (Pub/Sub)

State Subscription is a way for one Component to listen to another component State changes by subcribing to it. follow the example:

=== "BiddingDisplay.js"
	```js title="This is the parent component" hl_lines="11-15 19-24 7-8" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;

        /** @Proxy @type { BidOffersComponent } */
        bidOfferProxy;

		template = `
            <st-element 
                component="BidOffersComponent"
                proxy="BidOffersComponent"
            >
            </st-element>
            <st-element component="BiddersList"></st-element>
		`;

        closeCurrentBid(){
            /** This proxy represents BidOffersComponent component */
            this.bidOfferProxy.offerAmmount.onChange((value) => {
                console.log(`Theres is a new offer of ${value}`);
            });
        }

	}
	```

=== "BidOffersComponent.js"
	```js title="This child component has a proxy in the parent" hl_lines="18-20 7 11" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

        offerAmmount = 0;

		template = `
            <button (click)="increase()">Increase my offer</button>
			I'm willing to offer @offerAmmount.
		`;

        /* Child component updates itself, but parent classe 
         * can also call this method thereby beng able to update
         * the child value 
         * */
        increase(){
            this.offerAmmount = this.offerAmmount.value + 5;
        }

	}
	```

=== "BiddersList.js"
	```js title="" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddersList extends ViewComponent {

		isPublic = true;
		template = `
			Here goes the list of bidders.
		`;

	}

	```
!!! note "Proxy approach consideration"
    For Parent component can Subscribe to its childrens State through 2 means, the `@Proxy` way, and/or the component reference (`ref`) way.

    For using a proxy, the parent component needs to create a property annotated with both `@Proxy` and `@type` annotation, and `@Proxy`  comes first, the type will be the component class which the Proxy represents.

    Parent can access anything which is public from the Proxy property as shown in line 21 of previous example, hterefore, to subscribe to a State of the child, we only need to specify `.onChange()` event which recieves a closure/function, this closure recieves the new values as first parameter.

    A component can subscribe to change to itself, therefore this is automatically done when the State is bound to the template, in addition to that, it can also be done through the `.onChange()` method, and this is done by using <a href="#">Hooks</a>.


<br>

### 2. Adjacent (sibling) components communication (Pub/Sub)

State Subscription is a way for one Component to listen to another component State changes by subcribing to it. follow the example:

=== "BiddingDisplay.js"
	```js title="This is the parent component" hl_lines="8-12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddingDisplay extends ViewComponent {

		isPublic = true;

		template = `
            <st-element 
                component="BidOffersComponent"
                ref="BidOffersDisplayRef"
            >
            </st-element>
            <st-element component="BiddersList"></st-element>
		`;

	}
	```

=== "BidOffersComponent.js"
	```js title="This child component has a ref stated in the parent" hl_lines="15-17" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BidOffersComponent extends ViewComponent {

		isPublic = true;

		template = `
            <button (click)="increase()">Increase my offer</button>
			I'm willing to offer @offerAmmount.
		`;

        /* Child component updates itself, but parent and sibling classe can 
         * also call this method thereby beng able to update the child value 
         * */
        onNewBiderEntering(){
            console.log(`New bidder enter to the list and his bid is 0 for now`);
        }

	}
	```

=== "BiddersList.js"
	```js title="This child component access his sibling through the reference" linenums="1" hl_lines="7-8 12 20 25-27 31-34"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class BiddersList extends ViewComponent {

		isPublic = true;

        /** @type { BidOffersComponent } */
        bidOfferInstance;

		template = `
			Here goes the list of bidders.
            <button (click)="addBidder()">Admit new Bidder</button>
		`;

        constructor(){
            super();

            /** we need to assign this to a variable as it this keyword
             *  won't be available as such inside the whenReady Hook */
            const obj = this;

            /** whenReady() is a Hook which detects when the 
             * sibling component is available 
             * */
            this.whenReady(() => {
		        obj.bidOfferInstance = Components.ref('BidOffersDisplayRef');
            });

        }

        addBidder(){
            /** Calling the method from sibling component */
            this.bidOfferInstance.onNewBiderEntering();
        }

	}

	```

!!! note "Reference (ref) approach consideration"
    Jast like the `@Proxy`, reference (`ref`) way needs to be defined in the tag itself, which then makes it available to be accessed through the Components.ref() method as we can see in the second sibling ( BiddersList ).

    Proxies and references are alike except for the scope they are accessed, as Proxy only father can acces it (<a href="#proxy-example">see proxy example</a>), and the reference can be access by any component as long as it's sibling or active in the same moment, therefore, Parent component can access child through reference the same way the sibling does.