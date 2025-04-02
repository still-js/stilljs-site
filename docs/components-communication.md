!!! info "Work in Progress"

    Thee is yet a work in progress in this documentation, it means that some addiotnal content, scenarios and example are yet to be brought, nevertheless the current content cover from the basics to more elaborated scenarios.


!!! failure "<u>ViewComponent</u> and <u>BaseService</u> import in <a href="../installation-and-running-cdn/">CDN/Lone component mode</a>"

    The import (e.g. `import { ViewComponent } from "@still/component/super/ViewComponent.js"`) of <b>ViewComponent</b> and <b>BaseService</b> classes is inexistent <a href="../installation-and-running-cdn/">CDN mode setup</a>, as this is already provided by CDN itself.

<br/>

### Overview

In order to provide ways from components to communicate to each other, Still.js provade with different options thereby covering all scenarios such as Parent to child, Sibling to Sibling, any component to any other(s), follow the documentation.

<a name="proxy-example"></a>

### 1. Parent to child change Subscription using Proxy (Pub/Sub)

State Subscription is a way for one Component to listen to another component State changes by subcribing to it. The <b>`route.map.js`</b> file contains the mapping on where every component resides. follow the example:

=== "BiddingDisplay.js"
	```js title="This is the parent component" hl_lines="8-9 12-16 24-29" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { BidOffersComponent } from "./BidOffersComponent.js";

    export class BiddingDisplay extends ViewComponent {

        isPublic = true;

        /** @Proxy @type { BidOffersComponent } */
        bidOfferProxy; //This is assignet in the proxy prop of the <st-element> line 14

        template = `
            <st-element 
                component="BidOffersComponent"
                proxy="bidOfferProxy"
            >
            </st-element>
            <st-element component="BiddersList"></st-element>
        `;

        /** Component Hook which takes place when it's completly render and startder */
        stAfterInit() {
            /** This is needed so parent component only try to subscribe to state 
             * after child is completly loaded */
            this.bidOfferProxy.on('load', () => {
                // This proxy represents BidOffersComponent component
                this.bidOfferProxy.offerAmmount.onChange((value) => {
                    console.log(`Theres is a new offer of ${value}`);
                });
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
            <p>Here goes the list of bidders.</p>
        `;

    }

	```

=== "route.map.js"
	```js title="" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                BiddingDisplay: {
                    path: "app/components/communication",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/communication",
                    url: "/bid/offer"
                },
                BiddersList: {
                    path: "app/components/communication",
                    url: "/bid/bidder"
                }
            },
            lazyInitial: {}
        }
    }
	```

=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |___@still
    |___app
    |    |
    |    |__components
    |    |   |__bidding
    |    |   |   |__BiddingDisplay.js
    |    |   |   |__BidOffersComponent.js
    |    |   |   |__BiddersList.js
    |    |   |   |
    |__app-setup.js
    |__ ...

	```

!!! note "Proxy approach consideration"
    Parent component can Subscribe to its childrens State through 2 means, the <b>`@Proxy`</b> way, and/or the reference (<b>`ref`</b>) way.

    - For using a proxy, the Parent component needs to create a property annotated with both <b>`@Proxy`</b> and <b>`@type`</b> annotation, and <b>`@Proxy`</b> comes first, the type will be the component class which the Proxy represents.

    - Proxy readiness is needed to subscribe to its state, in this case subscription happens when child component is fully ready, hence we're doing <b>`this.bidOfferProxy.on('load', callBackFunction)`</b> which is placed in the <a href="#"><b>stAfterInit()</b></a> Hook, and my <b>callBackFunction</b> is where I implement the state subscription itself.

    - Parent can access anything which is public from the Proxy property as shown in line 25, therefore, to subscribe to a State of the child, we only need to specify <b>`.onChange()`</b> that which recieves a closure/function, this closure recieves the new values as first parameter.

    - A component can subscribe to change to itself, therefore this is automatically done when the State is bound to the template, in addition to that, it can also be done through the <b>`.onChange()`</b> method, and this is done by using the <a href="#">stAfterInit()</a> <a href="#">Hook</a> as well.


