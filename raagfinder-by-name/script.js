// scripts.js

const allRaagNames = [
    "aheer_bhairav", "alhaiya_bilawal", "all", "bageshree", "bahar", "bairagi",
    "bhairav", "bhairavi", "bheempalasi", "bhoopali", "bihag", "chandrakauns",
    "charukeshi", "des", "dhani", "durga", "gorakh_kalyan", "gauri_(bhairav_ang)",
    "gurjari_todi", "hans_dhwani", "hindol", "jhinjhoti", "jog", "kafi",
    "kaushik_dhwani_(bhinn_shadj)", "kedar", "keerwani", "khamaj", "malhar",
    "madhukauns", "maru_bihag", "nand", "none", "nut-bhairav", "puriya",
    "puriya_dhanashri", "prateeksha", "rageshree", "sarang_(brindavani_sarang)",
    "saraswati", "shankara", "shree", "shuddha_kalyan", "shuddha_sarang",
    "shyam_kalyan", "tilak_kamod", "tilang", "vachaspati", "vibhas", "yaman"
]

const cellWidthShort = 150;
const cellWidthLong = 450;
const cellHeight = 50;
const cellPad = 25;

document.getElementById('search-btn').addEventListener("click", () => {
    const raagName = document.getElementById('raag-name').value.trim();  // input
    // raagName = findBestMatch(raagName, allRaagNames);
    // TEMP
    // const raagName = 'bairagi'

    // const infoTableResult = document.getElementById('info-container');  // output 1
    // infoTableResult.innerHTML = "";  // Clear previous table
    // infoTableResult.appendChild(fetchTable(raagName));

    const tonnetzImageResult = document.getElementById('tonnetz-container');  // output 1
    tonnetzImageResult.innerHTML = "";  // Clear previous image
    tonnetzImageResult.appendChild(fetchTonnetz(raagName));
});

function fetchTonnetz(raagName) {
    const tonnetzImage = new Image();
    tonnetzImage.src = `../assets/tonnetz/images/raag_${raagName}.png`;
    tonnetzImage.onerror = () => {
        tonnetzImage.src = `../assets/tonnetz/images/all_notes.png`;
    };
    return tonnetzImage;
}


// function displayDictAsTable(raagName) {
//     const plotContainer = document.getElementById('plot-container');
//     plotContainer.innerHTML = ''; // Clear previous plots

//     const table = document.createElement('table');
//     table.classList.add('info-table');

//     // fetch json data
//     const fs = require('fs');
//     fs.readFile(`../assets/tonnetz/tables/raag_${raagName}.json`, 'utf8', (err, jsonString) => {
//         if (err) {
//             console.log("Error reading file:", err);
//             return;
//         }
//         try {
//             const data = JSON.parse(jsonString);
//             console.log(data); // Your data object
//         } catch (err) {
//             console.log('Error parsing JSON:', err);
//         }
//     });

//     for (const [key, value] of Object.entries(infoDict)) {
//         const row = document.createElement('tr');

//         const keyCell = document.createElement('td');
//         keyCell.textContent = key;
//         row.appendChild(keyCell);

//         const valueCell = document.createElement('td');
//         valueCell.textContent = value;
//         row.appendChild(valueCell);

//         table.appendChild(row);
//     }
//     plotContainer.appendChild(table);
// }

function fetchTable(raagName) {

    const infoDict = {
        'Raag Name': raagName,
        'aaroha': 'S r m P n S',
        'avaroha': 'S n P m r S',
    };

    // const fs = require('fs');
    // fs.readFile(`../assets/tonnetz/tables/raag_${raagName}.json`, "utf8", (err, jsonString) => {
    //     if (err) {
    //         console.log("Error reading file:", err);
    //         return;
    //     }
    //     try {
    //         const data = JSON.parse(jsonString);
    //         console.log(data); // Your object
    //     } catch (err) {
    //         console.log("Error parsing JSON:", err);
    //     }
    // });

    const canvas = document.createElement('canvas');
    canvas.width = cellWidthShort + cellWidthLong;
    canvas.height = Object.keys(infoDict).length * cellHeight;
    const ctx = canvas.getContext('2d');

    let yOffset = 0;
    for (const [key, value] of Object.entries(infoDict)) {
        ctx.save();
        ctx.translate(0, yOffset);
        drawRow(ctx, key, value);
        ctx.restore();
        yOffset += cellHeight;
    }

    return canvas
}

function drawRow(ctx, key, value) {

    ctx.fillStyle = "#960B2E";
    ctx.fillRect(0, 0, cellWidthShort, cellHeight);
    ctx.fillStyle = "white";
    ctx.font = "20px monospace";
    ctx.textAlign = "right";
    ctx.textBaseline = "middle";
    ctx.fillText(key, cellWidthShort - cellPad, cellHeight / 2);

    ctx.fillStyle = "white";
    ctx.fillRect(cellWidthShort, 0, cellWidthLong, cellHeight);
    ctx.fillStyle = "#960B2E";
    ctx.font = "20px monospace";
    ctx.textAlign = "left";
    ctx.textBaseline = "middle";
    ctx.fillText(value, cellWidthShort + cellPad, cellHeight / 2);

}

function findBestMatch(name, names) {
    var bestMatch = names[0];
    var lowestDistance = levenshteinDistance(name, bestMatch);
    names.slice(1).forEach(function(n) {
        var dist = levenshteinDistance(name, n);
        if (dist < lowestDistance) {
            lowestDistance = dist;
            bestMatch = n;
        }
    });
    return bestMatch;
}

function levenshteinDistance(s, t) {
    var m = s.length, n = t.length, d = [];
    if (!m) return n;
    if (!n) return m;
    for (var i = 0; i <= m; i++) d[i] = [i];
    for (var j = 1; j <= n; j++) d[0][j] = j;
    for (var i = 1; i <= m; i++) {
        for (var j = 1; j <= n; j++) {
            var cost = (s[i - 1] === t[j - 1]) ? 0 : 1;
            d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost);
        }
    }
    return d[m][n];
}