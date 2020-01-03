package lib

var message string

// PublicAttribute * This is some documentation
var PublicAttribute string

func init() {
	message = "[init] Hello :3"
	PublicAttribute = "Public Attribute"
}

// ! Naming conventions
// * start with lower case make the function unexported.
// * start with Upper case able the function to be exported.

func getHello() string {
	return "Hello private"
}

// GetHello return a message
// * Some little documentation
func GetHello() string {
	return "Hello Public" + "\n" + message
}
