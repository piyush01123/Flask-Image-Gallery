
# Flask Image Gallery

A Flask application that lets you quickly publish and view a gallery of images from a filesystem.

<img src='assets/screenshot.png'>


It can be useful if you wish to quickly look at images on your server or your own local machine.

The application is "Simple by Design".

### Run application
The preferred way to use is by Docker. If you have docker installed and you wish to view images on say `/home/piyush/Pictures` directory, you can issue following command and then browse `localhost:6006`. Change this to your preferred directory path.
```
docker run -it -p 0.0.0.0:6006:5000/tcp -v /home/piyush/Pictures:/imgdir:ro piyush01123/flaskig python app.py /imgdir -l 0.0.0.0 -p 5000
```


2nd way is to clone this repo, install `flask` and run `app.py`:
```
python app.py /path/to/your/root/directory/containing/images
```

If you wish to run it on a server and view the gallery on your own system then you might want to [port forward](https://www.ssh.com/ssh/tunneling/example) to your local system's IP or you might use a tunnelling service like [ngrok](https://ngrok.com) or [pagekite](https://pagekite.net/).
