
# Flask Image Gallery
This Flask application lets you publish a gallery of images from filesystem.

It can be useful if you wish to quickly look at images on your server or your own local machine. The application is "Simple by Design".

```
python app.py /path/to/your/root/directory/containing/images
```


<img src='assets/Screenshot 2020-07-09 at 1.07.18 AM.png'>
<img src='assets/Screenshot 2020-07-09 at 1.07.32 AM.png'>


If you wish to run it on a server you will need to port forward to your own `localhost` or you might use a tunnelling service like [ngrok](https://ngrok.com).


**Warning**: If deploying for production, use a production WSGI server such as [gunicorn](https://gunicorn.org).
