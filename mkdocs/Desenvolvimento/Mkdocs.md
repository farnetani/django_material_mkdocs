# Usando Mkdocs Material

[Mkdocs Material - Link][1]

  [1]: https://squidfunk.github.io/mkdocs-material/getting-started/

### Atalhos

* Well-designed search interface accessible through hotkeys (<kbd>F</kbd> or
  <kbd>S</kbd>), intelligent grouping of search results, search term
  highlighting and lazy loading.

### Favicon

> Default: `assets/images/favicon.png`

### Imagem

[![Material for MkDocs](../assets/images/material.png)](../assets/images/material.png)

> Atenção: `Sem Link`

![Material for MkDocs](../assets/images/material.png)

### Link

For detailed instructions see the [getting started guide][3].

  [3]:../index.md

## Headings

### The 3rd level

#### The 4th level

##### The 5th level

###### The 6th level

## Headings <small>with secondary text</small>

### The 3rd level <small>with secondary text</small>

#### The 4th level <small>with secondary text</small>

##### The 5th level <small>with secondary text</small>

###### The 6th level <small>with secondary text</small>

## Blockquotes

> Morbi eget dapibus felis. Vivamus venenatis porttitor tortor sit amet rutrum.
  Pellentesque aliquet quam enim, eu volutpat urna rutrum a. Nam vehicula nunc
  mauris, a ultricies libero efficitur sed. *Class aptent* taciti sociosqu ad
  litora torquent per conubia nostra, per inceptos himenaeos. Sed molestie
  imperdiet consectetur.

### Other content blocks

> Vestibulum vitae orci quis ante viverra ultricies ut eget turpis. Sed eu
  lectus dapibus, eleifend nulla varius, lobortis turpis. In ac hendrerit nisl,
  sit amet laoreet nibh.
  ``` js hl_lines="8"
  var _extends = function(target) {
    for (var i = 1; i < arguments.length; i++) {
      var source = arguments[i];
      for (var key in source) {
        target[key] = source[key];
      }
    }
    return target;
  };
  ```

  > > Praesent at `:::js return target`, sodales nibh vel, tempor felis. Fusce
      vel lacinia lacus. Suspendisse rhoncus nunc non nisi iaculis ultrices.
      Donec consectetur mauris non neque imperdiet, eget volutpat libero.

## Lists

### Unordered lists

* Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus tellus
  non sem sollicitudin, quis rutrum leo facilisis. Nulla tempor lobortis orci,
  at elementum urna sodales vitae. In in vehicula nulla, quis ornare libero.

    * Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    * Nam vulputate tincidunt fringilla.
    * Nullam dignissim ultrices urna non auctor.

* Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin ut
  eros sed sapien ullamcorper consequat. Nunc ligula ante, fringilla at aliquam
  ac, aliquet sed mauris.

* Nulla et rhoncus turpis. Mauris ultricies elementum leo. Duis efficitur
  accumsan nibh eu mattis. Vivamus tempus velit eros, porttitor placerat nibh
  lacinia sed. Aenean in finibus diam.

### Ordered lists

1. Integer vehicula feugiat magna, a mollis tellus. Nam mollis ex ante, quis
  elementum eros tempor rutrum. Aenean efficitur lobortis lacinia. Nulla
  consectetur feugiat sodales.

2. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur
  ridiculus mus. Aliquam ornare feugiat quam et egestas. Nunc id erat et quam
  pellentesque lacinia eu vel odio.

    1. Vivamus venenatis porttitor tortor sit amet rutrum. Pellentesque aliquet
      quam enim, eu volutpat urna rutrum a. Nam vehicula nunc mauris, a
      ultricies libero efficitur sed.

        1. Mauris dictum mi lacus
        2. Ut sit amet placerat ante
        3. Suspendisse ac eros arcu

    2. Morbi eget dapibus felis. Vivamus venenatis porttitor tortor sit amet
      rutrum. Pellentesque aliquet quam enim, eu volutpat urna rutrum a. Sed
      aliquet, neque at rutrum mollis, neque nisi tincidunt nibh.

    3. Pellentesque eget `:::js var _extends` ornare tellus, ut gravida mi.
    ``` js hl_lines="1"
    var _extends = function(target) {
      for (var i = 1; i < arguments.length; i++) {
        var source = arguments[i];
        for (var key in source) {
          target[key] = source[key];
        }
      }
      return target;
    };
    ```

### Definition lists

Lorem ipsum dolor sit amet

:   Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus
    tellus non sem sollicitudin, quis rutrum leo facilisis. Nulla tempor
    lobortis orci, at elementum urna sodales vitae. In in vehicula nulla.

    Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis.
    Nam vulputate tincidunt fringilla.
    Nullam dignissim ultrices urna non auctor.

