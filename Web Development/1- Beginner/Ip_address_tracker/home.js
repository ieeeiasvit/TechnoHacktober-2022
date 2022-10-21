window.onload = () =>{
    track();
    var mymap;
}
const track = () => 
{
    var data = {
        "ipAddress":document.getElementById("inputIp").value,
        "apiKey":"at_caMw5V6rzmdlMKcMNKDFJWaiSPbHm"
    };
     console.log(data) 
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("readystatechange", function() 
        {
            if(this.readyState === 4) 
            {
                if(this.status==200 || this.status==201)
                {
                        let newData = JSON.parse(this.responseText)                    
                        console.log(newData);
                        document.getElementById("ipAddress").innerHTML=newData["ip"];
                        document.getElementById("location").innerHTML='<div>'+newData["location"]["city"]+',</div><div>'+newData["location"]["region"]+',</div><div>'+newData["location"]["country"]+'</div>';
                        document.getElementById("timezone").innerHTML=newData["location"]["timezone"];
                        document.getElementById("isp").innerHTML=newData["isp"];
                        mymap = L.map('mapid').setView([newData["location"]["lat"], newData["location"]["lng"]], 13);
                        L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicGVsdGFzdGljIiwiYSI6ImNrZmlvcW5qdTBlZzMyem9kNWdya2J3MXUifQ.FtqkSaFMf4zmPAJTeiIAXQ', {
                            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                            maxZoom: 18,
                            id: 'mapbox/streets-v11',
                            tileSize: 512,
                            zoomOffset: -1,
                            accessToken: 'pk.eyJ1IjoicGVsdGFzdGljIiwiYSI6ImNrZmlvcW5qdTBlZzMyem9kNWdya2J3MXUifQ.FtqkSaFMf4zmPAJTeiIAXQ'
                        }).addTo(mymap);
                        var marker = new L.marker([newData["location"]["lat"], newData["location"]["lng"]],).addTo(mymap);
                }
                else{
                    alert("invalid IP");
                }
            }
        });
        xhr.open("GET","https://geo.ipify.org/api/v1?apiKey=at_caMw5V6rzmdlMKcMNKDFJWaiSPbHm&ipAddress="+data.ipAddress);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify(data));
        
        
}
const track2 = () => {
    var data = {
        "ipAddress":document.getElementById("inputIp").value,
        "apiKey":"at_caMw5V6rzmdlMKcMNKDFJWaiSPbHm"
    };
     console.log(data) 
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("readystatechange", function() 
        {
            if(this.readyState === 4) 
            {
                if(this.status==200 || this.status==201)
                {
                        let newData = JSON.parse(this.responseText)                    
                        console.log(newData);
                        document.getElementById("ipAddress").innerHTML=newData["ip"];
                        document.getElementById("location").innerHTML='<div>'+newData["location"]["city"]+',</div><div>'+newData["location"]["region"]+',</div><div>'+newData["location"]["country"]+'</div>';
                        document.getElementById("timezone").innerHTML=newData["location"]["timezone"];
                        document.getElementById("isp").innerHTML=newData["isp"];
                        mymap.setView([newData["location"]["lat"], newData["location"]["lng"]], 13);
                        var marker = new L.marker([newData["location"]["lat"], newData["location"]["lng"]],).addTo(mymap);
                }
                else{
                    alert("invalid IP");
                }
            }
        });
        xhr.open("GET","https://geo.ipify.org/api/v1?apiKey=at_caMw5V6rzmdlMKcMNKDFJWaiSPbHm&ipAddress="+data.ipAddress);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify(data));
}