import React from 'react'
import './Request.css'
import image from 'C:/Users/ASUS/Desktop/web-dev/PRACTISE/vistarr-work/src/Rakshit.png'


function Request() {
    return (
        <div className="box">
            
            <div className="profile">
                <img src={image} alt="profile-pic"></img>   
                <div className="Description">
                    <p><strong>NAME</strong></p>
                    <p>Designation</p>
                    <p id="Blue-color">500+ Connections</p>
                </div> 
            </div>

            <div className="Bar2">
                <button class="Accept acc" type="button">
                    Accept
                </button>
            
                <button class="Decline acc" type="button">
                    Decline
                </button>      
            </div>
        </div>
    )
}

export default Request
