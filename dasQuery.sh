#/bin/sh

files="/HIHighPt/HIRun2011-v1/RAW#11f9188c-170b-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#8e362d22-0cde-11e1-b764-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#8f074d1e-0e0d-11e1-9b6c-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#a21ee5d4-174e-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#a5361d28-0f47-11e1-9b6c-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#a58be658-188a-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#ab6b53c2-1cc9-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#af7f713a-1ed8-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#b2d41a26-19af-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#b401b8dc-0d0b-11e1-b764-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#bb0dfbaa-1cb4-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#bbbfc6fa-1cf0-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#be6f935a-1285-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#c11d0c3a-119b-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#c2e449fc-19ac-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#c3226156-1bd2-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#c51f5934-1d83-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#c8823ad2-11e5-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#ca4ef73a-1ef9-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#ce11e808-1082-11e1-9b6c-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#d912f7e0-0f35-11e1-9b6c-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#db0f5a2c-14f6-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#dc8d049c-180e-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#dd284704-1d4a-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#e07ee1aa-1c60-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#e630a73c-0f4a-11e1-9b6c-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#e884d1fa-1f00-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#ece0554a-129d-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#f1d4cf38-1ecb-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#f3e1c16e-1fa2-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#f87f5536-1bb2-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#fdf436c8-1d8b-11e1-9f13-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#fe36e132-1398-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#fe799806-1398-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#febae1e2-1179-11e1-b723-003048caaace \
/HIHighPt/HIRun2011-v1/RAW#fede0b7a-0f3c-11e1-9b6c-003048caaace"

for file in $files
do
    python ./das_client.py --format=plain --limit=0 --das-headers --query="run block=${file}"
    python ./das_client.py --format=plain --limit=0 --das-headers --query="lumi block=${file}"
done