Cras arcu libero

:   Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. Proin
    ut eros sed sapien ullamcorper consequat. Nunc ligula ante, fringilla at
    aliquam ac, aliquet sed mauris.

## Code blocks

### Inline

Morbi eget `dapibus felis`. Vivamus *`venenatis porttitor`* tortor sit amet
rutrum. Class aptent taciti sociosqu ad litora torquent per conubia nostra,
per inceptos himenaeos. [`Pellentesque aliquet quam enim`](/), eu volutpat urna
rutrum a.

Nam vehicula nunc `:::js return target` mauris, a ultricies libero efficitur
sed. Sed molestie imperdiet consectetur. Vivamus a pharetra leo. Pellentesque
eget ornare tellus, ut gravida mi. Fusce vel lacinia lacus.

### Listing

    #!js hl_lines="8"
    var _extends = function(target) {
      for (var i = 1; i < arguments.length; i++) {
        var source = arguments[i];
        for (var key in source) {
          target[key] = source[key];
        }
      }
      return target;
    };

## Horizontal rules

Aenean in finibus diam. Duis mollis est eget nibh volutpat, fermentum aliquet
dui mollis. Nam vulputate tincidunt fringilla. Nullam dignissim ultrices urna
non auctor.

***

### Anotações

!!! question "Why is there an edit button at the top of every article?"

    If the `repo_url` is set to a GitHub or BitBucket repository, and the
    `repo_name` is set to *GitHub* or *BitBucket* (implied by default), an
    edit button will appear at the top of every article. This is the automatic
    behavior that MkDocs implements. See the [MkDocs documentation][19] on more
    guidance regarding the `edit_uri` attribute, which defines whether the edit
    button is shown or not.

  [19]: http://www.mkdocs.org/user-guide/configuration/#edit_uri

!!! warning "Installation on macOS"

    When you're running the pre-installed version of Python on macOS, `pip`
    tries to install packages in a folder for which your user might not have
    the adequate permissions. There are two possible solutions for this:

    1. **Installing in user space** (recommended): Provide the `--user` flag
      to the install command and `pip` will install the package in a user-site
      location. This is the recommended way.

    2. **Switching to a homebrewed Python**: Upgrade your Python installation
      to a self-contained solution by installing Python with Homebrew. This
      should eliminate a lot of problems you may be having with `pip`.

!!! failure "Error: unrecognized theme 'material'"

    If you run into this error, the most common reason is that you installed
    MkDocs through some package manager (e.g. Homebrew or `apt-get`) and the
    Material theme through `pip`, so both packages end up in different
    locations. MkDocs only checks its install location for themes.

!!! info "Search language support for Chinese"

    [lunr-languages][18] currently doesn't include a stemmer for Chinese or
    other Asian languages, but uses the Japanese stemmer, as some users
    reported pretty decent results.

#### Primary colors

> Default: `indigo`

Click on a tile to change the primary color of the theme:

<button data-md-color-primary="red">Red</button>
<button data-md-color-primary="pink">Pink</button>
<button data-md-color-primary="purple">Purple</button>
<button data-md-color-primary="deep-purple">Deep Purple</button>
<button data-md-color-primary="indigo">Indigo</button>
<button data-md-color-primary="blue">Blue</button>
<button data-md-color-primary="light-blue">Light Blue</button>
<button data-md-color-primary="cyan">Cyan</button>
<button data-md-color-primary="teal">Teal</button>
<button data-md-color-primary="green">Green</button>
<button data-md-color-primary="light-green">Light Green</button>
<button data-md-color-primary="lime">Lime</button>
<button data-md-color-primary="yellow">Yellow</button>
<button data-md-color-primary="amber">Amber</button>
<button data-md-color-primary="orange">Orange</button>
<button data-md-color-primary="deep-orange">Deep Orange</button>
<button data-md-color-primary="brown">Brown</button>
<button data-md-color-primary="grey">Grey</button>
<button data-md-color-primary="blue-grey">Blue Grey</button>
<button data-md-color-primary="white">White</button>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorPrimary = this.dataset.mdColorPrimary;
    })
  })
</script>

#### Accent colors

> Default: `indigo`

Click on a tile to change the accent color of the theme:

