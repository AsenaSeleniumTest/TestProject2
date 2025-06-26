let restaurantMenu=
{
    restaurantname: "lordusbq cafe",
    menu: [
        {
            meals:
            [
               {
                name:"Chicken Burger",
                price: 5.99,
                description:"A chicken breast fillet, with tomato, avocado, bacon on a almod bread"
               },  
               {
                name:"beef burger",
                price: 6.99,
                description:"A beef 3/4 cooked , with tomato,avocado, bacon and crispy cheese on a almond bread"
               },
               {
                name:"Fish Burger",
                price: 7.99,
                description:"A fish fillet, with tomato, avocado, bacon on a almod bread"
               },
               {
                name:"Veggie Burger",
                price: 4.99,
                description:"A veggie patty, with tomato, avocado, bacon on a almod bread"
               }        
            ]

        },
        {
            drinks:
            [
                {
                    name:"Refresco",
                    price: 1.99,
                    description:"A refreshing cola drink"
                },
                {
                    name:"Lemonade",
                    price: 2.49,
                    description:"A tangy lemonade drink"
                },
                {
                    name:"Regular coffee",
                    price: 2.99,
                    description:"A chilled iced tea with a hint of lemon"
                },
                {
                    name:"Capucchino Coffee",
                    price: 3.49,
                    description:"A hot cup of coffee to start your day"
                }

            ]
        }

    ],
    fooditems: function()
    {
        alert("food items are: " + restaurantMenu.menu[0].meals.map(meal => meal.name)+"\n"+
              "with prices: " + restaurantMenu.menu[0].meals.map(meal => meal.price)+"\n"+ 
            "and descriptions: " + restaurantMenu.menu[0].meals.map(meal => meal.description));
    },
    drinksitems: function()
    {
        prompt("drinks items are: " + restaurantMenu.menu[1].drinks.map(drink => drink.name)+"\n"+
              "with prices: " + restaurantMenu.menu[1].drinks.map(drink => drink.price)+"\n"+ 
            "and descriptions: " + restaurantMenu.menu[1].drinks.map(drink => drink.description));
    }

}



