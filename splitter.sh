VIDEOFILE="$1"
SLATE="$2"

ffmpeg -i $VIDEOFILE -i $SLATE \
-an -filter_complex "blend=difference,blackdetect=d=0.6:pic_th=0.86:pix_th=0.28" -f null - 2>&1 | grep -o '].*' > tindex.temp

TOTALRUN=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEOFILE")

python3 generatestring.py "$VIDEOFILE" "$TOTALRUN"
CLIPNUM=$(wc -l "cmds.temp" | cut -f1 -d' ')

#echo $CLIPNUM
for run in $(seq 1 $CLIPNUM)
do
#	echo "HELLO"
#	echo $run
	$(awk NR==$run cmds.temp) 
done
mv "$VIDEOFILE" $(processed_"$VIDEOFILE")
#echo "$TOTALRUN"
