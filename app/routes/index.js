var express = require('express');
var router = express.Router();

var flare = require('../public/data/flareData_after')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

/** Query data */
router.get('/data', function(req, res, next) {
  res.send(flare);
});

module.exports = router;
