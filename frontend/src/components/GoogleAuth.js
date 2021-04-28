import React, { Component } from 'react'
import GoogleLogin from 'react-google-login'
 class GoogleAuth extends Component {

    responseGoogle=(response)=>{
        console.log(response)
        console.log(response.tc.id_token);
        //localStorage.setItem()
    }
    render() {
        return (
            <div>
               <GoogleLogin
               clientId='453293439718-hkqgoucgbauvjgnfq9rudappbra72inb.apps.googleusercontent.com'
               buttonText='Login'
               onFailur={this.responseGoogle}
               onSuccess={this.responseGoogle}
               cookiePolicy={'single_host_origin'}
               /> 
            </div>
        )
    }
}

export default GoogleAuth
