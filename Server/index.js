

/* Mongo DB */
const mongoose = require('mongoose');
//const uri = "mongodb+srv://Phoo:EWAH1KnfoMHEj99s@test-db.s72ptka.mongodb.net/?retryWrites=true&w=majority";
const uri = "mongodb+srv://muchimapl:Mochi2010@gentikxpertdb.5egoknj.mongodb.net/?retryWrites=true&w=majority";
mongoose.connect(uri);
mongoose.pluralize(null);



/* Model */
const users = mongoose.model('users',{
    Username: String,
    Password: String,
    Email : String,
})

const sample = mongoose.model('sample_data',{
    instruction: String,
    input : String,
    output : String
})

const users_data = mongoose.model('users_data',{
    username:String,
    instruction: String,
    input : String,
    output : String
})


 /*End connect MongoDB */

const express = require("express");
const app = express();
const port = process.env.PORT || 8765;
const bodyparser = require("body-parser")
const jwt = require('jsonwebtoken')
const secretKey = 'HelloxD'

app.use(bodyparser.json());
app.use(bodyparser.urlencoded({ extended: false }))

app.get('/',(req,res) => {
    res.send("Hello world");
})



app.post('/API/Save_Story',async(req,res) =>{
    try{
        console.log(req.body)
        const save_user_data = new users_data({
            username:req.body.Username,
            instruction: req.body.instruction,
            input : req.body.input,
            output : req.body.output 
        })
        await save_user_data.save()
        res.status(200).send({
            status: "save succussful"
        })
    }
    catch{
        res.status(500).send({
            status: "save fail"
        })
    }
})


app.post('/API/load_story',async(req,res) =>{
    const user = req.body.Username
    try{
    const data = await users_data.find({
        Username: user
    })
    res.status(200).send(data,{
        response:200
    })
    }
    catch{
        res.status(500).send({
            response:500
        })
    }
})



app.post('/API/sample_data',async(req,res) =>{
    try{
        const topic = req.body.topic
        
        const data_sample = await sample.find({
            instruction: topic
        })
        const ran_number = Math.floor(Math.random() * data_sample.length - 1)
        console.log(ran_number)
        const data = data_sample[ran_number]
        data.code = 200;

        res.status(200).send({
            data,
            response:200
        })
    }
    catch{
        const data = {
            response : 500 
        }
        res.status(500).send(data)
    }
})




app.post('/API/create_users',async(req,res) => {
    
    const check = await users.findOne({
        Username : req.body.Username
      });
      if(check === null){
    console.log(user_info)
    try{
        const user = new users({
            Username: req.body.Username,
            Password: req.body.Password,
            Email : req.body.Email,
    
        });
        await user.save();
        res.status(200).send('successfully Register');    
        }catch{
            res.status(500).send('Error Registeration')
        }
      }
      else{
        res.status(201).send('This Username already Taken');
      }
})


app.post('/API/login',async(req,res) =>{
    const check = await users.findOne({
        Username : req.body.Username,
        Password: req.body.Password
      });
    if(check === null){
        res.status(201).send({
            response: 201
        });
    }
    else{
        const tokens = jwt.sign(req.body.Username + req.body.Password + Math.random(0,100000),secretKey)
        res.status(200).send({
            token : tokens,
            Username: req.body.Username,
            response: 200
            
        });
    }
})



app.listen(port,() => {
    console.log("Starting node.js");
}) 