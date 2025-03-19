###  Basic component sample

All components extends from ViewComponent, and whenever gets rendered in the UI/browser can be assigned to the template variable as depicted below in lines 11 to 19.

```js title="HomeComponent.js" hl_lines="6-14" linenums="1"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

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

    constructor() {
        super();
    }

}
```
Run result:
<iframe src="https://nbernardo.github.io/stilljs/" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

<br>

###  Event handling

For event handling, we can create a method inside the component class, then we just need to bind it to any html element by assigning it to the (click) notation/directive as follow and highlighet in lines 12 and 16 to 18:

```js title="HomeWithEvent.js" hl_lines="16-18 12" linenums="1"
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

	constructor() {
		super();
	}

}
```
Run result:
<iframe src="https://nbernardo.github.io/stilljs/#/HomeWithEvent" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

<br>

###  State binding and reactive behavior

All dev defined variable are considered state which is managed by the components instance itself, when it comes to use it, any component calling it can use and listen to it. State binding can be achieved by using @stateVariableName inside the place where it's to be bound.

Access to the state value is done by calling `.value` property, assigning a value is is done straight to the property itself.


```js title="CounterComponent.js" hl_lines="13-14 18-20 22-24" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class CounterComponent extends ViewComponent {

	isPublic = true;
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

	constructor() {
		super();
	}


}
```
Run result:
<iframe src="https://nbernardo.github.io/stilljs/#/CounterComponent" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>


<br>

###  Two-way data binding and Forms

When building a form, in several situations Two-way data binding is needed, the (value) notation/directive is provided in which we only need to assign the state in which we are binding out form input, also input needs to be wrapped by a form (&lt;form&gt;&lt;/form&gt;).


```js title="BasicForm.js" hl_lines="14 20-22" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class BasicForm extends ViewComponent {

	isPublic = true;
	firstName = '';
	dateOfBirth;

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
					(value)="dateOfBirth" 
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

	constructor() {
		super();
	}

}
```
Run result:
<iframe src="https://nbernardo.github.io/stilljs/#/BasicForm" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

!!! note "Input/Form grouping Important consideration"

    Still.js adopts the Bootstrap approach when it comes to form group, though it's not needed, this is quite helpfull to organizing form component by adding it (Bootstrap) as part of the project, also it helps properly handle alignment/positioning like labels and validation messages.



<br>

###  Conditional rendering and Conditional Hide/Unhide

By creating a variable annotated with @Prop (using JSDoc approach) we can then use this as flags (or any other application flow value) thereby being possible to assigne it on the Still.js directive, in this case to render or not, or hide/unhide (renderIf) and (showIf) notations are provided.

```js title="BasicForm.js" hl_lines="7-8 10-11 18 24" linenums="1"
import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

export class BasicConditionalView extends ViewComponent {

	isPublic = true;

	/** @Prop */
	isAdminPermisison = false;

	/** @Prop */
	shouldShowContent = true;

	addLabel = 'Hide';
	adminLabel = 'Unable';

	template = `
        <div>
            <div (renderIf)="self.isAdminPermisison">
				Hello, this part of the content wond be rendere since
				<br/>the flag on (renderIf) is false, even if you click
				<br/>in the Render button which turns flag to true
			</div>

            <p (showIf)="self.shouldShowContent">
            If you click the button bellow this content will be hidden
			<br>in case flag is true, and hide if false
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

	constructor() {
		super();
	}

}
```
Run result:
<iframe src="https://nbernardo.github.io/stilljs/#/rendering-showing/basic-conditional-view" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>