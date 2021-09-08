# Sh!thead Card Game

## Development

This is all very much open for discussion and any fun or creative solutions. Let's over- optimize the fuck out of this from the start!

Read all new entries in `docs/` and use files here to share ideas and thoughts.

### Project Structure

Open to ideas here but I'll initialize the project with a skeleton structure something like below:

    .
    ├── docs
    ├── shithead
    │   ├── core
    │   │   ├── card.py
    │   │   ├── __init__.py
    │   │   └── utils.py
    │   ├── data
    │   │   └── __init__.py
    │   ├── resources
    │   ├── client.py
    │   ├── host.py
    │   └── __init__.py
    ├── tests
    │   └── __init__.py
    ├── Makefile
    ├── README.md
    └── requirements.txt

    6 directories, 11 files

#### Notes

I imagine once we move to GUI/Web based stuff we will have to restructure everything anyway but if we keep it clean and structured now that will be a lot easier.

All imports should be relative to the shithead directory to ensure easy importing within the project.

#### Directories

__common__: This should hold all core and game related objects/mechanisms/shared functions. This should stay 1 level deep with appropriate filenames to organize code structure.

__data__: This should hold all API and database interaction code mostly used by the host file server.

__resources__: This should hold source code related resources only i.e. game image files.

__others__: As of yet I can't think of any other needed directories although there certainly will be but this should be solid foundation to work from.

#### Files

__core__: Should contain all the required classes for creating a base game i.e Card, Dealer. At the moment I think this will be alright but maybe a switch to separate files for separate common components will be better suited.

__utils__: Any functions we end up creating that don't fit well inside a class or required elsewhere in the project. This file can become very messy very quickly so try to consider if it is a 'utility' or more specialised function.

__scripts__: I am imagining two distinct script files; a host script to run on a server, and a client script to be run by all players. Both scripts will need to share some source code but I foresee us being able to abstract most of the components that will be shared. These I think should replace the standard main.py entry point as we will have two distinct entry cases - hosting a game/server and running as a player.


### Project version timeline (Guestimates)
 * 0.0.xx - Project structure/version control systems/workflows clearly decided and outlined in this document. Some rough idea of tools/modules we will be using to build this game, although I think a pure python approach to start will be fun, how we will interact with a GUI and servers should be outlined first.

 * 0.1.xx - Boring part over, start work on creating our game components/classes/mechanisms. End goal here is some sort of terminal interaction that allows us to test initializing game variables and mechanics to see if we can manually run through a basic game. (Dealer.shuffle(), Dealer.next() etc.)

 * 0.2.xx - Now lets turn it into a game! (Sort of) Still all through single terminal interface just returning variables to stdout but have it play something like a hot-seat game. However as a player(s) you should be able to pick your starting cards and have some way of selecting what card to play on your turn. After running a single script a full game playthrough should be possible.

 * 0.3.xx - API and database stuff. Completed methods to call actions on a single 'server' instance as clients. Not sure how we will complete this yet but we will outline it before version 0.2 at least. Wont be run as a server, all localhost stuff at this point.

 * 0.4.x -> 0.5 - Big markers here. 0.5 should be the start of us being able to play a game with each other through the terminal on the same network with one of us running a hosting script! But no GUI.

 * 0.6.x -> 0.8.x - Let's attempt a GUI using whatever methods we outline at the start. Full game should be coming into shape now.

 * 0.9 - Optimizing and polishing up results. Stuff like animations, some style etc. should be added here.

 * 1.0 - We have a server running with client files, we have player profiles and game history, and anyone can create/connect to a game with our source files.
