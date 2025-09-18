const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({search: "Search service running"});
});

app.listen(7500, () => {
    console.log("Search service running on port 7500");
});
