<div align="center">
    <h1>Logitech-Macro-Volume</h1>
    <i>The one and only Python script to use your Logitech Macro keys for changing the volume of programs!</i>
</div>

---

## About

For a long time now, I haven't found a way to use the Macro Keys of my Logitech G910 😢. I am always furious, when suddenly a song on Spotify is a lot louder than the previous one, or when there are some ads 😡 (and I don't want to tab out of a game to change that). This is how I found a use for those Macro Keys.  😎

## Usage

1. Download [changevol.pyw](./changevol.pyw)

2. Edit the function of a Macro to Shortcut and enter the following

```bash
pyw <path to changevol.pyw> -p <program> [-v <volume> | -m]
```

Now, save the set Macro and you now should be able to control your program's audio without having to tab out of your programs.

_That is, assuming you have python3 and [Logitech Gaming-Software](https://support.logi.com/hc/de/articles/360025298053-Logitech-Gaming-Software) installed on your system_

#### Arguments

| Shortarg     | Longarg             | Function                                            | Example    |
| ------------ | ------------------- | --------------------------------------------------- | ---------- |
| -p <Program> | --program=<program> | Which program should be targetted                   | -p Spotify |
| -v <vol>     | --volume=<vol>      | By which amount (max is 1) volume should be changed | -v -0.05   |
| -m           | --mute              | Toggle mute a program                               | -m         |

#### Example

To fix my Spotify Ad problem, I simply use 

`pyw changevol.pyw -p Spotify -m`

and

`pyw changevol.pyw -p Spotify -v 0.05 ` & `pyw changevol.pyw -p Spotify -v -0.05 ` 

This can of course be used with any other program, that may sometimes annoy you 😜

