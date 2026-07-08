---
id: UNC@20.15.2@MMLCommand@CMP LICENSE
type: MMLCommand
name: CMP LICENSE（比较License）
nf: UNC
version: 20.15.2
verb: CMP
object_keyword: LICENSE
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- License管理
status: active
---

# CMP LICENSE（比较License）

## 功能

该命令用于比较系统运行的License与指定的License文件、或者任意两个License文件中的信息。

## 注意事项

当待比较的两个License相同，并且客户端上该命令的参数“显示相同记录” 选择“NO（否）”时，显示成功。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CMPTYPE | 比较类型 | 可选必选说明：必选参数。<br>参数含义：用于请求系统按照哪种比较类型来进行License比较。<br>取值范围：<br>- “RUNLIC(系统运行中的License和License文件)”：用于比较当前系统中运行的License和指定的License文件。<br>- “FILELIC(License文件之间)”：用于比较任意两个License文件。<br>默认值：无。<br>配置原则：无。 |
| FN | License<br>文件名称 | 可选必选说明：该参数在“<br>CMPTYPE<br>”配置为“<br>RUNLIC(系统运行中的License和License文件)<br>”时为条件必选参数。<br>参数含义：用于当比较类型选择“RUNLIC(系统运行中的License和License文件)”时，输入待比较的License文件名。<br>取值范围：长度为6~311的字符串。<br>文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：确认文件在License文件管理界面<br>存在。 |
| SRCFN | 第一个License文件名称 | 可选必选说明：该参数在“<br>CMPTYPE<br>”配置为“<br>FILELIC(License文件之间)<br>”时为条件必选参数。<br>参数含义：用于当比较类型选择“FILELIC(License文件之间)”时，输入第一个待比较的License文件名称。<br>取值范围：长度为6~311的字符串。<br>文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：确认文件在License文件管理界面存在。 |
| DESFN | 第二个License文件名称 | 可选必选说明：该参数在“<br>CMPTYPE<br>”配置为“<br>FILELIC(License文件之间)<br>”时为条件必选参数。<br>参数含义：用于当比较类型选择“FILELIC(License文件之间)”时，输入第二个待比较的License文件名称。<br>取值范围：长度为6~311的字符串。<br>文件名称必须以字母开头，可由字母、数字和下划线组成，下划线不能与后缀紧邻，文件名包含后缀的长度为6~311个字符，且后缀必须是dat、DAT、xml或XML。<br>默认值：无。<br>配置原则：确认文件在License文件管理界面存在。 |
| DSPTYPE | 显示相同记录 | 可选必选说明：该参数在“<br>CMPTYPE<br>”配置为“<br>RUNLIC(系统运行中的License和License文件)<br>”或“<br>FILELIC(License文件之间)<br>”时为条件必选参数。<br>参数含义：用于请求系统按照哪种类型来显示比较结果。<br>取值范围：<br>- “YES（是）”：用于请求系统将相同的控制项和不同的控制项都显示。<br>- “NO（否）”：用于请求系统只显示不同的控制项。<br>默认值：“NO（否）”。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LICENSE]] · 失效License（LICENSE）

## 使用实例

比较2.0版本License文件“license_20_1205.dat”和“license_19_1205.dat”：

```
%%CMP LICENSE: CMPTYPE=FILELIC, SRCFN="license_20_1205.dat", DESFN="license_19_1205.dat", DSPTYPE=YES;%% 
RETCODE = 0  操作成功  

License名称 
----------- 
第一个License文件名称  =  license_20_1205.dat 
第二个License文件名称  =  license_19_1205.dat 
(结果个数 = 1)  

基本信息比较结果 
----------------
控制项描述     第一个License的值                                    第二个License的值  
                                   
国家           India                                                India                                                 
运营商         LTE                                                  LTE                                                   
局点           htipl                                                htipl                                                 
创建者         haier Technologies Co., Ltd                          haier Technologies Co., Ltd                           
License序列号  LIC201909290XXXXX                                    LIC2019082406XXXXX                                     
创建时间       2015-01-01 10:30:00                                  2015-01-01 10:30:00                                   
产品           iXXXX                                                ioXXXX                                                  
设备序列号     0123456789                                           0123456789                                            
版本           V200R0XXXXXXXXXXX                                    V200R018C00XXXXX                                     
属性           DEMO, NULL, NULL, NULL, NULL, NULL                   DEMO, NULL, NULL, NULL, NULL, NULL                    
注释           Order XXXXXXXXXXXXXXXXXXXXXXXXXXX                    Order XXXXXXXXXXXXXX   
(结果个数 = 11)  

特征项比较结果 
-------------- 
特征项      控制项      控制项描述  第一个License的值                       第二个License的值 
                        
basic01     NULL        截止日期    2020-12-05                              2019-12-05                               
basic01     NULL        属性        DEMO, 2020-12-05, 60, NULL, NULL, NULL  DEMO, 2019-12-05, 60, NULL, NULL, NULL   
basic01     basicfun1   基本软件1   1000                                    1000                                     
basic01     basicfun2   基本软件2   1                                       1                                        
basic01     basicfun3   基本软件3   1000                                    1000                                                           
basic02     NULL        截止日期    2020-12-05                              2019-12-05                               
basic02     NULL        属性        DEMO, 2020-12-05, 60, NULL, NULL, NULL  DEMO, 2019-12-05, 60, NULL, NULL, NULL   
basic02     basicfun4   基本软件4   1                                       1                                        
basic02     basicfun5   基本软件5   1                                       1                                        
basic02     basicfun6   基本软件6   1000                                    1000                                     
basic02     basicfun7   基本软件7   1000                                    1000                                     
(结果个数 = 14) 

 ---    END 
```

