const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const sqlite3 = require('sqlite3').verbose();

class App {

    constructor() {
        this.server = express();
        this.server.use(bodyParser.json());
        this.server.use(bodyParser.urlencoded({ extended: true }));
        this.server.use(cors({ credentials: true }));

        this.middlewares();
        this.routes();
    }

    middlewares() {

    }

    routes() {
        // Cadastros

        this.server.post("/autenticacao", async function (req, res) {
            const db = new sqlite3.Database(__dirname + '/../database.db');
            db.serialize(() => {
                db.all("SELECT * FROM clientes where email = '" + req.body.email + "' and senha = '" + req.body.senha + "'", (err, clientes) => {
                    if(clientes.length > 0)
                        res.send({status:clientes[0].status})
                    else
                        res.send({status:0})
                });
            });
        })

        this.server.get("/clientes", async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            db.serialize(() => {
                db.all("SELECT * FROM clientes", (err, clientes) => {
                    res.send(clientes)
                });
            });
        });

        this.server.post('/clientes', async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            let { status, nome, email, proximoPagamento , whatsapp} = req.body;
            const stmt = db.prepare("INSERT INTO clientes (status,nome,email,whatsapp,proximo_pagamento) VALUES (" + status + ",'" + nome + "','" + email + "','"+whatsapp+"','" + proximoPagamento + "')");
            stmt.run()
            stmt.finalize();
            res.send()
        });

        this.server.post('/trocarsenha', async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            let {email, senha} = req.body;
            console.log( req.body)
            const stmt = db.prepare("update clientes set senha = '"+senha+"' where email = '" + email + "'");
            stmt.run()
            stmt.finalize();
            res.send()
        });

        this.server.post('/atualizaclientes', async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            let {id, status, nome, email, proximoPagamento , whatsapp} = req.body;
            console.log( req.body)
            const stmt = db.prepare("update clientes set status =" + status + ",nome = '"+nome+"',email = '"+email+"',whatsapp = '"+whatsapp+"',proximo_pagamento = '"+proximoPagamento+"' where id = " + id);
            stmt.run()
            stmt.finalize();
            res.send()
        });


    }

}
module.exports = new App().server