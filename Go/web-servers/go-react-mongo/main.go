package main

import (
	"context"
	"fmt"

	"os"

	swagger "github.com/arsmn/fiber-swagger/v2"
	"github.com/gofiber/fiber/v2"
	"github.com/gofiber/fiber/v2/middleware/cors"
	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"

	"github.com/youngermaster/go-react-mongo/models"
)

func main() {

	port := os.Getenv("PORT")
	mongodb := os.Getenv("MONGODB_URI")

	if port == "" {
		port = "3000"
	}

	if mongodb == "" {
		mongodb = "mongodb://localhost:27017/gomongodb"
	}

	app := fiber.New()
	app.Get("/swagger/*", swagger.HandlerDefault) // default
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(mongodb))

	if err != nil {
		panic(err)
	}

	app.Use(cors.New())

	app.Static("/", "./client/dist")

	app.Post("/users", func(c *fiber.Ctx) error {
		var user models.User

		c.BodyParser(&user)

		coll := client.Database("gomongodb").Collection("users")
		result, err := coll.InsertOne(context.TODO(), bson.D{{
			Key:   "name",
			Value: user.Name,
		}})

		if err != nil {
			panic(err)
		}

		return c.JSON(&fiber.Map{
			"data": result,
		})
	})

	app.Get("/users", func(c *fiber.Ctx) error {
		var users []models.User

		coll := client.Database("gomongodb").Collection("users")
		results, error := coll.Find(context.TODO(), bson.M{})

		if error != nil {
			panic(error)
		}

		for results.Next(context.TODO()) {
			var user models.User
			results.Decode(&user)
			users = append(users, user)
		}

		return c.JSON(&fiber.Map{
			"users": users,
		})

	})

	app.Listen(":" + port)
	fmt.Println("Server on port 3000")
}
