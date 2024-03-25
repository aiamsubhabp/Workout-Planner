import { NavLink } from 'react-router-dom'
import React from 'react'
import './NavBar.css'

function NavBar(){
    return (
        <nav>
            <NavLink
                to = '/'
                className = 'nav-link'
            > TEST
            </NavLink>
        </nav>
    )
}

export default NavBar