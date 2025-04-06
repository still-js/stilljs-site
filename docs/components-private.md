### Overview
For the sake of user permission aspect, Private components in Still.js help manage user authorization for navigation and rendering. If a component is not public (<b>`isPublic = false`</b> or unset), custom logic is required to control its visibility. Still.js allows blacklisting and whitelisting components based on custom requirements, overriding the <b>`isPublic`</b> flag regardless of its value (true or false).

<br>
<a name="making-component-private"></a>
### 1. Making component private

=== "NewAccountForm.js"

    ```js title="This is the entry point component which is set as Home in app-setup.js" linenums="1" hl_lines="5 10 12"
    import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

    export class NewAccountForm extends ViewComponent {
        // Bellow flag makes the component public
        isPublic = true;
        template = `
            <section>
                This is the UI for creating account<br>
                More Options<br><br>
                <a href="#" (click)="goto('SavingAccount')">List Saving accounts</a>
                |
                <a href="#" (click)="goto('CheckingAccount')">List Checking accounts</a>
            </section>
        `;
    }
    ```

=== "CheckingAccount.js"

    ```js title="This is a private component" linenums="1" hl_lines="5"
    import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

    export class CheckingAccount extends ViewComponent {
        // Since the flag is set to false the component is then private
        isPublic = false;
        template = `
            <div>
                Here will be the list of Checking accounts
            </div>
        `;

    }
    ```

=== "CheckingAccount.js"

    ```js title="This is a private component" linenums="1" hl_lines="5"
    import { ViewComponent } from "../../../@still/component/super/ViewComponent.js";

    export class SavingAccount extends ViewComponent {

        /** The isPublic flag is not set making it to default to private */

        template = `
            <div>
                The Saving accounts will be displayed here
            </div>
        `;
    }
    ```

=== "app-setup.js"
    ```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="11" linenums="1"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { NewAccountForm } from "./app/components/BankAccount/NewAccountForm.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            //Bellow the entry point component is being set
            this.setHomeComponent(NewAccountForm);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
    ```

=== "route.map.js"
    ```js title="Routes will be added and manage automatically from here when creating the component using still-cli" hl_lines="4 8 12" linenums="1"
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                SavingAccount: {
                    path: "app/components/BankAccount",
                    url: "/minha/url/like/rest"
                },
                CheckingAccount: {
                    path: "app/components/BankAccount",
                    url: "/bankaccoun/checking-account"
                },
                NewAccountForm: {
                    path: "app/components/BankAccount",
                    url: "/bankaccoun/new-account-form"
                },
            },
            lazyInitial: {}
        }
    }
    ```


=== ":octicons-project-roadmap-16: Project folder structure"
    ```js title="Project folder structure"
    project-root-folder
    |__ @still/
    |__ app/
    |    |
    |    |__ components/
    |    |   |__ BankAccount/
    |    |   |   |__ NewAccountForm.js
    |    |   |   |__ CheckingAccount.js
    |    |   |   |__ SavingAccount.js
    |    |   |   |
    |__ app-setup.js
    |__ route.map.js
    |__  ...

    ```

In the example above, the NewAccountForm component includes buttons to navigate to private components, causing an <b>`Unauthorized acces`</b> warning and not rendering the component. To allow navigation, two approaches can be used separately or in combination and they can be set through the <b>`StillAppSetup`</b> (<b>app-setup.js</b> file):

- ***setAuthN*** - For the Application context, when the AuthN is set to true (`this.setAuthN(true)`), it understands that navigation to/ embeding such component can happen at all levels, anyway, there might be some exception which cannot be addressed here.


- ***setWhiteList*** - It's possible to specify a list of components that should be whitelisted, by doing that, even if the component is private, it'll always be accessible.



<br/><br/>





<a name="authn-flag"></a>
#### 1.1 Allowing private component access through `authN` flag

The <b>`authN`</b> flag is configured at the application level in the <b>`StillAppSetup`</b> class (<b>`app-setup.js`</b>). It is set using <b>`.setAuthN(true)`</b> in the custom authentication logic to indicate that the user is authenticated, allowing access to all components, including private ones. Having the same sample project from <a href="#making-component-private">point 1</a> only edit the <b>`app-setup.js`</b> as follow:

