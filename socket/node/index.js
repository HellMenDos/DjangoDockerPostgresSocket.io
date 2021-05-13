const express = require('express');
const axios = require('axios');

const app = express();

app.get('/socket', (req, res) => {
  res.send('Hello from Socket');
});

let server = app.listen(8888);

const io = require('socket.io')(server);



io.on('connection', client => {
  client.on('startChat',({user,room})=> {
    // Join to room
    client.join(room)
  })
  client.on('message',({user,room,message})=> {
    
    axios.post('http://server:8000/inserMessage/',{user,room,message}).then((js)=> {
      console.log(js)
      io.to(room).emit('send',{user,message})
    }).catch((er)=> {
      console.log(er)
    }) 
  })
  
});

