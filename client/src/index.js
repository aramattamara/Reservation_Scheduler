import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"

const pizzaData = [
  {
    name: "Focaccia",
    ingredients: "Bread with italian olive oil and rosemary",
    price: 6,
    photoName: "pizzas/focaccia.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Margherita",
    ingredients: "Tomato and mozarella",
    price: 10,
    photoName: "pizzas/margherita.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Spinaci",
    ingredients: "Tomato, mozarella, spinach, and ricotta cheese",
    price: 12,
    photoName: "pizzas/spinaci.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Funghi",
    ingredients: "Tomato, mozarella, mushrooms, and onion",
    price: 12,
    photoName: "pizzas/funghi.jpg",
    soldOut: false,
  },
  {
    name: "Pizza Salamino",
    ingredients: "Tomato, mozarella, and pepperoni",
    price: 15,
    photoName: "pizzas/salamino.jpg",
    soldOut: true,
  },
  {
    name: "Pizza Prosciutto",
    ingredients: "Tomato, mozarella, ham, aragula, and burrata cheese",
    price: 18,
    photoName: "pizzas/prosciutto.jpg",
    soldOut: false,
  },
];

// import App from './App';

function App() {
  return (
      <div>
        <Header/>
        <Pizza/>
        <Menu/>
        <Footer/>
      </div>
  )
}

function Header() {
  return (
      <header className="header">
        <h1>Home</h1>
        <h1>Reservations</h1>
        <h1>Our Story</h1>
        <h1>Menu</h1>
        <h1>Order online</h1>
        <h1>Contact</h1>
      </header>
  )
}

function Menu() {
  return (
      <main className='menu'>
        <h2>Our menu</h2>

        <ul>

          {pizzaData.map((pizza) => <Pizza pizzaj={pizza} key={pizza.name}/>)}
        </ul>
      </main>
  )
}

function Pizza(props) {
  return(
      <li className='pizza'>
        <span>{props.pizzaj.name}</span>
        <img src={props.pizzaj.photoName} alt={props.pizzaj.name}></img>
        <span>{props.pizzaj.ingredients}</span>
        <span>{props.pizzaj.name}</span>
      </li>
  )

}

function Footer() {
  return (
      <footer className="footer">
        {new Date().toLocaleDateString()} We're currently open
      </footer>
  )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
      <App/>
    </React.StrictMode>
);

