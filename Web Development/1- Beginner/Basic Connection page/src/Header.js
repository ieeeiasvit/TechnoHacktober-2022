import React from 'react'
import './Header.css'
import SearchIcon from '@mui/icons-material/Search';

function header() {
    return (
        <div className='header'>
            <div className="header_left">
                <img src="" alt="app-icon"/>
                <div className="header_search">
                    <SearchIcon />
                    <input type="text" size="70" placeholder="search" />
                </div>
            </div>  
        </div>
    )
}

export default header
