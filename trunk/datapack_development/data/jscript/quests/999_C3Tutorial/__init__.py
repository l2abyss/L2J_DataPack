# Maked by Mr. Have fun! Version 0.2
print "importing quests: 999: C3 Tutorial"
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

VOUCHER_OF_FLAME_ID = 1496
SOULSHOOT_NOVICE_ID = 5789
BLUE_GEM_ID=6353

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "7573_02" :
#      st.showRadar(2,-56736,-113680,-672)
      htmltext = "7573-03.htm"
      if st.getQuestItemsCount(VOUCHER_OF_FLAME_ID) and int(st.get("onlyone")) == 0 :
        st.addExpAndSp(0,50)
        st.takeItems(VOUCHER_OF_FLAME_ID,1)
        st.giveItems(SOULSHOOT_NOVICE_ID,200)
        st.set("cond","0")
        st.set("onlyone","1")
        st.setState(COMPLETED)
        st.playSound("ItemSound.quest_finish")
    return htmltext


 def onTalk (Self,npcId,st):
   htmltext = "<html><head><body>I have no tasks for you right now.</body></html>"
   id = st.getState()
   if id == CREATED :
     st.setState(STARTING)
     st.set("cond","0")
     st.set("onlyone","0")
     st.set("id","0")
   if (npcId == 7573 or npcId == 7575) and int(st.get("onlyone")) == 0 and int(st.get("cond")) == 0 and st.getPlayer().getLevel() < 10 and st.getPlayer().getRace().ordinal() == 3 :
	if npcId == 7573 :
          htmltext = "7573-01.htm"
	if npcId == 7575 :
          htmltext = "7575-01.htm"
          st.set("cond","1")
          st.setState(STARTED)
          st.playSound("ItemSound.quest_tutorial")
   elif st.getPlayer().getLevel() >= 10 or int(st.get("onlyone")):
	if npcId == 7575 :
          htmltext = "7575-05.htm"
   elif npcId == 7575 and int(st.get("cond"))==1 and st.getQuestItemsCount(VOUCHER_OF_FLAME_ID)==0 :
      if st.getQuestItemsCount(BLUE_GEM_ID) :
          st.takeItems(BLUE_GEM_ID,st.getQuestItemsCount(BLUE_GEM_ID))
          st.giveItems(VOUCHER_OF_FLAME_ID,1)
          st.giveItems(SOULSHOOT_NOVICE_ID,200)
          htmltext = "7575-03.htm"
          st.set("cond","2")
      else :
          htmltext = "7575-02.htm"
   elif npcId == 7575 and int(st.get("cond"))==2 and st.getQuestItemsCount(VOUCHER_OF_FLAME_ID) :
      htmltext = "7575-04.htm"
   elif npcId == 7573 and  int(st.get("cond"))==1 :
      htmltext = "7573-01.htm"
   elif npcId == 7573 and  int(st.get("cond"))==2 and st.getQuestItemsCount(VOUCHER_OF_FLAME_ID) :
      htmltext = "7573-02.htm"
   elif npcId == 7573 and  int(st.get("cond"))==3 :
      htmltext = "7573-04.htm"
   return htmltext

 def onKill (self,npcId,st):
   if npcId == 5198 :
      if int(st.get("cond"))==1 and st.getRandom(100) < 70 :
        if st.getQuestItemsCount(BLUE_GEM_ID) == 0 :
            st.giveItems(BLUE_GEM_ID,1)
            st.playSound("ItemSound.quest_itemget")
            st.playSound("ItemSound.quest_tutorial")
   return

QUEST       = Quest(999,"999_C3Tutorial","C3 Tutorial")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(7573)
QUEST.addStartNpc(7575)

STARTED.addTalkId(7573)
STARTED.addTalkId(7575)

STARTED.addKillId(5198)

STARTED.addQuestDrop(5198,BLUE_CRYSTAL,1)
STARTED.addQuestDrop(7575,VOUCHER_OF_FLAME_ID,1)
