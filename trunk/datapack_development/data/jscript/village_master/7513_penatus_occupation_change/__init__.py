#
# Created by DraX on 2005.08.21
#

print "importing village master data: Tower of Aden          ...done"

import sys

from net.sf.l2j.gameserver.model.quest        import State
from net.sf.l2j.gameserver.model.quest        import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

MARK_OF_CHALLENGER_ID   = 2627
MARK_OF_PILGRIM_ID      = 2721
MARK_OF_DUELIST_ID      = 2762
MARK_OF_WARSPIRIT_ID    = 2879
MARK_OF_GLORY_ID        = 3203
MARK_OF_CHAMPION_ID     = 3276
MARK_OF_LORD_ID         = 3390 
HIGH_PREFECT_PENATUS    = 7513
HIGH_PREFECT_KARIA      = 7681
HIGH_PREFECT_GARVARENTZ = 7704
HIGH_PREFECT_LADANZA    = 7865
HIGH_PREFECT_TUSHKU     = 7913

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st):
   
   htmltext = event
   Race     = st.getPlayer().getRace()
   ClassId  = st.getPlayer().getClassId()
   Level    = st.getPlayer().getLevel()

   if event == "7513-01.htm":
     st.exitQuest(True)
     return "7513-01.htm"

   if event == "7513-02.htm":
     st.exitQuest(True)
     return "7513-02.htm"

   if event == "7513-03.htm":
     st.exitQuest(True)
     return "7513-03.htm"

   if event == "7513-04.htm":
     st.exitQuest(True)
     return "7513-04.htm"

   if event == "7513-05.htm":
     st.exitQuest(True)
     return "7513-05.htm"

   if event == "7513-06.htm":
     st.exitQuest(True)
     return "7513-06.htm"

   if event == "7513-07.htm":
     st.exitQuest(True)
     return "7513-07.htm"

   if event == "7513-08.htm":
     st.exitQuest(True)
     return "7513-08.htm"

   if event == "7513-09.htm":
     st.exitQuest(True)
     return "7513-09.htm"

   if event == "7513-10.htm":
     st.exitQuest(True)
     return "7513-10.htm"

   if event == "7513-11.htm":
     st.exitQuest(True)
     return "7513-11.htm"

   if event == "7513-12.htm":
     st.exitQuest(True)
     return "7513-12.htm"

   if event == "7513-13.htm":
     st.exitQuest(True)
     return "7513-13.htm"

   if event == "7513-14.htm":
     st.exitQuest(True)
     return "7513-14.htm"

   if event == "7513-15.htm":
     st.exitQuest(True)
     return "7513-15.htm"


   if event == "class_change_48":
     if ClassId in [ClassId.orcMonk]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_CHALLENGER_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_DUELIST_ID) == 0:
            st.exitQuest(True)
            return "7513-16.htm"
          else:
            st.exitQuest(True)
            return "7513-17.htm"
        elif Level >= 40:
          if st.getQuestItemsCount(MARK_OF_CHALLENGER_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_DUELIST_ID) == 0:
            st.exitQuest(True)
            return "7513-18.htm"
          else:
            st.takeItems(MARK_OF_CHALLENGER_ID,1)
            st.takeItems(MARK_OF_GLORY_ID,1)
            st.takeItems(MARK_OF_DUELIST_ID,1)
            st.player.setClassId(48)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(True)
            return "7513-19.htm"


   if event == "class_change_46":
     if ClassId in [ClassId.orcRaider]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_CHALLENGER_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_CHAMPION_ID) == 0:
            st.exitQuest(True)
            return "7513-20.htm"
          else:
            st.exitQuest(True)
            return "7513-21.htm"
        elif Level >= 40:
          if st.getQuestItemsCount(MARK_OF_CHALLENGER_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_CHAMPION_ID) == 0:
            st.exitQuest(True)
            return "7513-22.htm"
          else:
            st.takeItems(MARK_OF_CHALLENGER_ID,1)
            st.takeItems(MARK_OF_GLORY_ID,1)
            st.takeItems(MARK_OF_CHAMPION_ID,1)
            st.player.setClassId(46)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(True)
            return "7513-23.htm"


   if event == "class_change_51":
     if ClassId in [ClassId.orcShaman]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_PILGRIM_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_LORD_ID) == 0:
            st.exitQuest(True)
            return "7513-24.htm"
          else:
            st.exitQuest(True)
            return "7513-25.htm"
        elif Level >= 40:
          if st.getQuestItemsCount(MARK_OF_PILGRIM_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_LORD_ID) == 0:
            st.exitQuest(True)
            return "7513-26.htm"
          else:
            st.takeItems(MARK_OF_PILGRIM_ID,1)
            st.takeItems(MARK_OF_GLORY_ID,1)
            st.takeItems(MARK_OF_LORD_ID,1)
            st.player.setClassId(51)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(True)
            return "7513-27.htm"


   if event == "class_change_52":
     if ClassId in [ClassId.orcShaman]:
        if Level <= 39:
          if st.getQuestItemsCount(MARK_OF_PILGRIM_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_WARSPIRIT_ID) == 0:
            st.exitQuest(True)
            return "7513-28.htm"
          else:
            st.exitQuest(True)
            return "7513-29.htm"
        elif Level >= 40:
          if st.getQuestItemsCount(MARK_OF_PILGRIM_ID) == 0 or st.getQuestItemsCount(MARK_OF_GLORY_ID) == 0 or st.getQuestItemsCount(MARK_OF_WARSPIRIT_ID) == 0:
            st.exitQuest(True)
            return "7513-30.htm"
          else:
            st.takeItems(MARK_OF_PILGRIM_ID,1)
            st.takeItems(MARK_OF_GLORY_ID,1)
            st.takeItems(MARK_OF_WARSPIRIT_ID,1)
            st.player.setClassId(52)
            st.player.broadcastUserInfo()
            st.playSound("ItemSound.quest_fanfare_2")
            st.exitQuest(True)
            return "7513-31.htm"


 def onTalk (Self,npcId,st):
   
   Race    = st.getPlayer().getRace()
   ClassId = st.getPlayer().getClassId()
   
   # orc�s got accepted
   if npcId == HIGH_PREFECT_PENATUS or HIGH_PREFECT_GARVARENTZ or HIGH_PREFECT_KARIA or HIGH_PREFECT_LADANZA or HIGH_PREFECT_TUSHKU and Race in [Race.orc]:
     if ClassId in [ClassId.orcMonk]:
       st.exitQuest(True)
       return "7513-01.htm"
     elif ClassId in [ClassId.orcRaider]:
       st.exitQuest(True)
       return "7513-05.htm"
     elif ClassId in [ClassId.orcShaman]:
       st.exitQuest(True)
       return "7513-09.htm"
     elif ClassId in [ClassId.destroyer, ClassId.tyrant, ClassId.overlord, ClassId.warcryer]:
       st.exitQuest(True)
       return "7513-32.htm"
     elif ClassId in [ClassId.orcFighter, ClassId.orcMage]:
       st.exitQuest(True)
       return "7513-33.htm"
     else:
       st.exitQuest(True)
       return "7513-34.htm"

   # All other Races must be out
   else:
     st.exitQuest(True)
     return "7513-34.htm"

QUEST   = Quest(7513,"7513_penatus_occupation_change","village_master")
CREATED = State('Start',QUEST)

QUEST.setInitialState(CREATED)

QUEST.addStartNpc(7513)
QUEST.addStartNpc(7681)
QUEST.addStartNpc(7704)
QUEST.addStartNpc(7865)
QUEST.addStartNpc(7913)

STARTED.addTalkId(7513)
STARTED.addTalkId(7681)
STARTED.addTalkId(7704)
STARTED.addTalkId(7865)
STARTED.addTalkId(7913)