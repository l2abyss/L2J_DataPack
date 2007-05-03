#Made by Emperorc
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "613_ProveYourCourage_Varka"

#NPC
Ashas = 31377
Hekaton = 25299

#Quest Items
Hekaton_Head = 7240
Valor_Feather = 7229
Varka_Alliance_Three = 7223

def giveReward(st,npc):
    if st.getState() == STARTED :
        npcId = npc.getNpcId()
        cond = st.getInt("cond")
        if npcId == Hekaton :
            if st.getPlayer().isAlliedWithVarka() :
                if cond == 1:
                    if st.getPlayer().getAllianceWithVarkaKetra() == -3 and st.getQuestItemsCount(Varka_Alliance_Three) :
                        st.giveItems(Hekaton_Head,1)
                        st.set("cond","2")

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   htmltext = event
   if event == "31377-04.htm" :
       if st.getPlayer().getAllianceWithVarkaKetra() == -3 and st.getQuestItemsCount(Varka_Alliance_Three) :
            if st.getPlayer().getLevel() >= 75 :
                    st.set("cond","1")
                    st.setState(STARTED)
                    st.playSound("ItemSound.quest_accept")
                    htmltext = "31377-04.htm"
            else :
                htmltext = "31377-03.htm"
                st.exitQuest(1)
       else :
            htmltext = "31377-02.htm"
            st.exitQuest(1)
   elif event == "31377-07.htm" :
       st.takeItems(Hekaton_Head,-1)
       st.giveItems(Valor_Feather,1)
       st.addExpAndSp(10000,0)
       st.playSound("ItemSound.quest_finish")
       htmltext = "31377-07.htm"
       st.exitQuest(1)
   return htmltext

 def onTalk (self,npc,player):
    st = player.getQuestState(qn)
    htmltext = "<html><head><body>I have nothing to say you</body></html>"
    if st :
      npcId = npc.getNpcId()
      cond = st.getInt("cond")
      Head = st.getQuestItemsCount(Hekaton_Head)
      Valor = st.getQuestItemsCount(Valor_Feather)
      if npcId == Ashas :
          if Valor == 0 :
              if Head == 0:
                  if cond != 1 :
                      htmltext = "31377-01.htm"
                  else:
                      htmltext = "31377-06.htm"
              else :
                  htmltext = "31377-05.htm"
          #else:
              #htmltext="<html><head><body>This quest has already been completed</body></html>"
    return htmltext

 def onKill (self,npc,player):
    partyMember = self.getRandomPartyMemberState(player,STARTED)
    if not partyMember : return
    st = partyMember.getQuestState(qn)
    if st :
       giveReward(st,npc)
       party = st.getPlayer().getParty()
       if party :
           for player in party.getPartyMembers().toArray() :
               pst = player.getQuestState(qn)
               if pst :
                   giveReward(pst,npc)
    return

QUEST       = Quest(613,qn,"Prove Your Courage!")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(Ashas)

QUEST.addTalkId(Ashas)

STARTED.addQuestDrop(Hekaton,Hekaton_Head,1)

QUEST.addKillId(Hekaton)

print "importing quests: 613: Prove Your Courage! (Varka)" 
