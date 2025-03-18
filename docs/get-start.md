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

<iframe src="https://nbernardo.github.io/stilljs/" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

<br>

###  Event handling

For event handling, we can create a method inside the component class, then we just need to bind it to any html element by assigning it to the (click) notation/directive as follow and highlighet in lines 11 and 15 to 17:

```js title="HomeWithEvent.js" hl_lines="15-17 11" linenums="1"
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

<iframe src="https://nbernardo.github.io/stilljs/#/HomeWithEvent" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>