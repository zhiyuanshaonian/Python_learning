# Fiddler命令

### ?sometext 查找网址中包含某些字符的会话信息，如：    
```?abc``` 筛选会话列表中所有网址中包含abc字符串的会话信息

### size
```size>40000``` 选择请求响应大小大于40kb的会话  
```size>5k```选择请求响应大小小于5kb的会话  

### =status =method 选择响应状态为status或者请求方法为method的会话  
```=301``` 选择301重定向响应  
```=POST``` 选择POST方式的请求  

### @host 选择会话中域名包含host的会话，按Enter键可高亮所有匹配的结果  
```@msn.com```选择www.msn.com, login.msn.com等  

### bold 标记任何URL包含了目标字符串的后续请求
```bold /bar.aspx```  
```bold``` 调用不带任何参数的命令来清除上一设置

### bpafter 设置中断请求URI中包含指定字符串的响应，如：  
```bpafter www.baidu.com``` 只中断百度网站相应的响应，不会影响其他网站  
```bpafter``` 调用不带任何参数的命令来清除上一设置

### bps 中断与设置的状态代码匹配的响应
```bps 404```  
```bps``` 调用不带任何参数的命令来清除上一设置

### bpv or bpm 对指定的HTTP方法创建请求端点。设置此命令将请清除该命令的任何以前的值，不带参数调用它会禁用断点
```bpv POST```  
```bpv``` 调用不带任何参数的命令来清除上一设置

### bpu 对包含指定字符串的URI创建请求断点。设置此命令将清除该命令的任何以前的值，不带参数调用它会禁用断点
```bpu /myservice.asmx```  
```bpu``` 调用不带任何参数的命令来清除上一设置

### cls or clear 清空会话列表
```cls```

### dump 打包所有会话成zip文档到C:/ 
```dump```

### g or go 恢复所有设置了断点的响应 
```g```  

### help 打开Fiddler帮助网页
```help```

### hide 隐藏Fiddler界面，系统后台运行
```hide```

### urlreplace 用一个不同的字符串替换URL中任何字符串。设置此命令将清除该命令的任何以前的值，不带参数调用它，将取消更换
```urlreplace SeekStr ReplaceWithStr```  
```urlreplace``` 调用不带任何参数的命令来清除上一设置

### start 注册成为系统代理
```start``` 

### stop 取消注册为系统代理
```stop```

### show 从系统托盘中恢复Fiddler,从ExecAction.exe获取更多有用的触发规则
```show```

### select MIME 选择Content-Type头中包含指定字符串的响应，可用于选择文件格式等
```select image```  
```select css```  
```select htm```

### select HeaderOrFlag PartialValue 选择已命名的header或SessionFlag包含指定字符串的响应  
```select ui-comments slow```  
```select ui-bold *```  除非 * 符号在 \ 之前，否则 * 符号代表任意值  
```select ui-comments \*```  选择带有 * 符号的注释   
```select @Request.Accept html```  选择Accept为html的请求  
```select @Response.Set-Cookie domain``` 选择在域名设置Cookie的响应


### allbut or keeponly 隐藏Content-Type中包含了指定字符串的所有会话
```allbut xml```  
```allbut java```  

### quit 退出Fiddler
```quit```

### !dns hostname 进行目标域名DNS查找，并将结果显示在LOG选项上  
```!dns www.example.com```  
```!nslookup www.example.com```

### !listen PORT [CERTHOSTNAME] 在另一个端口增设一个监听器，选择安全的HTTPS证书
```1.!listen 8889```  
```2.!listen 4443 localhost```  
```3.!listen 444 secure.example.com```  

### select 选择所有相应类型content-type为指定类型的HTTP请求，如：  
```select css ``` 选择所有类型为css的会话信息    
```select html ``` 选择所有类型为html的会话信息    
```select image ``` 选择所有类型为image的会话信息    
