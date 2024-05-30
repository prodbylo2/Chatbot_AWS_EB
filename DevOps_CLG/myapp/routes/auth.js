const express = require('express');
const passport = require('passport');
const router = express.Router();

router.post('/login',
  passport.authenticate('local', { failureRedirect: '/' }),
  (req, res) => {
    res.redirect('/chatbot');
  }
);

router.get('/logout', (req, res) => {
  req.logout(() => {
    res.redirect('/');
  });
});

module.exports = router;
