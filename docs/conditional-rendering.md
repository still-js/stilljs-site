### Overview
When it comes to handle specific part of a component/UI in order to hide/unhide or render conditionally, Stilljs provides with a proper directive.



### The <b>`(showIf) - showIf`</b> Directive example:

As the directive itself suggests, this directive will <b>`show`</b> a content <b>`If`</B> the assigned flag matches the stated condition, in case the condition is not matched, it'll hide the content.

It's mandatory to specify the container (see <a href="../directive/#container-directive">container directive</a>) when using `(showIf)` directive, and, in the container itself, we place our condition as follow bellow:



=== "template"

    ```html title="This is the template code snippet" linenums="1"
    <div>
        <p>
            Click to hide/unhide the date
        </p>
        <button (click)="handleShowDate()">Hide/Unhide date</button>
        <div (showIf)="self.showDate">
            Today is @todayDate
        </div>
    </div>
    ```

=== "component"

    ```js title="This is the component code snippet" linenums="1"

    // Because we don't need to listen to changes, the variable is turned to Prop
    /** @Prop */
    todayDate = new Date().toDateString();

    /** @Prop */
    showDate = true;

    handleShowDate() {
        this.showDate = !this.showDate;
    }
    ```

In the above example, the flag need to be boolean, in this case it will be checked that if it's true, then the data will be showed, otherise (if false), it'll hidden. 

It's also possible to negate the <b>`(showIf)` - renderIf</b> flag by putting ! before the flag itself, if that's the case we'll have the code as follow:

```html
<div (showIf)="!self.showDate">
```

<br>

#### Using expresion as flag

It's also possible to use expression when using the `(renderIf)` directive, for that, the expression needs to produce a boolean result as follow:

=== "template"

    ```html title="This is the template code snippet" linenums="1"
    <div>
        <nav>
            <div>
                <button (click)="showOption(2)">2</button>
                <button (click)="showOption(3)">3</button>
                <button (click)="showOption(5)">5</button>
            </div>
        </nav>
        <p>The bellow content is presente acoordng to the flag assigned value</p>
        <div (showIf)="self.checkFlag==5">Contante when flag is 5</div>
        <div (showIf)="self.checkFlag==3">Whrn flag is 3 this is the content</div>
        <div (showIf)="self.checkFlag==2">Flag value was assigned with 2</div>
    </div>
    ```

=== "component"

    ```js title="This is the component code snippet" linenums="1"
    /** @Prop */
    isMainFlag = true;

    /** @Prop */
    checkFlag;

    // Set the initial value for checkFlag  
    // when the component got initiated
    stAfterInit(){
        this.checkFlag = 3;
    }

    showOption(val){
        this.checkFlag = val;
    }
    ```

<br>

### The <b>`(renderIf)`</b> Directive example:

The `(renderIf)` directive will not render the UI part if the flag value is false, whereas `(showIf)` hides only giving the possibility of unhiding it afterwards.

Unlike `(showIf)`, the `(renderIf)` is flaged with a boolean only, means, expressions kind of flagging is not supported.


<style>

    table.annotations tr td:first-child {
        width: 140px;
        font-weight: bold;
    }

    table.annotations tr:first-child {
        font-weight: bold !important;
    }

    table.annotations td {
        padding-left: 5px;
        padding-top: 5px;
        border: 1px solid rgb(193, 185, 185);
    }

    table.annotations tr:nth-child(even) {
        background:rgb(245, 239, 239);
    }

    table.annotations  { font-size:12px;, border: 1px solid; }

    dependent-l {
        border: 1px solid orange;
        background: yellow;
        text-align: center;
        border-radius:6px;
        margin-left: 5px;
        padding: 3px;
        font-size: 12px;
    }


    .tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
    }

    .tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: grey;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 5px;

    /* Position the tooltip */
    position: absolute;
    z-index: 1;
    }

    .tooltip:hover .tooltiptext {
    visibility: visible;
    }

</style>

<br>





