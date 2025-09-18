const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({catalog: "Catalog service running"});
});

app.listen(7400, () => {
    console.log("Catalog service running on port 7400");
});
