let m=document.getElementById('timeclock');
console.log(m);
function timechange(n){

    if(n===1)
    {
        m.src="../static/images/6am.svg";
    }

    
    if(n===2)
    {
        m.src="../static/images/7am.svg";
    }

    
    if(n===3)
    {
        m.src="../static/images/8am.svg";
    }

    
    if(n===4)
    {
        m.src="../static/images/9am.svg";
    }
}
