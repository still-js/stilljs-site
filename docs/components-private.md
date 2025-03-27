### StillJS Routing and Routing Object

### Simple example

=== "HomeComponent.js"

    ```js title="HomeComponent.js" linenums="1" hl_lines="12 19-21"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";
    import { UsersGridComponent } from "components/users/UsersGridComponent.js";
    import { Router } from "../../@still/routing/router.js";

    export class HomeComponent extends ViewComponent {

        isPublic = true;
        template = `
            <h1>
                Welcome to the main page
            </h1>
            <a (click)="gotoUsersGrid()">List Users</a>
        `;

        constructor() {
            super();
        }

        gotoUsersGrid(){
            Router.goto(UsersGridComponent);
        }

    }
    ```

=== "UsersGridComponent.js"

    ```js title="HomeComponent.js" linenums="1"
    import { ViewComponent } from "../../@still/component/super/ViewComponent.js";

    export class UsersGridComponent extends ViewComponent {

        isPublic = true;
        template = `
            <h2>Users Data</h2>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>
                <tr>
                    <td>1</td>
                    <td>Alice Johnson</td>
                    <td>alice@example.com</td>
                    <td>Admin</td>
                </tr>
                <tr>
                    <td>2</td>
                    <td>Bob Smith</td>
                    <td>bob@example.com</td>
                    <td>Editor</td>
                </tr>
            </table>
        `;

        constructor() {
            super();
        }

    }
    ```

??? abstract "Routing considerations"

    For this example routing is implemented inside another method which then
    We're passing the component we want to navigate/go to, follow such component.

!!! note "Important consideration"

    In the above code, on the HomeComponent we have the Route.goto() (line 20) being
    called inside the component method gotoUsersGrid(), as this method could
    be named anything (following  JS naming convention), nevertheless, this is
    then called on the template <a></a> tag (line 12), as this is the practice in StillJS.