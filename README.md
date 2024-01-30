# Typing Speed Test App

Simple application that allows users to check their typing speed. From a list of the most common English words it will generate a random sample of 120. When the user starts to type there are 60 seconds to complete the test.

## Getting Started
1. Clone the repository
<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>git clone https://github.com/tarintrader/Typing-Speed-Test.git
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="git clone https://github.com/Veluthil/Typing-Speed-Test-App.git" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>
  
2. Change directory into the project folder
3. Create virtual environment<br>

<div class="snippet-clipboard-content notranslate position-relative overflow-auto"><pre class="notranslate"><code>py -m venv venv
venv/Scripts/activate
</code></pre><div class="zeroclipboard-container">
    <clipboard-copy aria-label="Copy" class="ClipboardButton btn btn-invisible js-clipboard-copy m-2 p-0 tooltipped-no-delay d-flex flex-justify-center flex-items-center" data-copy-feedback="Copied!" data-tooltip-direction="w" value="py -m venv venv
venv/Scripts/activate" tabindex="0" role="button">
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-copy js-clipboard-copy-icon">
    <path d="M0 6.75C0 5.784.784 5 1.75 5h1.5a.75.75 0 0 1 0 1.5h-1.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-1.5a.75.75 0 0 1 1.5 0v1.5A1.75 1.75 0 0 1 9.25 16h-7.5A1.75 1.75 0 0 1 0 14.25Z"></path><path d="M5 1.75C5 .784 5.784 0 6.75 0h7.5C15.216 0 16 .784 16 1.75v7.5A1.75 1.75 0 0 1 14.25 11h-7.5A1.75 1.75 0 0 1 5 9.25Zm1.75-.25a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h7.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Z"></path>
</svg>
      <svg aria-hidden="true" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-check js-clipboard-check-icon color-fg-success d-none">
    <path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0Z"></path>
</svg>
    </clipboard-copy>
  </div></div>

  <p dir="auto">To get started, simply run the <code>main.py</code> file. The app will launch and display the starting screen:</p>
  
## Features
<br>
  <img width="533" alt="image" src="https://github.com/tarintrader/Typing-Speed-Test/assets/142015759/26be5a1d-8d65-4d91-b80f-9ff2e175ba51">
  <br>
  <br>
The cursor is automatically placed on the text entry. When you touch the first key the test will begin. From that moment on you have 60 seconds to write as many words as you can.

### Check Spelling 
<img width="533" alt="image" src="https://github.com/tarintrader/Typing-Speed-Test/assets/142015759/395ab3f5-ecfc-4774-8cf0-ec4ffed46363">
<br>
<br>
The app checks words one by one as you type. If there is any typing error the word will turn red. If there are no errors it will turn green. For the final calculation, only correctly written words will be taken into account.

### Final Score
<img width="533" alt="image" src="https://github.com/tarintrader/Typing-Speed-Test/assets/142015759/bbc3b968-0257-4050-8c55-18693a107d9d">
<br>
<br>
When the clock reaches zero, writing is disabled. The program shows the score obtained in CPM (Clicks per minute) and WPM (Words per minute).

### Repeat
<img width="533" alt="image" src="https://github.com/tarintrader/Typing-Speed-Test/assets/142015759/32d3d297-80dd-46b3-85ff-3ff16f3603b5">
<br>
<br>
If you wish, you can reset the test and try again. By pressing the "Restart" button, a new sample of random words is generated and the test time is reset. You just have to start writing to start again.
