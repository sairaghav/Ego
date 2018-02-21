Ego is a voice-controlled personal assistant for Windows powered by Google's Speech Recognition API.

It offers capabilities such as:
1. **Switch windows (Equivalent of Win+Tab):**
	The command 'switch windows' will display all opened windows. The required window can be chosen by the commands:
	- Windows 10: 'left'/'right'/'up'/'down' to choose the window and 'select' to focus it to the foreground
	- Windows 7: 'previous'/'next' to choose the window and 'select' to focus it to the foreground
		
	Saying 'escape' at any point after 'switch windows' will change the focus to the original window in the foreground.
	
2. **Play music (Play music from YouTube):**
	The command 'play music' will ask you for the song to be played. The song requested by the user will be played on YouTube. You can give other commands to Ego while the song is being played in the background.
	
3. **Search Google:**
	The command 'search' will ask you for the query to be searched. The requested keyword will then be searched in Google.
	
4. **Control volume:**
	The following commands can be used to control the volume:
	- increase volume
	- decrease volume
	- mute volume
	- unmute volume
	
5. **Take notes:**
	The command 'take notes' will record everything you say and store it in a text file. Once you are done with your notes, please say 'end of notes' to stop the recording.
	
6. **Basic navigation:**
	- Show desktop: 'Show desktop' command shows the desktop.
	- Close window: 'close window' command closes the window in the foreground.
	- Close tab: 'close tab' command closes the browser tab in focus.
	- New tab: 'new tab' command creates a new tab in the browser.
	- Restore tab: 'restore tab' command re-opens the recently closed tabs.
	- Next tab: 'next tab' command moves to the next tab.
	- Previous tab: 'previous tab' command moves to the next tab.
	
7. **Read news:**
	The command 'read news' will trigger the news reader module. The news headlines will be collected from Google News based on your query.
	- 'more'/'select' after a news headline will pause playback and open the link that displays the headline
	- 'pause'/'wait' will pause news playback
	- 'stop'/'exit' will stop news playback
	
8. **Read books:**
	The command 'read book' will trigger the reader module which will ask you for the book that you would like to read. Then it will search for the book and read it for you if found.
	- 'pause'/'wait' will pause playback
	- 'stop'/'exit' will stop playback

9. **Conversation mode:**
	Ask Ego any question you want and it will try to answer.
	
10. **Cast YouTube video to chromecast:**
	Any command starting with 'chromecast' will activate the chromecast module. All words after 'chromecast' will be taken as input to search YouTube for videos.
	- 'chromecast pause' will pause the playback
	- 'chromecast play' will resume the playback
	
Say 'exit' anytime to stop Ego.