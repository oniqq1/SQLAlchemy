from flask import render_template, request, redirect, url_for, abort
from app import app


@app.get("/")
def main():
    return render_template("main.html")
