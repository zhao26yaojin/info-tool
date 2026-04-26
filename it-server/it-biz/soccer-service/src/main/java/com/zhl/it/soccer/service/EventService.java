package com.zhl.it.soccer.service;

import com.zhl.it.soccer.model.entity.FbEvent;
import com.zhl.it.soccer.model.qo.EventQO;
import com.zhl.it.soccer.model.vo.EventVO;

import java.util.List;

public interface EventService {

    List<FbEvent> selectList(EventQO qo);

    List<EventVO> selectVOList(EventQO qo);
}
