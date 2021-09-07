# Testing #

I'll try and outline a testing methodology here although I will require some help, looking at you @nx1, as I have literally never done proper testing.

## Unittest ##

Current implementation for simple tests is using the `unittest` inbuilt module. All test scripts can be placed inside of `/tests` with appropriate naming (i.e 'test_xclass.py' for <xclass> implementations).

To run all current tests run the following in the project root:
    
    python -m unittest discover

To run a specific test file:

    python -m unittest tests/[test_file.py]

For the time being this should suffice, but I would like to try and do things by the book when it comes to testing because as I said that's not been the case in any of my past projects.
