import React from 'react'

export default function Header() {
  React.useEffect(() => {
    document.addEventListener('click', function (event) {
      if (event.target.tagName === 'A') {
        event.preventDefault();
        const targetSection = event.target.getAttribute('href').substring(1);
        console.log(targetSection)

        // Scroll to the target section
        const element = document.getElementById(targetSection)
        if(element) {
          element.scrollIntoView({
            behavior: 'smooth'
          });
        }
      }
    });
  }, []);

  return <div className="header">
    <h1>ALLENS </h1>
    <p><i>Reverse Image Search</i></p>
    <div className="menu">
      <a href="#home">Home</a>
      <a href="#how">How to Use</a>
      <a href="#concepts">Basic Concepts</a>
      <a href="#about">About Us</a>
    </div>
  </div>
}