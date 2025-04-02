### Using CDN For Lone Component and/or Microfrontend
<hr/>
In the CND mode, instead of the whole folder structure, only the `app` folder and `route.map.js` file are needed, also, we need to set the path where they'll be placeed by using the `STILL_HOME` variable, follow the folder structure example as well as coding sample right after:


<a name="project-structure"></a>


#### 1. Folder Structure
=== "Folder structure in CDN mode"
```js hl_lines="3-7"
my-project-name
|
|_ microfronteds
   |_ still
      |_ app
      |  |_ components
      |_ route.map.js
   |_ another-mf-provider

```



!!! info "Project folder substructure considerations"

    In the above example structure, we have a folder name `microfronted`, where we have the `still` sub-folder, and, we also have `component` folder inside the app root, nevertheless all 3 (microfronted, still and component) can be named as per the dev will.


<br/>

#### 2. Basic code sample

=== "index.html"

    ```html linenums="1" hl_lines="5-6 9"
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <script> STILL_HOME = 'microfronteds/still/' </script>
            <link href="https://cdn.jsdelivr.net/npm/@stilljs/core@0.0.8/@still/ui/css/stillcss" rel="stylesheet">
            <script src="https://cdn.jsdelivr.net/npm/@stilljs/core@0.0.8/@still/lone.js"type="module"></script>
        </head>
        <body>
            <st-element component="CounterComponent"></st-element>
        </body>
    </html>
    ```



=== "CounterComponent.js"
	```js linenums="1"
    /** 
     * This file will be place inside the components folder
     * according to the above folder structure 
     * */
    export class CounterComponent extends ViewComponent {

        isPublic = true;
        count = 0;

        template = `
        <div>
            <p>My counter state is @count</p>
            <button (click)="increment()">Increment (@count)</button>
        </div>
        `;

        increment() {
            this.count = this.count.value + 1;
        }
    }
	```

=== "route.map.js"
	```js linenums="1" hl_lines="7"
    /** 
     * This file will be placed in the root of app folder
     * */
    export const stillRoutesMap = {
        viewRoutes: {
            regular: {
                CounterComponent: { path: "app/components/" }
            },
            lazyInitial: {}
        }
    }
	```


We can add our components in our HTML/App (React, Angular, etc.) by using`<st-element>` tag instead of depending on the Still.js Application container to render the components, as it (Application container) is totally inexistent in this case.

!!! warning "Component creation"
    Although we don't have <b>Still project structure</b> in <b>CDN mode</b>, it's always recommended to use the still-cli to generate components</b>, as this is the way the routes will be automatically added/managed in addition to the component generation.


!!! info "Routing and route.map.js file"
    Despite Still App container is not available in the <b>CND mode</b>, <b>navigation feature is still available</b>, plus, <b>it's needed for the framework to know how to locate the components, hence the route.map.js</b> file.


<br>

#### 3. Running the project in CDN mode
The proper way of running the project in the CDN mode is by having it from a web server, we'll use `live-server` in this example, for that let's first install it:

```js
npm i -g live-server
```

Running the project from inside the project root folder ( <a href="#project-structure">`my-project-name` </a>)
```js
npx live-server
```

Run result:
<iframe src="https://still-js.github.io/stilljs-doc-website/#/for-cdn/example" 
            frameBorder="0"
            style="border: 1px solid grey; border-radius:4px; padding: 5px; background: white"
            >
</iframe>

<br>

#### CDN Files

<div style="padding-left: 20px;">
JavaScript: 
```
https://cdn.jsdelivr.net/npm/@stilljs/core@latest/@still/lone.js
```
</div>


<div style="padding-left: 20px;">
CSS: 
``` 
https://cdn.jsdelivr.net/npm/@stilljs/core@latest/@still/ui/css/still.css
```
</div>
<h2>You're good to go! enjoy your coding.</h2>
<br/>