const mongoose = require('mongoose');

//How my data looks
const LocateSchema = mongoose.Schema({
    input: {
        type: String,
        required: true
    }
});

module.exports = mongoose.model('Locate', LocateSchema);