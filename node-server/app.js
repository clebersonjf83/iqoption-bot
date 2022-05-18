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


        this.server.get("/clientes", async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            db.serialize(() => {
                db.all("SELECT * FROM clientes", (err, clientes) => {
                    console.log(clientes)
                    res.send(clientes)
                });
            });
        });

        this.server.post('/clientes', async function (req, res) {

            const db = new sqlite3.Database(__dirname + '/../database.db');
            let {status,nome,email,proximoPagamento} = req.body;
            const stmt = db.prepare("INSERT INTO clientes (status,nome,email,proximo_pagamento) VALUES ("+status+",'"+nome+"','"+email+"','"+proximoPagamento+"')");
            stmt.run()
            stmt.finalize();
            res.send()
        });


    }

}
module.exports = new App().server