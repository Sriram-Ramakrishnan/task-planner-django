// Code for Integrated signin and login toggle

document.addEventListener("DOMContentLoaded", ()=>{
    // Sign In and Sign Up toggle 
    const signupform = document.querySelector('.tableview');
    const loginform = document.querySelector('.soloview');
    var signup =document.getElementById("signupform");
    var login = document.getElementById("loginform");
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
)