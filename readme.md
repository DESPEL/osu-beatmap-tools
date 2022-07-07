# How to Run

Pip Install
- osu-tools
- fastapi
- uvicorn

```
    pip install osu-tools fastapi uvicorn
```

Install chrome extensions:
- TamperMonkey
- CORS Unblock

Create a new script in tampermonkey and paste the text in script.txt
```
// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://osu.ppy.sh/beatmapsets*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=ppy.sh
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    setTimeout(async () => {
        let response = await fetch("http://127.0.0.1:8000/beatmaps", {method: "GET"})
        let beatmaps = (await response.json()).beatmaps.sort()
        console.log(beatmaps)
        setInterval(() => {
            const maps = document.querySelectorAll(".beatmapsets__item")
            for (const container of maps) {
                const map_url = container.children[0].children[0].href.split("/")
                const bmap_id = parseInt(map_url[map_url.length - 1])
                if (beatmaps.includes(bmap_id)) {
                    container.style.opacity = 0.01
                } else {
                    console.log(bmap_id)
                }
            }

        },250)
    }, 500)
    // Your code here...
})();
```

Disable cors (click the CORS Unblock icon, should be colored instead of grayed-out)

Run the beatmap_server.py with
```
    python3 -m uvicorn beatmap_server:app --reload
```

Now search for beatmaps in osu, already downloaded ones will be transparent.

If you downloaded beatmaps and want to gray out the new ones go to: `http://localhost:8000/refresh`