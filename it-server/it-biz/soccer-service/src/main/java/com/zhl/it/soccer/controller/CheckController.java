package com.zhl.it.soccer.controller;

import com.zhl.it.util.rest.RestResponse;
import org.springframework.web.bind.annotation.GetMapping;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.http.HttpStatus;

@RestController
@RequestMapping("/support")
@Slf4j
public class CheckController {

    @GetMapping("check")
    public RestResponse<String> check(){
        return RestResponse.ok(HttpStatus.OK.getReasonPhrase());
    }

}