const express = require('express');
const session = require('express-session');
const passport = require('passport');
const flash = require('connect-flash');
const path = require('path');

const app = express();
const port = process.env.PORT || 3000;

// Passport Config
require('./config/passport-config')(passport);

// EJS
app.set('view engine', 'ejs');

// Express body parser
app.use(express.urlencoded({ extended: true }));

// Express session
app.use(session({
    secret: 'secret',
    resave: true,
    saveUninitialized: true
}));

// Passport middleware
app.use(passport.initialize());
app.use(passport.session());

// Connect flash
app.use(flash());

// Global variables
app.use((req, res, next) => {
    res.locals.success_msg = req.flash('success_msg');
    res.locals.error_msg = req.flash('error_msg');
    res.locals.error = req.flash('error');
    next();
});

// Static folder
app.use(express.static(path.join(__dirname, 'public')));

// Routes
app.use('/', require('./routes/index'));
app.use('/auth', require('./routes/auth'));

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
