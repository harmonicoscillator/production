source /afs/cern.ch/cms/LCG/LCG-2/UI/cms_ui_env.sh
voms-proxy-init --valid 168:00 -voms cms
voms-proxy-info --all
source /afs/cern.ch/cms/cmsset_default.sh
source /afs/cern.ch/cms/ccs/wm/scripts/Crab/crab.sh
#echo "WARN: Make sure you have your sourced a CMSSW env before submitting crab jobs."

cd /afs/cern.ch/user/r/richard/PRODUCTION/CMSSW_5_3_20 && cmsenv && cd -
echo set /afs/cern.ch/user/r/richard/PRODUCTION/CMSSW_5_3_20 env
