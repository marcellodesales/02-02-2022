echo "##### Next times - Schedule"
echo ""
for TIME in $(python combinations.py | jq -r '.[]' | sed 's/.\{2\}/&:/g;s/:$//'); do
  echo "* ${TIME}"
done

echo ""
echo ""

for TIME in $(python combinations.py | jq -r '.[]' | sed 's/.\{2\}/&:/g;s/:$//'); do

  # wait until the current time matches a unique time
  while [ "${CURRENT}" != "${TIME}" ]; do
    # https://stackoverflow.com/questions/20361982/get-current-time-in-hours-and-minutes/20362063#20362063
    CURRENT=$(date +%H:%M:%S)

    # wait a couple of milliseconds
    # https://serverfault.com/questions/469247/how-do-i-sleep-for-a-millisecond-in-bash-or-ksh/469259#469259
    perl -e "select(undef,undef,undef,0.3);"

    # Now, it will break the time
    echo "Current time: 02/02/2022 at ${CURRENT}  Waiting for 02/02/2022 at ${TIME}"
  done

  HASH_TAG=$(echo ${TIME} | sed 's/://g')

  echo ""
  echo "########### Unique !!!!! ----"
  echo ""
  echo "* Will tweet at ${TIME}"

  echo ""
  MSG="This is the unique tweet at 02/02/2022 at ${TIME}. #02022022${HASH_TAG}"
  echo "\"${MSG}\""
  echo ""

  echo "Executing 'bash ./tweet.sh post ${MSG}'"
  echo ""

  bash ./tweet.sh post ${MSG}

done
