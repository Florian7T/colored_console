# colored_console

This library can be used to add color to your console output. It works in all linux terminals and windows' new Terminal.
It uses byte combinations to determine color which I converted to a simple to use library

It should be used like this: print(color_console.red+"message"+color_console.end)
The library also includes a custom print function which will automatically add color_console.end at the end (color_console.end sets color back to default).
