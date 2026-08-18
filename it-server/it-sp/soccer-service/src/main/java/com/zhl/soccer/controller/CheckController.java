package com.zhl.soccer.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.zhl.utils.rest.RestResponse;
import lombok.extern.slf4j.Slf4j;
import java.lang.String;

@RestController
@RequestMapping("/support")
@Slf4j
public class CheckController {

	@GetMapping("check")
	public RestResponse<String> check(){
		return RestResponse.ok(HttpStatus.OK.getReasonPhrase());
	}

}