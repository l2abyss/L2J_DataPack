/*
 * Copyright (C) 2004-2013 L2J DataPack
 * 
 * This file is part of L2J DataPack.
 * 
 * L2J DataPack is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * L2J DataPack is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
 * General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */
package handlers.effecthandlers;

import java.util.List;

import com.l2jserver.gameserver.model.effects.EffectTemplate;
import com.l2jserver.gameserver.model.effects.L2Effect;
import com.l2jserver.gameserver.model.effects.L2EffectType;
import com.l2jserver.gameserver.model.stats.Env;
import com.l2jserver.gameserver.model.stats.Formulas;
import com.l2jserver.gameserver.network.SystemMessageId;
import com.l2jserver.gameserver.network.serverpackets.SystemMessage;

/**
 * Steal Abnormal effect implementation.
 * @author Adry_85, Zoey76
 */
public class StealAbnormal extends L2Effect
{
	private final String _slot;
	private final int _rate;
	private final int _max;
	
	public StealAbnormal(Env env, EffectTemplate template)
	{
		super(env, template);
		_slot = template.getParameters().getString("slot", null);
		_rate = template.getParameters().getInteger("rate", 0);
		_max = template.getParameters().getInteger("max", 0);
	}
	
	@Override
	public L2EffectType getEffectType()
	{
		return L2EffectType.NONE;
	}
	
	@Override
	public boolean isInstant()
	{
		return true;
	}
	
	@Override
	public boolean onStart()
	{
		if ((getEffected() != null) && getEffected().isPlayer() && (getEffector() != getEffected()))
		{
			final List<L2Effect> toSteal = Formulas.calcCancelStealEffects(getEffector(), getEffected(), getSkill(), _slot, _rate, _max);
			if (toSteal.isEmpty())
			{
				return false;
			}
			final Env env = new Env();
			env.setCharacter(getEffected());
			env.setTarget(getEffector());
			for (L2Effect eff : toSteal)
			{
				env.setSkill(eff.getSkill());
				final L2Effect effect = eff.getEffectTemplate().getStolenEffect(env, eff);
				if (effect != null)
				{
					effect.scheduleEffect();
					if (effect.isIconDisplay() && getEffector().isPlayer())
					{
						final SystemMessage sm = SystemMessage.getSystemMessage(SystemMessageId.YOU_FEEL_S1_EFFECT);
						sm.addSkillName(effect);
						getEffector().sendPacket(sm);
					}
					getEffector().getEffectList().add(effect);
				}
				eff.exit();
			}
			return true;
		}
		return false;
	}
}