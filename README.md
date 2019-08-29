# video-slate-splitter
[video-slate-splitter](https://github.com/nriebesehl/video-slate-splitter) is a realllllly quick and dirty script to split up an archive video tape with slates in between each item into clips based on each item using poor-man's optical detection.

## Requirements
* FFmpeg
* Python3
* Lots of file footage
* Suspension of Disbelief

##  Usage
1. Capture an entire video tape into one big, long, unwieldy file.
2. Save a still image of the frame before the first frame of real video to compare against. Make sure it is the same dimensions as the video file. 
3. With the shell script and the Python script in the same folder, run the following:
```
./splitter.sh [VIDEO FILE PATH] [SLATE IMAGE PATH]
```
It will look like nothing is happening, but FFmpeg will compare the video file frame-by-frame to the slate reference image using a difference filter and checking for "black" video.
FFmpeg will generate a list of the "black" sections, their start times, end times, and durations. 
Then, the Python script takes those time indices, turns them inside-out and generates an FFmpeg command for each chunk of video and transcodes all the chunks! 

## Development
To-do:
 - Specify transcoding params using command line argument
 - Add Blackmagic VTR control to ingest entire tape and then run script.
 - Add basic content recognition and audio transcription 




### SOFTWARE LICENSE:
(C) 2019 
>Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
>
>The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
>
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.