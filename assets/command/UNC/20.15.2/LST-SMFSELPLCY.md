---
id: UNC@20.15.2@MMLCommand@LST SMFSELPLCY
type: MMLCommand
name: LST SMFSELPLCY（查询SMF选择策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFSELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF选择策略管理
status: active
---

# LST SMFSELPLCY（查询SMF选择策略）

## 功能

**适用NF：AMF**

该命令用于查询SMF的选择策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用SMF选择策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户<br>- “HOME_USER（本网用户）”：本网用户<br>- “FOREIGN_USER（外网用户）”：外网用户<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀<br>默认值：无<br>配置原则：<br>对于指定的用户（群），SMF选择策略的匹配优先级从高到低依次为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”，“ALL_USER(所有用户)”。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定应用SMF选择策略的用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFSELPLCY]] · SMF选择策略（SMFSELPLCY）

## 使用实例

- 查询当前配置的SMF选择策略，执行如下命令：
  ```
  %%LST SMFSELPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                           用户范围  =  所有用户
                                           IMSI前缀  =  NULL
                                        DNN群组标识  =  NULL
                              是否携带Serving Scope  =  No
                                           服务范围  =  NULL
                                  是否支持I-SMF选择  =  否
                                        是否使用TAI  =  否
                                   是否使用用户IMSI  =  否
                                     是否使用MSISDN  =  否
                              融合SMF/PGW-C选择条件  =  NULL
                                        是否重选SMF  =  是
                                    优选同一SMF开关  =  否
                                            DNN格式  =  默认方式
                            签约信息中的SMF选择策略  =  默认
                     EPS与5GS互操作专用切片选择策略  =  签约方式
                     EPS与5GS互操作专用切片业务类型  =  0
                     EPS与5GS互操作专用切片细分标识  =  FFFFFF
                                          I-SMF重选  =  默认模式
                                  4到5切换I-SMF重选  =  默认模式
                            签约信息中的相同SMF指示  =  否			 
                                ISMF场景相同SMF开关  =  是			 
                                VSMF场景相同SMF开关  =  是
                                         V-SMF重选   =  默认模式
                                  4到5切换V-SMF重选  =  默认模式
                              Preferred TAI功能开关  =  否  
                                漫游用户是否使用TAI  =  是
                                漫游用户DNN群组标识  =  1
                             是否携带IsmfSupportInd  =  否
  Home Routed国际漫游选择H-SMF是否携带Serving Scope  =  否
           Home Routed国际漫游场景下H-SMF的服务范围  =  NULL
                 Home Routed国际漫游用户DNN群组标识  =  NULL
                                           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询当前配置“用户范围”为“本网用户”的SMF选择策略，执行如下命令：
  ```
  %%LST SMFSELPLCY: SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                           用户范围  =  本网用户
                                           IMSI前缀  =  NULL
                                        DNN群组标识  =  NULL
                              是否携带Serving Scope  =  No
                                           服务范围  =  NULL
                                  是否支持I-SMF选择  =  否
                                        是否使用TAI  =  否
                                   是否使用用户IMSI  =  否
                                     是否使用MSISDN  =  否
                              融合SMF/PGW-C选择条件  =  NULL
                                        是否重选SMF  =  是
                                    优选同一SMF开关  =  否
                                            DNN格式  =  默认方式
                            签约信息中的SMF选择策略  =  默认
                     EPS与5GS互操作专用切片选择策略  =  签约方式
                     EPS与5GS互操作专用切片业务类型  =  0
                     EPS与5GS互操作专用切片细分标识  =  FFFFFF
                                          I-SMF重选  =  默认模式
                                  4到5切换I-SMF重选  =  默认模式
                            签约信息中的相同SMF指示  =  否			 
                                ISMF场景相同SMF开关  =  是			 
                                VSMF场景相同SMF开关  =  是
                                         V-SMF重选   =  默认模式
                                  4到5切换V-SMF重选  =  默认模式
                              Preferred TAI功能开关  =  否
                                漫游用户是否使用TAI  =  否
                                漫游用户DNN群组标识  =  NULL
                             是否携带IsmfSupportInd  =  否
  Home Routed国际漫游选择H-SMF是否携带Serving Scope  =  否
           Home Routed国际漫游场景下H-SMF的服务范围  =  NULL
                 Home Routed国际漫游用户DNN群组标识  =  NULL
                                           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFSELPLCY.md`
