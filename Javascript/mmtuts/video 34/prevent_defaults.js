let stuff = "some properties as document.querySelector('Stuff')"

// With the e in any function this will prevent some defaults 
// behaviours
function anotherFuncion(e) {
	e.preventDefault();
	// Stuff
}

// How I can call they?
stuff.anotherFuncion;
// And that's it, you don't need to pass a parameter


// Now what happen if I want to execute more than one function?

function firstFunction(e) {
	e.preventDefault();
	// More Stuff
}

function secondFunction() {
	// Stuff
}

function thirdFunction(name) {
	console.log(name);
}

stuff.addEventListener("click", firstFunction);
stuff.addEventListener("click", secondFunction);

// We can also use anonimus functios inside of the Event Listener
stuff.addEventListener("click", function (e) {
	thirdFunction("Juan Manuel Young Hoyos");
});