比较3.0版本License：

```
%%CMP LICENSE: CMPTYPE=FILELIC, SRCFN="license_c20_share_20191130.xml", DESFN="license_c20_share_20190601.xml", DSPTYPE=YES;%% 
RETCODE = 0  操作成功  

License名称 
----------- 
第一个License文件名称  =  license_c20_share_20191130.xml 
第二个License文件名称  =  license_c20_share_20190601.xml 
(结果个数 = 1)  

基本信息比较结果 
---------------- 
控制项描述     第一个License的值              第二个License的值 
               
国家           Sweden                         Sweden                          
运营商         Net4Mobility HB                Net4Mobility HB                 
局点           FRSLUNDA                       FRSLUNDA                        
创建者         Huawei Technologies Co., Ltd.  Huawei Technologies Co., Ltd.   
License序列号  LIC201900000XXXXX              LIC2017111601XXXXX              
创建时间       2019-06-05 18:20:57            2012-01-17 18:20:57             
产品           iXXXXX                         iXXXXX                            
设备序列号     0298100810                     0123456789                      
版本           V200R018CXXXXX                 V200R018CXXXXX               
(结果个数 = 9)  

销售项比较结果 
-------------- 
销售项        控制项      控制项描述  第一个License的值  第二个License的值   
 
LT1SRANSAA11  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSAA11  basicres1   NULL        1000               500                 
LT1SRANSAA11  basicres2   NULL        1000               1000                
LT1SRANSAA11  basicfun1   NULL        1                  1                   
LT1SRANSDC09  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSDC09  basicfun1   NULL        1                  1                   
LT1SRANSDC09  basicfun2   NULL        1                  1                   
LT1SRANSDC10  NULL        截止日期    2019-09-30         2019-06-01          
LT1SRANSDC10  basicfun3   NULL        1                  1                   
LT1SRANSDC10  basicfun4   NULL        1                  1                            
(结果个数 = 10)  

---    END 
```

与系统运行中的License比较：

```
%%CMP LICENSE: CMPTYPE=RUNLIC, FN="license_c20_share_20191130.xml", DSPTYPE=YES;%% 
RETCODE = 0  操作成功 
 
License名称 
----------- 
系统运行的License  =  license_c20_share_20191201_50.xml   
  待比较的License  =  license_c20_share_20191130.xml
(结果个数 = 1)
  
基本信息比较结果
---------------- 
控制项描述     系统运行的License的值          待比较的License的值   
           
国家           Sweden                         Sweden                          
运营商         Net4Mobility HB                Net4Mobility HB                 
局点           FRSLUNDA                       FRSLUNDA                        
创建者         Huawei Technologies Co., Ltd.  Huawei Technologies Co., Ltd.   
License序列号  LIC2019000000XXXXX             LIC2017111601XXXXX              
创建时间       2019-06-05 18:20:57            2012-01-17 18:20:57             
产品           iXXXXXXX                       iXXXXX                            
设备序列号     0298100810                     0123456789                      
版本           V200R018CXXXXX                 V200R018CXXXXX               
(结果个数 = 9)  

销售项比较结果 
-------------- 
销售项        控制项      控制项描述  系统运行的License的值  待比较的License的值  
  
KVBS034PVB01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVB01  basicres1   NUll        3000                   50000                 
KVBS034PVB01  basicres2   NUll        3000                   50000                                 
KVBS034PVB01  basicfun1   NUll        1                      1                     
KVBS034PVB01  basicfun2   NUll        1                      1                                    
KVBS034PVC01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVC01  basicres3   NUll        3000                   50000                 
KVBS034PVG01  NULL        截止日期    2019-12-05             2019-12-01            
KVBS034PVG01  basicres4   NUll        3000                   50000                 
KVBS034PVG01  basicres5   NUll        3000                   50000                 
KVBS034PVG01  basicfun3   NUll        1                      1   
(结果个数 = 11)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CMP-LICENSE.md`
