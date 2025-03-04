StillJS is a modern frontend framework that enables developers to write and reuse Vanilla JavaScript while providing a modular and component-based architecture similar to React, Angular, and VueJS. It offers a lightweight yet powerful approach to structuring applications, allowing for better maintainability and scalability without introducing a complex abstraction layer. With StillJS, you get the flexibility of raw JavaScript while benefiting from an organized and efficient development workflow. 🚀
<br><br>

### Basic component sample


```js title="HomeComponent.js" linenums="1"
import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

export class HomeComponent extends ViewComponent {

    isPublic = true;
    template = `
        <h1>
            Put here your template code
        </h1>
    `;

    constructor() {
        super();
    }

}
```




