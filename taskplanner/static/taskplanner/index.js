// Code for Integrated signin and login toggle  
document.addEventListener("DOMContentLoaded", ()=>{
    // Sign In and Sign Up toggle 
    const signupform = document.querySelector('.signupform');
    const loginform = document.querySelector('.loginform');
    var signup =document.getElementById("signupform");
    var login = document.getElementById("loginform");
    if (!signup&&login) { 
        signup.onclick = function(){
            signupform.style["display"] = "flex";
            loginform.style["display"] = "none";
            signup.className = "btn btn-info";
            login.className = "btn btn-secondary";
            }
            
        login.onclick = function(){
            signupform.style["display"] = "none";
            loginform.style["display"] = "flex";
            signup.className = "btn btn-secondary";
            login.className = "btn btn-info";
        }   
    }

    }
)