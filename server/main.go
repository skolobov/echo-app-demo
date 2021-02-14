package main

import (
    "fmt"
    "io/ioutil"
    "net/http"

    "github.com/labstack/echo/v4"
    "github.com/labstack/echo/v4/middleware"
)

func main() {
    e := echo.New()
    e.Use(middleware.Logger())
    e.Any("/", func(c echo.Context) error {
        method := c.Request().Method
        body, err := ioutil.ReadAll(c.Request().Body)
        if err != nil {
            return err
        }
        response := fmt.Sprintf("Method %s, Body \"%s\"", method, body)
        return c.String(http.StatusOK, response)
    })
    e.Logger.Fatal(e.Start(":1323"))
}