<button data-md-color-accent="red">Red</button>
<button data-md-color-accent="pink">Pink</button>
<button data-md-color-accent="purple">Purple</button>
<button data-md-color-accent="deep-purple">Deep Purple</button>
<button data-md-color-accent="indigo">Indigo</button>
<button data-md-color-accent="blue">Blue</button>
<button data-md-color-accent="light-blue">Light Blue</button>
<button data-md-color-accent="cyan">Cyan</button>
<button data-md-color-accent="teal">Teal</button>
<button data-md-color-accent="green">Green</button>
<button data-md-color-accent="light-green">Light Green</button>
<button data-md-color-accent="lime">Lime</button>
<button data-md-color-accent="yellow">Yellow</button>
<button data-md-color-accent="amber">Amber</button>
<button data-md-color-accent="orange">Orange</button>
<button data-md-color-accent="deep-orange">Deep Orange</button>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorAccent = this.dataset.mdColorAccent;
    })
  })
</script>

### Font family

> Default: `Roboto` and `Roboto Mono`

By default the [Roboto font family][12] is included with the theme, specifically
the regular sans-serif type for text and the `monospaced` type for code. Both
fonts are loaded from [Google Fonts][13] and can be changed to other fonts,
like for example the [Ubuntu font family][14]:

``` yaml
theme:
  font:
    text: 'Ubuntu'
    code: 'Ubuntu Mono'
```

The text font will be loaded in weights 400 and **700**, the `monospaced` font
in regular weight. If you want to load fonts from other destinations or don't
want to use the Google Fonts loading magic, just set `font` to `false`:

``` yaml
theme:
  font: false
```

  [12]: https://fonts.google.com/specimen/Roboto
  [13]: https://fonts.google.com
  [14]: https://fonts.google.com/specimen/Ubuntu


## Data tables

| Sollicitudo / Pellentesi | consectetur | adipiscing | elit    | arcu | sed |
| ------------------------ | ----------- | ---------- | ------- | ---- | --- |
| Vivamus a pharetra       | yes         | yes        | yes     | yes  | yes |
| Ornare viverra ex        | yes         | yes        | yes     | yes  | yes |
| Mauris a ullamcorper     | yes         | yes        | partial | yes  | yes |
| Nullam urna elit         | yes         | yes        | yes     | yes  | yes |
| Malesuada eget finibus   | yes         | yes        | yes     | yes  | yes |
| Ullamcorper              | yes         | yes        | yes     | yes  | yes |
| Vestibulum sodales       | yes         | -          | yes     | -    | yes |
| Pulvinar nisl            | yes         | yes        | yes     | -    | -   |
| Pharetra aliquet est     | yes         | yes        | yes     | yes  | yes |
| Sed suscipit             | yes         | yes        | yes     | yes  | yes |
| Orci non pretium         | yes         | partial    | -       | -    | -   |

Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus tellus
non sem sollicitudin, quis rutrum leo facilisis. Nulla tempor lobortis orci,
at elementum urna sodales vitae. In in vehicula nulla, quis ornare libero.

| Left       | Center   | Right   |
| :--------- | :------: | ------: |
| Lorem      | *dolor*  | `amet`  |
| [ipsum](/) | **sit**  |         |

Vestibulum vitae orci quis ante viverra ultricies ut eget turpis. Sed eu
lectus dapibus, eleifend nulla varius, lobortis turpis. In ac hendrerit nisl,
sit amet laoreet nibh.

<table>
  <colgroup>
    <col width="30%">
    <col width="70%">
  </colgroup>
  <thead>
    <tr class="header">
      <th>Table</th>
      <th>with colgroups (Pandoc)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Lorem</td>
      <td>ipsum dolor sit amet.</td>
    </tr>
    <tr>
      <td>Sed sagittis</td>
      <td>eleifend rutrum. Donec vitae suscipit est.</td>
    </tr>
  </tbody>
</table>

***

<table style="white-space: nowrap;">
  <thead>
    <tr>
      <th colspan="4">Available language stemmers</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>da</code> / Danish</td>
      <td><code>du</code> / Dutch</td>
      <td><code>en</code> / English</td>
      <td><code>fi</code> / Finnish</td>
    </tr>
    <tr>
      <td><code>fr</code> / French</td>
      <td><code>de</code> / German</td>
      <td><code>hu</code> / Hungarian</td>
      <td><code>it</code> / Italian</td>
    </tr>
    <tr>
      <td><code>jp</code> / Japanese</td>
      <td><code>no</code> / Norwegian</td>
      <td><code>pt</code> / Portugese</td>
      <td><code>ro</code> / Romanian</td>
    </tr>
    <tr>
      <td><code>ru</code> / Russian</td>
      <td><code>es</code> / Spanish</td>
      <td><code>sv</code> / Swedish</td>
      <td><code>tr</code> / Turkish</td>
    </tr>
  </tbody>
</table>
