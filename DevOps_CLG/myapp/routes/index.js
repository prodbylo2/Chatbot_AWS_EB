const express = require('express');
const router = express.Router();

// Middleware to ensure the user is authenticated (you may need to adjust this to match your setup)
function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
      return next();
  }
  res.redirect('/login');
}

// Route to render the chatbot page
router.get('/chatbot', ensureAuthenticated, (req, res) => {
  res.render('chatbot');
});

module.exports = router;