=== "app-setup.js"
    ```js title="This is the where Application context aspects are setup. This file is in the root folder. " hl_lines="13" linenums="1"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { NewAccountForm } from "./app/components/BankAccount/NewAccountForm.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            //Bellow the entry point component is being set
            this.setHomeComponent(NewAccountForm);
            //This informs the application that user can access all component
            this.setAuthN(true);
        }

        async init() {
            return await AppTemplate.newApp();
        }
    }
    ```


<br><br>

<a name="whitelist-component"></a>
#### 1.2 Using `whiteList` to allow access to Private component

In addition to <b><a href="#authn-flag">`setAuthN`</a></b> flag approach, <b>`setWhiteList`</b> is another way to make a private component accessible, in this case we have to pass an array of all components that we want to make accessible although it's private. Having the same sample project from <a href="#making-component-private">point 1</a> only edit the <b>`app-setup.js`</b> as follow:

=== "app-setup.js"
    ```js title="This is the where Application con, follow the text aspects are setup. This file is in the root folder. " hl_lines="14 16" linenums="1"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { CheckingAccount } from "./app/components/BankAccount/CheckingAccount.js";
    import { NewAccountForm } from "./app/components/BankAccount/NewAccountForm.js";
    import { SavingAccount } from "./app/components/BankAccount/SavingAccount.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            //Bellow the entry point component is being set
            this.setHomeComponent(NewAccountForm);
            const whiteListComponents = [SavingAccount, CheckingAccount];
            //Make components whitelisted by passing it to setWhiteList App configuration
            this.setWhiteList(whiteListComponents);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
    ```

<a name="white-list-explain"><a>
!!! info "Whitelist behind the scenes"
    <b>`whiteList components`</b> can only be set once, means, if <b><a href="#whitelist-component">`setWhiteList()`</a></b> is call more than once, only the first call will take affect, therefore changing it the runtime does not work, nevertheless, multiples list can yet be set and combined with the appropriate application logic/flow, so alternative flows can take place.

<br>

<a name="whitelist-component"></a>
### 2 Using <b>`blackList`</b> to make a component private (not accessible)

The blacklist is used to restrict access to specific components or parts of the application, even for authenticated users. When combined with business logic, it ensures that components listed in the blacklist remain inaccessible—regardless of a successful <a href="#making-component-private"><b>`.setAuthN(true)`</b></a> call—preventing access via both navigation and embedding. Having the same sample project from <a href="#making-component-private">point 1</a> only edit the <b>`app-setup.js`</b> as follow:

=== "app-setup.js"
    ```js title="This is the where Application con, follow the text aspects are setup. This file is in the root folder. " hl_lines="14-17 20" linenums="1"
    import { StillAppMixin } from "./@still/component/super/AppMixin.js";
    import { Components } from "./@still/setup/components.js";
    import { AppTemplate } from "./app-template.js";
    import { CheckingAccount } from "./app/components/BankAccount/CheckingAccount.js";
    import { NewAccountForm } from "./app/components/BankAccount/NewAccountForm.js";

    export class StillAppSetup extends StillAppMixin(Components) {

        constructor() {
            super();
            //Bellow the entry point component is being set
            this.setHomeComponent(NewAccountForm);

            const userAuthSuccess = true;
            if (userAuthSuccess) {
                this.setAuthN(true);
            }

            //Revokes access to CheckingAccount provided by authN flag
            this.setWhiteList([CheckingAccount]);
        }

        async init() {
            return await AppTemplate.newApp();
        }

    }
    ```


!!! info "Blacklist precedence and considerations"
    - Blacklist has hte highest precedence in case it's combined with <b>`authN`</b> flag or <b>`whiteList`</b>, no matter in what order they are called, once <b>`blackList`</b> takes this hieghst priority if when a component is found there.

    - <b>`blackList components`</b> can only be set once, means, just as the <b>`whiteList`</b> (<a href="#white-list-explain">see explanation</a>).

<br>

Component rendering will be affectid by the component visibility (public, private), nevertheless, therefore, this happens in the application level, however Still.js also provides with <a href="../get-start/#render-if-ex1">(renderIf)</a> directive which allows controling component in the component level by putting such directive in the template for a specific HTML tag as shown in <a href="../get-start/#render-if-ex1">this example</a>.

<br><br>