<br>

<a name="reference-example"></a>

### 2. Adjacent (sibling) components reactive communication using Reference (Pub/Sub)

State Subscription is a way for one Component to listen to another component State changes by subcribing to it. The <b>`route.map.js`</b> file contains the mapping on where every component resides, follow the example:

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
	```js title="This child component has a ref stated in the parent" hl_lines="15-17 6 9" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

    export class BidOffersComponent extends ViewComponent {

        isPublic = true;
        totalBidders = 0;

        template = `
            Total bidders now is @totalBidders.
        `;

        /* Child component updates itself, but parent and sibling classe can 
        * also call this method thereby beng able to update the child value 
        * */
        onNewBiderEntering() {
            console.log(`New bidder enter to the list and his bid is 0 for now`);
        }

    }
	```

=== "BiddersList.js"
	```js title="This child component access his sibling through the reference" linenums="1" hl_lines="8-9 13 20-23 27-34"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
	import { BidOffersComponent } from "./BidOffersComponent.js";

    export class BiddersList extends ViewComponent {

        isPublic = true;

        /** @Prop @type { BidOffersComponent } */
        bidOfferInstance;

        template = `
            Here goes the list of bidders.
            <button (click)="addBidder()">Admit new Bidder</button>
        `;

        constructor() {
            super(); //Supper is needed to be called according to JavaScript standards

            // stWhenReady() Hook detects when the sibling component is available
            this.stWhenReady(() => {
                // Assigning the sibling instance to the property
                this.bidOfferInstance = Components.getFromRef('BidOffersDisplayRef');
            });

        }

        addBidder() {
            // Call sibling component method
            this.bidOfferInstance.onNewBiderEntering();

            // Updating the sibling component State through the reference
            const prevTotalBidders = this.bidOfferInstance.totalBidders.value;
            this.bidOfferInstance.totalBidders = prevTotalBidders + 1;
        }

    }

	```

=== "route.map.js"
	```js title="" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                BiddingDisplay: {
                    path: "app/components/communication",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/communication",
                    url: "/bid/offer"
                },
                BiddersList: {
                    path: "app/components/communication",
                    url: "/bid/bidder"
                }
            },
            lazyInitial: {}
        }
    }
	```


