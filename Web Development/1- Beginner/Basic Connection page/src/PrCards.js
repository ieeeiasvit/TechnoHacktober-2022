import React from 'react'
import './PrCards.css'
import image from 'C:/Users/ASUS/Desktop/web-dev/PRACTISE/vistarr-work/src/Rakshit.png'
import {useState} from 'react';
import CancelIcon from '@mui/icons-material/Cancel';



// import React, { Component } from 'react';
// import {  Animated, Text, TouchableOpacity, StyleSheet,Image, Dimensions, Platform,  UIManager } from 'react-native'



// const [state, setstate] = useState("CONNECT");
// const changeText=(text)=>setstate(text);
// return (
//     <Button onClick={() => changeText("Request Sent")}>{state}</Button>
//   )


// function generateUsers(amount) {
//     const users = [];
  
//     for (let i = 0; i < amount; i++) {
//       users.push({
//         name: faker.name.findName(),
//         description: faker.name.jobType(),
//         avatar: faker.image.avatar(),
//         id: faker.random.number(100)
//       });
//     }
  
//     return users;
//   }



function Cards(props) {
    


    const [state, setstate] = useState("CONNECT");
    const changeText=(text)=>setstate(text);

    // const handleClick = user => event => {
    //     const { users } = this.state;
    //     users.splice(users.indexOf(user), 1);
    
    //     this.setState({
    //       users
    //     });
    //   };
 

    return (
        <div className="Card">
          
            
            <iconbutton id ="Cancel" className="Cross" type="button" onClick={()=> props.removeCard(props.data.id)}>
                <CancelIcon />
            </iconbutton>



            <img src={image} alt="profile-pic" class="Ao"></img>
            <div className="names">
                <p>
                    <strong>{props.data.name}</strong>
                </p>
                <p>{props.data.workingPlace}</p>
            </div>
            <div className="Connections">
                <div calssName="number">
                    <p><strong>400</strong></p>
                    <p>Connections</p>
                </div>
            </div>
            <div className="Connect">
                
            <button className="connect" type="button" onClick={() => changeText("Request Sent")} >
                {state}
            </button>
            </div>      
        </div>      
    )
}



// render{
//     return(
//         <iconbutton id ="Cancel" className="Cross" type="button" onClick={this.handleClick(user)}>
//                 <CancelIcon />
//         </iconbutton>
//     )
// }


export default Cards



// { Data.map (post => {
//     return(
//       <div key={post.id}>
//         <h4>{post.name}</h4>
//         <p>{post.workingPlace}</p>

//       </div>
//     )
//   })}