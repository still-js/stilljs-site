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


```js title="HomeWithEvent.js" hl_lines="13-14 18-20 22-24" linenums="1"
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