=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |___@still
    |___app
    |    |
    |    |__components
    |    |   |__bidding
    |    |   |   |__BiddingDisplay.js
    |    |   |   |__BidOffersComponent.js
    |    |   |   |__BiddersList.js
    |    |   |   |
    |__app-setup.js
    |__ ...

	```

!!! note "Reference (ref) approach consideration"
    - Just like the `@Proxy`, reference (`ref`) way needs to be defined in the tag itself, which then makes it available to be accessed through the Components.ref() method as we can see in the second sibling ( BiddersList ).

    - Proxies and references are alike except for the scope they can be accessed, as Proxy only the Father can acces it (<a href="#proxy-example">see proxy example</a>), and the reference can be access by any component as long as it's sibling or active in the same moment, therefore, Parent component can access child through reference the same way the sibling does.


<br>

<a name="service-example"></a>

### 3. Global state management Reactively - Components communication with Service

Services is another way of providing component communication capabilities, in this case, the service is not tied to any component, which means that state will remain even if some component was unloaded. The <b>`route.map.js`</b> file contains the mapping on where every component resides, follow the code example:

=== "BiddingDisplay.js"
	```js title="This is the parent component" hl_lines="2 10-12 27-32" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { BiddingService } from "../../service/BiddingService.js";

    export class BiddingDisplay extends ViewComponent {

        isPublic = true;

        /** Service declaration, will get injected automatically from the service
         *  path defined in the application level (StillAppSetup) in app-setup.js (last tab)
         * @Inject
         * @type { BiddingService } */
        bService;


        template = `
            <st-element component="BiddersList"></st-element>
            <st-element 
                component="BidOffersComponent"
            >
            </st-element>
        `;

        /** Component Hook which takes place when it's completly render and startder */
        stAfterInit() {
            /** This is needed so parent component only try to subscribe to state 
             * after child is completly loaded */
            this.bService.on('load', () => { //Check service readiness
                //Bellow, it Subscribe to ServiceEvent variable (countryStore)
                this.bService.countryStore.onChange(newValue => {
                    console.warn(`New country entered the Bid, follow the list: `, newValue);
                });
            });

        }

    }
	```

=== "BidOffersComponent.js"
	```js title="This child component has a ref stated in the parent" hl_lines="2 8-9 13 18 22 25" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { BiddingService } from "../../service/BiddingService.js";

    export class BidOffersComponent extends ViewComponent {

        isPublic = true;

        /** @Inject @type { BiddingService } */
        bService;

        template = `
            <p>
                <button (click)="exitTheBid()">Exit the bidding</button>
            </p>
        `;

        exitTheBid() {
            let countryStore = this.bService.countryStore.value;
            const myCountry = 'Australia';

            // Filter out every country but Australia
            countryStore = countryStore.filter(country => country != myCountry);

            // Update the store with Australia removed from the list
            this.bService.countryStore = countryStore;
        }

    }
	```

=== "BiddersList.js"
	```js title="This child component access his sibling through the reference" linenums="1" hl_lines="9-11 24 30-31 34"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { BiddingService } from '../../service/BiddingService.js';

    export class BiddersList extends ViewComponent {

        isPublic = true;

        /** 
         * @Inject
         * @type { BiddingService } */
        bService;

        /** Not a state but a prop, hence the annotation
         * @Prop */
        countriesList = ['Bulgaria', 'Canada', 'Denmark', 'Ethiop', 'France', 'Ghana']

        template = `
            <p>Here goes the list of bidders.</p>
            <button (click)="addMoreCountry()">Adde new country</button>
        `;

        addMoreCountry() {
            /** Retrieve and log the current/initial state */
            const countryState = this.bService.countryStore.value;
            console.log(`----> Country Store before updating: `, countryState);

            /** Get the next country from the  */
            const newCountry = this.countriesList[countryState.length - 1];
            /** Updating the store and re-assigning it to the service */
            countryState.push(newCountry);
            this.bService.countryStore = countryState;

            /** Retrieve and log the state after update from store */
            const updatedCountryState = this.bService.countryStore.value;
            console.log(`----> Country Store after updating: `, updatedCountryState);
        }
    }

	```

=== "BiddingService.js"
	```js title="Service Path is defined in StillAppSetup class" linenums="1" hl_lines="9-11 24 30-31 34"
    import { BaseService, ServiceEvent } from "../../@still/component/super/service/BaseService.js";

    export class BiddingService extends BaseService {

        /** An array with a single country is being assigner */
        countryStore = new ServiceEvent(['Australia']);

    }

	```

=== "app-setup.js"
	```js title="Definition of the service folder" linenums="1" hl_lines="11"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { HomeComponent } from "./app/home/HomeComponent.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            this.setHomeComponent(HomeComponent);
            //service is the name of the folder where services will be placed
            this.setServicePath('service/')
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
                    path: "app/components/communication",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/communication",
                    url: "/bid/offer"
                },
                BiddersList: {
                    path: "app/components/communication",
                    url: "/bid/bidder"
                }
            },
            lazyInitial: {}
        }
    }
	```


=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |___@still
    |___app
    |    |
    |    |__components
    |    |   |__bidding
    |    |   |   |__BiddingDisplay.js
    |    |   |   |__BidOffersComponent.js
    |    |   |   |__BiddersList
    |    |   |   |
    |    |__service
    |    |   |__BiddingService.js
    |    |   |
    |__app-setup.js
    |__ ...

	```

