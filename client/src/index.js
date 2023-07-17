import React from 'react';
import ReactDOM from 'react-dom/client';
import "./index.css"

const menuData = [
  {
    name: "Focaccia",
    type: "Antipasti",
    ingredients: "Bread with italian olive oil and rosemary",
    price: 6,
    photoName: undefined,
    soldOut: false,
    tag: null,
  },
  {
    name: "Fried Calamari",
    type: "Antipasti",
    ingredients: "Fried calamari with bread",
    price: 13,
    photoName: undefined,
    soldOut: false,
    tag: null,
  },
  {
    name: "Fried Zucchini",
    type: "Antipasti",
    ingredients: "Fried calamari with bread",
    price: 13,
    photoName: undefined,
    soldOut: false,
    tag: "vegetarian"
  },
  {
    name: "Insalata Mista",
    type: "Antipasti",
    ingredients: "Fried calamari with bread",
    price: 13,
    photoName: undefined,
    soldOut: false,
    tag: "organic",
  },
  {
    name: "Pizza Margherita",
    type: "Pizza",
    ingredients: "Tomato and mozarella",
    price: 10,
    photoName: "pizzas/margherita.jpg",
    soldOut: false,
    tag: "vegetarian"
  },
  {
    name: "Pizza Spinaci",
    type: "Pizza",
    ingredients: "Tomato, mozarella, spinach, and ricotta cheese",
    price: 12,
    photoName: "pizzas/spinaci.jpg",
    soldOut: false,
    tag: "hot"
  },
  {
    name: "Pizza Funghi",
    type: "Pizza",
    ingredients: "Tomato, mozarella, mushrooms, and onion",
    price: 12,
    photoName: "pizzas/funghi.jpg",
    soldOut: false,
    tag: "vegetarian"
  },
  {
    name: "Pizza Salamino",
    type: "Pizza",
    ingredients: "Tomato, mozarella, and pepperoni",
    price: 15,
    photoName: "pizzas/salamino.jpg",
    soldOut: true,
    tag: null
  },
  {
    name: "Pizza Prosciutto",
    type: "Pizza",
    ingredients: "Tomato, mozarella, ham, aragula, and burrata cheese",
    price: 18,
    photoName: "pizzas/prosciutto.jpg",
    soldOut: false,
    tag: null
  }
]


function App() {
  return (
      <>
        <Header/>
        <Menu/>
        <Footer/>
      </>
  )
}

function Header() {
  return (<header className="header">
        <h1>Menu</h1>
      </header>
  )

}
function Menu() {
  const items = menuData

  return (
      <main className='menu'>
        <h2>Our food is made with love</h2>

        <ul>
          {items.map((item) => <Item itemObj={item} key={item.name}/>)}
        </ul>
      </main>
  )
}

function Item({itemObj}) {
  function getColor(tag) {
    if (tag === "organic") {
      return 'green';
    }
    if (tag === "vegetarian") {
      return 'lightgreen';
    }
    if (tag === "hot") {
      return 'red';
    }

  }

  return (
      <li>
        <img src={itemObj.photoName} alt={itemObj.name}></img>
        <span>{itemObj.name}</span>
        <span>{itemObj.ingredients}</span>
        <span style={{backgroundColor: getColor(itemObj.tag)}}>{itemObj.tag}</span>
      </li>
  )

}

function Footer() {
  return (
      <footer className="footer">
        <div className='order'>
          {new Date().toLocaleDateString()} We're currently open
        </div>
        <button className='btn'>Order</button>
      </footer>

  )
}


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <React.StrictMode>
      <App/>
    </React.StrictMode>
);

