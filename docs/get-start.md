###  Basic component sample

All components extends from ViewComponent, and whenever gets rendered in the UI/browser can be assigned to the template variable as depicted below in lines 11 to 19.

=== "HomeComponent.js"

```js title="This component is placed under the app/home/ path" hl_lines="11-18" linenums="1"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

	/** 
	 * isPublic flag is needed for any component that is publicly accessible, therefore, 
	 * when dealing with authentication and permission scenario any component requiring
	 * user permission the flag will be removed or turned to false
	 */
    isPublic = true;
    template = `
        <div>
            <h2>Hello world!</h2>
            <p>
            I'm an easy component with a button
            </p>
            <button>I'm a button</button>
        </div>
    `;

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>


<br>

<a name="template-splitting"></a>
###  Splitting Template (`.html`) from `.js` file

As long as both template/.html and .js files are in the same folder and have the are named similarly, we just need to remove the variable template from .js and it will be able to refer to the .html file instead. Tamplete splitting from .js file is quite usefull for complex template coding also making it more manageable and organized.

=== "SlittedComponent.js"
	```js title="This component is placed under the app/components/splitting/ path" hl_lines="16-18 12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class SlittedComponent extends ViewComponent {
		isPublic = true;
	}
	```

=== "SlittedComponent.html"
	```html title="Teamplate file stays in the same folder as the component" linenums="1"
	<div>
		<h3>
			This is the header for the splitted template file
		</h3>
		<br/>
		<hr/>
		<br/>
		<p>
			Template splitted from the .js file is quite usefull especially on 
			those situations that the template content is quite extensive, 
			normally template inside the .js file can be natually used for smaller 
			template cases.
		</p>
	</div>
	```
	
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/bas/slitted" 
            frameBorder="0"
            style="border: 1px solid grey; 
				   border-radius:4px;
				   width: 100%; 
				   padding: 5px; background: white"
            >
</iframe>



<br>

###  Event handling

For event handling, we can create a method inside the component class, then we just need to bind it to any html element by assigning it to the (click) notation/directive as follow and highlighet in lines 12 and 16 to 18:

=== "HomeWithEvent.js"
```js title="This component is placed under the app/components/event/ path" hl_lines="16-18 12" linenums="1"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeWithEvent extends ViewComponent {

	isPublic = true;
	template = `
        <div>
            <h2>Hello world from HomeWithEvent!</h2>
            <p>
            I'm an easy component with a button
            </p>
            <button (click)="callMe()">I'm a button</button>
        </div>
    `;

	callMe() {
		alert(`Hi, you clicked me, I'm a button`);
	}

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/HomeWithEvent" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

<br>

###  State binding and reactive behavior

All dev defined variable are considered state which is managed by the components instance itself, when it comes to use it, any component calling it can use and listen to it. State binding can be achieved by using @stateVariableName inside the place where it's to be bound.

Access to the state value is done by calling `.value` property, assigning a value is is done straight to the property itself.

=== "CounterComponent.js"
```js title="This component is placed under the app/components/counter/ path" hl_lines="16-17 21-23 25-27 9" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class CounterComponent extends ViewComponent {

	isPublic = true;
	/**
	 * This is a state since no annotation or signature is put for it
	 */
	count = 0;

	template = `
	<div>
		<p>
			My counter state is @count
		</p>
		<button (click)="increment()">Increment (@count)</button>
		<button (click)="decrement()">Decrement (@count)</button>
	</div>
	`;

	increment() {
		this.count = this.count.value + 1;
	}

	decrement() {
		this.count = this.count.value - 1;
	}

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/CounterComponent" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>


<br>

###  Two-way data binding and Forms

When building a form, in several situations Two-way data binding is needed, the (value) notation/directive is provided in which we only need to assign the state in which we are binding out form input, also input needs to be wrapped by a form (&lt;form&gt;&lt;/form&gt;).

=== "BasicForm.js"
```js title="This component is placed under the app/components/form/ path" hl_lines="14 20-22" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class BasicForm extends ViewComponent {

	isPublic = true;
	firstName = '';
	shoeSize;

	template = `
	<div>
		<form>
			<div class="form-group">
				<label>First Name</label>
				<input (value)="firstName" type="text"  placeholder="Enter first name">
			</div>
			<br/>
			<div class="form-group">
				<label>Shoe Size</label>
				<input 
					(value)="shoeSize" 
					(validator)="number" 
					(validator-warn)="Invalid shoe size, number is required"
					placeholder="Enter valid shoe size"
				>
			</div>
		</form>
		<br/>
		<p>Welcome <b>@firstName</b></p>
		<br/>
		<button (click)="setFirstName('Michael')">Set Michael</button>
		<button (click)="setFirstName('Dario')">Set Dario</button>
	</div>
	`;

	/** Single line method using arrow function */
	setFirstName = (val) => this.firstName = val;

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/BasicForm" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

!!! note "Input/Form grouping Important consideration"

    Still.js adopts the Bootstrap approach when it comes to form group, though it's not needed, this is quite helpfull to organizing form component by adding it (Bootstrap) as part of the project, also it helps properly handle alignment/positioning like labels and validation messages.



<br>

<a name="render-if-ex1"></a>
###  Conditional rendering and Conditional Hide/Unhide

By creating a variable annotated with @Prop (using JSDoc approach) we can then use this as flags (or any other application flow value) thereby being possible to assigne it on the Still.js directive, in this case to render or not, or hide/unhide (renderIf) and (showIf) notations are provided respectively.

=== "BasicConditionalView.js"
```js title="This component is placed under the app/components/conditoinal-render/ path" hl_lines="11-13 16 23 29" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class BasicConditionalView extends ViewComponent {

	isPublic = true;

	/**
	 * The props differ from state (which does not have any annotation)
	 * in a way that state allow to trace changes which is also useful
	 * in the component to component communication scenario in real time/reactively
	 * @Prop 
	 */
	isAdminPermisison = false;

	//Annotation can be put in the same line of the prop/variable
	/** @Prop */ shouldShowContent = true;

	addLabel = 'Hide';
	adminLabel = 'Unable';

	template = `
        <div>
            <div (renderIf)="self.isAdminPermisison">
				Hello, this part of the content wont be rendered since
				the flag on (renderIf) is false, even if you click
				in the second button which turns flag to true
			</div>

            <p (showIf)="self.shouldShowContent">
            If you click the button bellow this content will be unhide
			<br>in case flag is true, and hidden if false
            </p>
            <button (click)="hideOrUnhide()">@addLabel content</button>
            <button (click)="renderContent()">@adminLabel Admin</button>
        </div>
    `;

	hideOrUnhide() {
		this.addLabel = 'Hide';
		this.shouldShowContent = !this.shouldShowContent;
		if (!this.shouldShowContent) this.addLabel = 'Unhide';
	}

	renderContent() {
		this.adminLabel = 'Unable';
		this.isAdminPermisison = !this.isAdminPermisison;
		if (this.isAdminPermisison) this.adminLabel = 'Able';
	}

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/BasicConditionalView" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>



<br>

###  Adding CSS Styles

Everything is base in Vanilla web technologies, therefore we can just write CSS naturally by creating the <style></style> scope, but it it also allows inline CSS if needed just like normall HTML with css in it.

=== "FormatedDataTable.js"
```js title="This component is placed under the app/components/styled/ path" hl_lines="9-13 14 16 18-22 24 26-29" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class FormatedDataTable extends ViewComponent {

	isPublic = true;
	template = `
	
		<style>
			ol {
				display: table;
				width: 98%;
				border: 1px solid black;
			}
			li, ol::before { display: table-row }

			ol::before { content: "" }

			li span {
				display: table-cell;
				border: 1px solid black;
				padding: 8px;
			}
			
			li:nth-child(odd) { background: lightgrey; }

			li:first-child {
				font-weight: bold;
				background-color: grey;
			}
			
		</style>
    	<h2>Ordered List Styled as a Table</h2>

		<ol>
			<li>
				<span>#</span>
				<span>Item</span>
			</li>
			<li>
				<span>1</span>
				<span>Apple</span>
			</li>
			<li>
				<span>2</span>
				<span>Banana</span>
			</li>
			<li>
				<span>3</span>
				<span>Grapes</span>
			</li>
			<li>
				<span>4</span>
				<span>Orange</span>
			</li>
			<li>
				<span>5</span>
				<span>Mango</span>
			</li>
		</ol>
	`;

}
```
Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/stylin/formated-data-table" 
            frameBorder="0"
            style="
				border: 1px solid grey; 
				border-radius:4px; 
				width: 50%;
				height: 200px;
				padding: 5px; background: white"
            >
</iframe>



<br>

###  Basics of Component Embeding

Bringing a component inside another in general is achievable by using the `<st-element></st-element>` tag where we can then specify the component name we want to embed as child (tag property as line 16), additional child component property (e.g. lines 18 and 19) and event handlers also can be passed the same way (in the tag) as long as they child difined it.

=== "Parent Component"
	```js title="UserForm.js - This component is placed under the app/components/embed/ path" hl_lines="8-9 12 15-21 28-30" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class UserForm extends ViewComponent {

		isPublic = true;

		/** @Prop */
		childTitleState = 'Child Title from Parent';
		changeCounter = 0;

		template = `
			<button (click)="updateChildTitle()">Change child title</button>
			<br/>
			<br/>
			<st-element 
				component="UserGrid"
				ref="insideFormGridReference"
				tableTitle="self.childTitleState"
				titleMergeSize="5"
				>
			</st-element>
		`;

		updateChildTitle() {

			this.changeCounter = this.changeCounter.value + 1;

			/** @type { UserGrid } */
			const userGridObj = Components.getFromRef('insideFormGridReference');
			userGridObj.tableTitle = 'Title altered ' + this.changeCounter.value + 'x';
		}

	}
	```

=== "Child Component"
	```js title="UserGrid.js - This component is placed under the app/components/embed/ path" hl_lines="7-9 14" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class UserGrid extends ViewComponent {

		isPublic = true;

		tableTitle = "Users List Not changed";
		/** @Prop */
		titleMergeSize;

		template = `
			<table border="1">
				<thead>
					<tr><th colspan="@titleMergeSize">@tableTitle</td></tr>
					<tr>
						<th>ID</th>
						<th>Name</th>
						<th>Email</th>
						<th>Age</th>
						<th>Country</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>1</td>
						<td>John Doe</td>
						<td>john@example.com</td>
						<td>28</td>
						<td>USA</td>
					</tr>
					<tr>
						<td>2</td>
						<td>Jane Smith</td>
						<td>jane@example.com</td>
						<td>32</td>
						<td>UK</td>
					</tr>
				</tbody>
			</table>

		`;
	}
	```

Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/user/user-form" 
            frameBorder="0"
            style="
				border: 1px solid grey; 
				border-radius:4px; 
				width: 100%;
				height: 200px;
				padding: 5px; background: white"
            >
</iframe>


<br>

###  Basics of Navigation

Whe using still-cli (`@stilljs/cli` - which is the recommended way) to generate the component, both route name (same as component name) and component URL will be added automatically in the `route.map.js` file in the project root folder, therefore, navigation can be done the way it workes in regular web pages. in the bellow code navigation is done by using route name. 

=== "First Component"
	```js title="EntryMenu.js - This component is placed under the app/components/menu/ path" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class EntryMenu extends ViewComponent {

		isPublic = true;
		template = `
			<div>
				This is Entry menu component, press the bellow 
				<br/>button or in the link to navigate to User
				<br/>
				<br/>
				<button (click)="goto('UserRegistration')">Register user</button>
			</div>
		`;

	}
	```

=== "Second Component"
	```js title="UserRegistration.js - This component is placed under the app/components/user/ path" hl_lines="12" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class UserRegistration extends ViewComponent {

		isPublic = true;
		template = `
			<div class="user-reg-container">
				<span class="smile-icone">&#9787;</span> 
				<br/>
				This is the user registration component
				<br/>
				<button (click)="goto('EntryMenu')">Go to Menu</button>
			</div>

			<style>
				.user-reg-container { text-align: center; }
				.smile-icone { 
					color: orange;
					font-size: 60px;
				}
			</style>
		`;

	}
	```

=== "Routing file"
	```js title="route.map.js - This is a framework core file whichs stays in the project root dir" hl_lines="4 5" linenums="1"
	export const stillRoutesMap = {
		viewRoutes: {
			regular: {
				EntryMenu: { path: "app/components/routing" },
				UserRegistration: { path: "app/components/routing" }
			},
			lazyInitial: {}
		}
	}

	```

Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/routin/entry-menu" 
            frameBorder="0"
            style="
				border: 1px solid grey; 
				border-radius:4px; 
				width: 50%;
				height: 200px;
				padding: 5px; background: white"
            >
</iframe>



<br>

###  DOM Manipulation

Because Still.js is 100% pure/Vanilla JavaScript, DOM manipulation can be done straight as the native/regular DOM API, no workaround or additional layer/special coding is needed. 

=== "EntryMenu.js"
```js title="This component is placed under the app/components/dom/ path" hl_lines="18 31-37 40-46 28" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class LoginComponent extends ViewComponent {

	isPublic = true;

	userName;
	password;

	template = `
		<form onsubmit="return false;">
			<div>Type the same for both user and password for <br>success login, something else for invalid<div>
			
			Username: <input type="text" (value)="userName">
			<br><br>
			Password: <input type="password" (value)="password"><br>
			
			<span id="loginStatus"></span><br>

			<button (click)="processLogin()">Login</button>
		</form>
	`;

	processLogin() {

		const user = this.userName.value;
		const password = this.password.value;
		const messageContainer = document.getElementById('loginStatus');

		if (user !== password || user == '' || password == '') {
			/** Assignin new content via DOM manipulation */
			messageContainer.innerHTML = 'Invalid user or password';
			/** CSS updating through DOM */
			messageContainer.style = 'color: red; background-color: #ab1f1f38;';
			/** Changing inputs border via DOM manipulation */
			document.querySelector('input[type=text]').style = 'border: 1px solid red';
			document.querySelector('input[type=password]').style = 'border: 1px solid red';

		} else {
			/** Assignin new content via DOM manipulation */
			messageContainer.innerHTML = 'User login success! &#9787;';
			/** CSS updating through DOM */
			messageContainer.style = 'color: green; background-color: none;';
			/** Changing inputs border via DOM manipulation */
			document.querySelector('input[type=text]').style = 'border: 1px solid green';
			document.querySelector('input[type=password]').style = 'border: 1px solid green';
		}
	}

}
```

Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/dom-manipulatio/login" 
            frameBorder="0"
            style="
				border: 1px solid grey; 
				border-radius:4px; 
				width: 50%;
				height: 200px;
				padding: 5px; background: white"
            >
</iframe>


<br>

###  Looping and Rendering from a List

Lopping a list and rendering its items is quite simple, Still.js provides the (forEach) notation/directive, which can be pass to a top level container which is then used to wrap the template for the desired output of each list item. 

=== "LoopingDirective.js"
	```js title="This component is placed under the app/components/looping/ path" hl_lines="7-12 18-23 35" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class LoopingDirective extends ViewComponent {

		isPublic = true;

		/** This is the list of products ( data source ) */
		productList = [
			{ name: 'Orange', sold: 3, stockAvail: 7, price: '0.75$' },
			{ name: 'Apple', sold: 1, stockAvail: 5, price: '0.88$' },
			{ name: 'Banana', sold: 10, stockAvail: 50, price: '1.03$' },
		]

		template = `
			<div>
				<h5>Looping with HTML child</h5>
				<br>
				<span (forEach)="productList">
					Stock Availability
					<div each="item">
						<b>Name:</b> {item.name} - <b>Sock:</b> {item.stockAvail} - <b>Price:</b> {item.price}
					</div>
				<span>
			</div>
			
			<br><hr><br/>

			<div>
				<h5>Looping with child Component</h5>
				<br>
				<span (forEach)="productList">
					Shipping Cart Checkout
					<!-- Fields are mapped one to one from data 
						source (productList) to the child component state -->
					<st-element component="ShoppingItem" each="item"></st-element>
				<span>
			</div>
		`;
	}
	```

=== "ShoppingItem.js"
	```js title="This component is placed under the app/components/looping/ path" hl_lines="7-13 17-19" linenums="1"
	import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

	export class ShoppingItem extends ViewComponent {

		isPublic = true;

		/**
		 * Bellow states (name, sold, price) are being mapped directly since those
		 * names coincides with each item in the Data source in the parent component
		 */
		name;
		sold;
		price;

		template = `
			<div class="shoping-item-card">
				<span>Produce Name: @name</span>
				<span>Quantity: @sold</span>
				<span>Price: @price</span>
			</div>

			<style>
				.shoping-item-card{ display: flex; }

				.shoping-item-card span:first-child { width: 30%; }
				
				.shoping-item-card span:last-child { border-right: none; }

				.shoping-item-card span {
					border-right: 1px solid black;
					padding: 2px 5px; width: 18%;
					text-align: center; display: block;
				}
			</style>
		`;
	}
	```

Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/data-u/looping-directive" 
            frameBorder="0"
            style="
				border: 1px solid grey; 
				border-radius:4px; 
				width: 100%;
				height: 275px;
				padding: 5px; background: white"
            >
</iframe>






<br/>
<br/>