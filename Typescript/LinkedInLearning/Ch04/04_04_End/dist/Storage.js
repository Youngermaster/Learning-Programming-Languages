/**
 * Retrieves data from storage
 */
function getFromStorage(key) {
    return __delay(function () {
        var serialized = localStorage.getItem(key) || "";
        return JSON.parse(serialized);
    });
}
/**
 * Save data to storage
 */
function saveToStorage(key, data) {
    return __delay(function () {
        var serialized = JSON.stringify(data);
        localStorage.setItem(key, serialized);
    });
}
/** helper function to introduce a random delay to simulate network conditions */
function __delay(action) {
    return new Promise(function (done) {
        setTimeout(function () { return done(action()); }, Math.random() * 2000 // delay from 0-2 seconds
        );
    });
}
