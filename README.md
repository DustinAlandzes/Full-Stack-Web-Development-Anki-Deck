# Full-Stack-Web-Development-Anki-Deck
Using https://github.com/Stvad/CrowdAnki to collaboratively create a deck for a webdev class

--- 
## To start working on the deck you need to

1. Install git on their machine.
2. Clone the repository you've created:

    ```
    git clone https://github.com/Stvad/DeckX.git
    ```

3. [Import the deck](#import).

If somebody **just wants to use the deck** you've uploaded to GitHub - they can [import decks directly from there](#import-from-github).

#### How to upload changes

When you or one of your collaborators want to upload changes you've made to the GitHub, you need to:

1. Get the latest changes from the GitHub:
   
    ```
    git pull
    ```
2. [Import the deck](#import) to combine changes you've made with the changes other people have made.
3. Export the deck the same directory where your repository is located so that export will overwrite media directory and JSON file in the repository. (As an alternative you can export it elsewhere and copy JSON file and media directory yourself to overwrite the ones that are in repository directory.)
4. Add the changes to the repository:

    ```
    git add *
    git commit -m "new updates"
    ```
5. Upload changes you've made to the GitHub:

    ```
    git push origin master
    ```

If you just want to **get latest changes from other people** - you need to perform only steps 1 and 2.


## Generic collaboration workflow
The current workflow could be described as following:
* The user creates or imports an Anki deck.
* He makes some modification to it (i.e. to notes, deck settings, deck structure or note models).
* Then the user can export the deck in JSON format (accompanied by media directory with media files used in that deck) and share it with other users. For example by creating GitHub repository with it.
* Other people then can either modify JSON directly or import the deck to their instance of Anki and then make some modifications to it.
* Original JSON then can be updated the with the changes, these people made (merging several changes together if necessary).
* After that original user (and other people) can import updated deck to integrate these new changes into their collection.

## Export
To perform the export go to menu `File > Export`

Select the deck and the export format "CrowdAnki JSON representation".
After pressing the Export button - select directory where the result should be stored.

### Limitations:
* CrowdAnki won't allow you to do export of "All decks", you should use CrowdAnki snapshot instead.   
* Export of a filtered deck is not supported, export the main deck instead and filter it again after importing. You don't have to delete existing filtered decks, as all cards are still part of the main deck. When exporting nested decks, filtered sub-decks are just ignored.

## Import
To perform the import go to menu `File > CrowdAnki: Import from disk` and select the directory where the deck is stored.

## Import from GitHub
To get the deck from GitHub go to menu `File > CrowdAnki: Import from GitHub` and enter GitHub username and repository name in suggested format.

So, for example, to get my [git deck](https://github.com/Stvad/Software_Engineering__git) you would need to enter Stvad/Software_Engineering__git.

### Things to note for the Import:
* Automatic backup would be triggered prior to the import;
* If note model for the note has changed, or if note model itself changed in a way that it's not easy to update it automatically: you would be prompted with the window, that will ask you to specify correspondence between old and new model;
* If the note was moved to another deck in JSON file, on import all cards from that note (except the ones, that are in dynamic decks) will be moved to the specified deck.
