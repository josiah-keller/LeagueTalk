# LeagueTalk

Speech-to-text tool meant for chat in League of Legends. Inspired by [LeagueSpeak](https://github.com/MilesJuddPorter/leagueSpeak/) but with improvements.

## Easy Windows setup (non-developer)

0. Install Python by going to [python.org](https://python.org) and downloading/running the Windows installer. Make sure to choose the default installation that includes pip.
1. Download these files. Click the green "&lt;&gt; Code &darr;" button above, and choose "Download ZIP"
2. Extract the ZIP and copy the files somewhere sensible (ie, probably don't just leave them in your Downloads folder)
3. Install. Double-click the `install.bat` file
    - This just installs a few Python libraries
4. Run. Double-click the `start.bat` file

## Usage
LeagueTalk will bind to <kbd>G</kbd> as a hotkey to activate speech-to-text. It will listen for speech until you stop talking, convert to text, and then insert the text into the currently active program (hopefully your game). Before inserting the text, it will inject an <kbd>ENTER</kbd> keystroke to bring up the chat.

Unlike the original LeagueSpeak, LeagueTalk will not press <kbd>ENTER</kbd> a second time, allowing you to review the message before sending.