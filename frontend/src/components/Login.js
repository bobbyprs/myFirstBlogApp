import React, { useState,useEffect,useContext } from 'react'
import {APIService} from '../APIService'
import {useCookies} from 'react-cookie'
import {useHistory} from 'react-router-dom'
import {Navigation} from './Navigation'
import {useForm} from 'react-hook-form'
import loginImg from '../../src/login.svg'
import ContextProvider from './ComponentC'
import GoogleAuth from './GoogleAuth'
import Card from "react-bootstrap/Card";







export default function Login () {
  const [username,setUsername] = useState('')
  const [password, setPassword] = useState('')
  // const [grant_type,setgrant_type]=useState('password')
  // const [client_id,setclient_id] =useState('ZT6UqOjnzvpOd1NDH7Ene7qBm1O2ihSWyrpeRWGg')
  // const [client_id,setclient_id] =useState('ZT6UqOjnzvpOd1NDH7Ene7qBm1O2ihSWyrpeRWGg')

  const [token , setToken,removeToken] = useCookies(['mytoken'])
  const {register,errors,handleSubmit} = useForm()
   const {uservalue,setUservalue}=useContext(ContextProvider)
  // const [message, setMessage] = useState();
  // let authname={username}
  let history =useHistory()
  // const{setUsername} = useContext(GlobalContext)
  useEffect(() =>{
    if(token['mytoken']){
      history.push('/articles/')
      console.log(['mytoken'])
    }
    
  },[token])
 

  
  
  const loginBtn = ()=>{
    setUservalue(username)
    localStorage.setItem('user',username)
    APIService.LoginUser({username,password})
     .then(res =>{
        if(res && res == 'Password incorrect'){
          removeToken('mytoken')
          alert('Password in correct')
          return undefined
        }
        else if(res && res == 'user name error'){
          removeToken('mytoken')
          alert('Invalid User name Password')
          return undefined
        }
        
        setToken('mytoken',res.token)
        
      })
      .catch(error =>{
        removeToken('mytoken')
      })
  
    }
    return (
     
        <div  className='App'>
          <Navigation/>       
      {/* <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Open Login page</button>
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header bg-secondary">
                <h5 class="modal-title text-light " id="exampleModalLabel">LOGIN</h5>
                <button type="button" class="btn btn-close" data-bs-dismiss="modal" aria-label="Close"><h4>X</h4></button>
              </div> */} 
              <div style={{marginLeft:'auto',marginRight:'auto',maxWidth:'500px',marginTop:'50px'}} className='container-sm'>
              <Card  className="focus mt-2 mb-2 shadow p-3  ">
              <Card.Body style={{backgroundColor:'#E5E5E5'}}>
                <Card.Title className="text-center text-secondary card-title">Login</Card.Title>
                <hr />
                <Card.Text className="card-text d-flex justify-content-start flex-column">
                <img src={loginImg}/>
             <form onSubmit={handleSubmit(loginBtn)}>
                        
                        <div className='modal-body' >          
                           <div class="form-group text-dark">
                               <label  class="form-label">Username</label>
                               <input name="login_Username" type="text" 
                               value ={username} onChange ={e =>setUsername(e.target.value)}
                               class="form-control"
                               ref={register({required:{value:true,message:'this is a required fied'}})}
                               ></input>
                               {errors.login_Username && (
                                 <span style ={{color:'red'}}>{errors.login_Username.message}</span>
                               )}
                           </div>
                           <div class="form-group text-dark">
                               <label>Password</label>
                               <input name="login_password" type="password" class="form-control"
                               value ={password} onChange ={e =>setPassword(e.target.value)}
                               ref={register({required:{value:true,message:'this is a required fied'}})}
                            />
                            {errors.login_password && (
                                 <span style ={{color:'red'}}>{errors.login_password.message}</span>
                               )}
                           </div>
                           <div class="mx-auto text-center">
                               <button type='submit'  class="btn btn-primary mb-4">login</button><br/>
                               <GoogleAuth/>
                           </div>
                           </div>
                          </form>
                </Card.Text>
              </Card.Body>
            </Card>
         
              
                   
                   
                   </div>
                 </div>
            //     </div>
        
            // </div> 
            
        )
    }



