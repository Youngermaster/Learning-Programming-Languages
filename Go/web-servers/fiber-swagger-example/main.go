package main

import (
	"log"

	"github.com/gofiber/fiber/v2"
	"github.com/swaggo/fiber-swagger"
	// _ "github.com/swaggo/fiber-swagger/example/docs" // This line loads the Swagger UI files.
	_ "github.com/youngermaster/fiber-swagger-example/docs"
)

// HelloHandler returns a friendly greeting.
//
//	@Summary		Say hello
//	@Description	Returns a friendly greeting
//	@Tags			Greetings
//	@Accept			json
//	@Produce		json
//	@Success		200	{string}	string	"Hello, world!"
//	@Router			/hello [get]
func HelloHandler(c *fiber.Ctx) error {
	return c.SendString("Hello, world!")
}

//	@title			Swagger Golang Chimbo
//	@description	This is a sample Swagger API for Go Fiber.
//	@version		1.0
//	@host			localhost:3000
//	@BasePath		/
func main() {
	app := fiber.New()

	// Route to access the auto-generated Swagger docs.
	app.Get("/swagger/*", fiberSwagger.WrapHandler)

	// Route to test the API.
	app.Get("/hello", HelloHandler)

	log.Fatal(app.Listen(":3000"))
}
