## How to Add Application Shortcuts on Ubuntu Desktop

- Go to Files -> Other Location -> Computer -> usr -> share -> applications. Open terminal here

- Run the command sudo nano my_app.desktop (enter password when prompted)

- Paste(`shift + insert`) the below code in the window.

```
[Desktop Entry]
Version = 1.0
Type = Application
Terminal = false
Name = STS
Exec = /path/to/the/executable/file
Icon = /path/to/the/icon/to/show
Categories = Application;
```

- Save(`ctrl + o`) the file.

- Exit(`ctrl + x`) from the nano editor.
