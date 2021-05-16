## How to find color name by hex code programetically
```
const fetch = require("node-fetch");

fetch('https://www.thecolorapi.com/id?hex=EEF3FF').then((resp)=>{
    resp.json().then((json)=>{
        console.log(json.name.value);
    })
});
```
