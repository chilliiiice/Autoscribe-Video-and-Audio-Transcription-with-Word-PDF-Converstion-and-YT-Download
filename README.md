# FFmpeg Setup

**Prerequisite:** Make sure FFmpeg is installed. You can download it from:  
- [FFmpeg official builds](https://www.ffmpeg.org/download.html#build-windows)  
- [Gyan’s FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/)  

**Setup Instructions:**  
1. Extract the downloaded zip file to a location of your choice.  
2. Copy the path to the `bin` folder inside the extracted FFmpeg directory. Example:  "ffmpeg-master-latest-win64-gpl\bin"
3. Open **Edit System Environment Variables** via the Windows search bar.  
4. In the **System Properties** window, click **Environment Variables…**  
5. Under **System Variables**, find and select **Path**, then click **Edit → New**.  
6. Paste the copied `bin` folder path and click **OK** to save.  

After this, FFmpeg should be available in any command prompt or terminal. You can test by running:  
ffmpeg -version
