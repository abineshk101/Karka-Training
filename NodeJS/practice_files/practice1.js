import http from 'http'
const PORT=process.env.PORT;

const server = http.createServer((req,res)=>{
    try{
        if (req.method==='GET'){
            if (req.url==='/'){
                res.setHeader('Content-Type','text/html')
                res.end('<h1>HELLO WORLD!</h1>')    
            }else if(req.url==='/about'){
                res.writeHead(400,{'Content-Type':'application/json'})
                res.end(JSON.stringify({
                    message:'about page',
                    status:400
                }))
            }else{
                res.writeHead(404,{'Content-Type':'text/html'})
                res.end('<h1>error occured</h1>')
            };
        }else{
            throw new  Error("Method is invalid")
        }
    }catch(error){
        res.writeHead(404,{'Content-Type':'text/plain'})
        res.end('server error')
    }
})

server.listen(PORT,()=>{console.log(`The server running on ${PORT}`)})