!!! note "Still.js Service considerations"
    - Services are singleton and for them to be injected we use the <b>`@Inject`</b> annotation which can also be combined with <b>`@ServicePath`</b> annotation allowing for specification of the service file path, also, it's required to define the injection <b>`@type`</b> just like we do for a <a href="#proxy-example">Proxy</a>.

    - Just the same as <b>`@Proxy`</b>, Service need to be ready to be used, then again we call the the <b>serviceName.on('load', callBackFunc)</b>, where <b>serviceName</b> is the variable name annotated with <b>`@Inject`</b>.
    
    - The concept behind the service is that it can be composed by different type of features such as store/ServiceEvent, regular state and methods (e.g. to implement API call or complex logic implementation), for this example only ServiceEvent/Store is being used.

    - ServiceEvent variable in the Service are the ones which allow for reactive behavior through the means os subscription the same way it happens with component state.

<br>

#### 3.1. Defining Service path using @ServicePath annotation

For the sake of peculiar kind of organization of project structure, Still.js provides with @ServicePath annotation which allow for specification of the folder path in which the injecting service is located. The <b>`route.map.js`</b> file contains the mapping on where every component resides:

=== "BiddingDisplay.js"
	```js title="This is the parent component which subscribe to the service store" hl_lines="10-13 22-27" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { CustomersService } from "../../service/api/CustomersService.js";

    export class BiddingDisplay extends ViewComponent {

        isPublic = true;

        /** Service declaration, will get injected automatically due to Inject anottation
         *  from the specified ServicePath path due to the annotation
         * @Inject
         * @ServicePath service/api/
         * @type { CustomersService } */
        custService;

        template = `
            <st-element component="BiddersList"></st-element>
        `;

        /** Component Hook which takes place when it's completly render and startder */
        stAfterInit() {

            this.custService.on('load', () => { //Check service readiness
                //Bellow, it Subscribes to ServiceEvent variable (totalCustomers)
                this.custService.totalCustomers.onChange(newValue => {
                    console.log(`Total customer was updated to: `, newValue);
                });
            });
            
        }

    }
	```

=== "BiddersList.js"
	```js title="This is the parent component which subscribe to the service store" hl_lines="2 10-13 17 21 23" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";
    import { CustomersService } from '../../service/api/CustomersService.js'

    export class BiddersList extends ViewComponent {

        isPublic = true;

        /** Parameter after sertice path is infact the folder
         *  where it's (CustomersService.js) placed
         * @Inject
         * @ServicePath service/api/
         * @type { CustomersService } */
        customerService;

        template = `
            <p>Here goes the list of bidders.</p>
            <button (click)="updateTotalCustomer()">Up customers</button>
        `;

        updateTotalCustomer() {
            const currentValue = this.customerService.totalCustomers.value;
            /** Update the value of the of the Store variable in the service */
            this.customerService.totalCustomers = currentValue + 10;
        }
    }
	```

=== "CustomersService.js"
	```js title="This is the parent component which subscribe to the service store" hl_lines="4" linenums="1"
    import { BaseService, ServiceEvent } from '../../../@still/component/super/service/BaseService.js';
    export class CustomersService extends BaseService {

        totalCustomers = new ServiceEvent(0);

    }
	```


=== "route.map.js"
	```js title="" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                BiddingDisplay: {
                    path: "app/components/communication",
                    url: "/bid/display"
                },
                BidOffersComponent: {
                    path: "app/components/communication",
                    url: "/bid/offer"
                },
                BiddersList: {
                    path: "app/components/communication",
                    url: "/bid/bidder"
                }
            },
            lazyInitial: {}
        }
    }
	```


=== ":octicons-project-roadmap-16: Project folder structure"
	```js title="Project folder structure"
    project-root-folder
    |___@still
    |___app
    |    |
    |    |__components
    |    |   |__bidding
    |    |   |   |__BiddingDisplay.js
    |    |   |   |__BiddersList.js
    |    |   |   |
    |    |__service
    |    |   |__api
    |    |   |   |__CustomersService.js
    |    |   |   |
    |__app-setup.js
    |__ ...

	```

<br/>
In addition the the different component intecommunication approached in thispage, Still.js also provide Parent to Child communication approach which allowpassing properties and methods from parent to child as explained in the <a href="../components/#st-element-parent-child-communication">Component to Component communication</a>.
<br/>
<br/>
<br/>