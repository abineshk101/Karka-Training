import http from 'http';
import  url  from 'url';
import path from 'path';
import fs from 'fs/promises';

const PORT=process.env.PORT;

const __filename=url.fileURLToPath(import.meta.url);
const __dirname=path.dirname(__filename);

const server = http.createServer(async(req,res)=>{
    try{
        if (req.method==='GET'){
            let filepath;
            if (req.url==='/'){
                filepath=path.join(__dirname,'public','index.html')
            }else if(req.url==='/about'){
                filepath=path.join(__dirname,'public','about.html')
            }else{
                throw new Error("404 Error, Page not found")
            };
            const data=await fs.readFile(filepath)
            res.setHeader('Content-Type','text/html');
            res.write(data);
            res.end()
        }else{
            throw new  Error("Method is invalid")
        }
    }catch(error){
        res.writeHead(400,{'Content-Type':'text/html'})
        res.end('<h1>Bad Request</h1>')
    }
})

server.listen(PORT,()=>{console.log(`The server running on ${PORT}`)})