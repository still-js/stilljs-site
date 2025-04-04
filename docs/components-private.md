### Private Component

!!! info "Work in Progress - Coming Soon"

    We're still preparing and elaborating the content which will be part of this page, please just be a bit patient, It'll be here soon.

<br/>

### Overview
Private components in Still.js help manage user authorization for navigation and rendering. If a component is not public (`isPublic = false` or unset), custom logic is required to control its visibility. Still.js allows blacklisting and whitelisting components based on custom requirements, overriding the isPublic flag regardless of its value (true or false).

<br>

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

In the example above, the NewAccountForm component includes buttons to navigate to private components, causing an Unauthorized access warning. To enable authorized navigation, two methods can be used:

- ***setAuthN*** - For the Application context, when the AuthN is set to true, it understand that navigation and component embeding can happen at all level, anyway, there might be some exception which cannot be addressed here.


- ***setWhiteList*** - It's possible to specify a list of components that should be whitelisted, by doing that, even if the component is private, it'll always be accessible.