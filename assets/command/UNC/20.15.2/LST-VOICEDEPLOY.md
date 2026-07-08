---
id: UNC@20.15.2@MMLCommand@LST VOICEDEPLOY
type: MMLCommand
name: LST VOICEDEPLOY（查询语音部署配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VOICEDEPLOY
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 语音业务管理
status: active
---

# LST VOICEDEPLOY（查询语音部署配置）

## 功能

**适用网元：MME**

该命令用于查询UE使用E-UTRAN网络接入时的IMS VoPS语音部署方案配置。UE使用E-UTRAN网络接入时可以选择两种语音部署方案：

- IMS VoPS（IMS Voice over PS session），即基于IMS网络提供语音业务。PS网络上部署专门的IMS APNNI，用于承载IMS业务相关的信令和数据。
- CSFB（Circuit Switched Fallback），利用现有的GSM /UMTS网络实现语音通话的一种语音解决方案。用户进行语音业务时，由EPS（Evolved Packet System）网络指示用户回落到目标GSM/UMTS电路域（CS）网络之后，再发起语音呼叫。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>取值范围：<br>- “ALL_USER（所有用户）”<br>- “HOME_USER（本网用户）”<br>- “FOREIGN_USER（外网用户）”<br>- “IMSI_PREFIX（指定IMSI前缀）”<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：<br>- 该参数在“SUBRANGE（用户范围）”配置为“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”后生效。<br>取值范围：0～64，128～254<br>默认值：无<br>说明：- 如果不输入该参数，系统会查询所有的“SUBRANGE（用户范围）”配置为“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”记录。<br>- NOID未配置时，显示为255 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。<br>前提条件：此参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>时有效。<br>取值范围：1～15位十进制数字字符串<br>默认值：无<br>说明：如果不输入该参数，系统会查询所有“SUBRANGE（用户范围）”配置为“IMSI_PREFIX（指定IMSI前缀）”的配置记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VOICEDEPLOY]] · 语音部署配置（VOICEDEPLOY）

## 使用实例

场景参见 [**ADD VOICEDEPLOY**](增加语音部署配置(ADD VOICEDEPLOY)_72345361.md) 的命令使用实例。

- 查询本网用户语音部署配置：
  LST VOICEDEPLOY: SUBRANGE=HOME_USER;
  ```
  %%LST VOICEDEPLOY:SUBRANGE=HOME_USER;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
                       用户范围  =  本网用户
                     运营商标识  =  0
                       IMSI前缀  =  NULL
                       IMS VoPS  =  是
                IMS APN网络标识  =  NULL
                       终端类型  =  Voice Centric
   禁止特征RFSP用户使用IMS VoPS  =  否
                   特征RFSP索引  =  NULL
                   基于IMEI控制  =  白名单
                   IMEI群组标识  =  1
  CS Fallback not preferred指示  =  是
  (结果个数 = 1)
  ---   END
  ```
- 查询所有语音部署配置：
  LST VOICEDEPLOY:;
  ```
  %%LST VOICEDEPLOY:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
   用户范围  运营商标识  IMSI前缀  IMS VoPS  IMS APN网络标识  终端类型       禁止特征RFSP用户使用IMS VoPS  特征RFSP索引  基于IMEI控制  IMEI群组标识  CS Fallback not preferred指示

   本网用户  0           NULL      是        NULL             Voice Centric  否                            NULL          白名单        1             是                           
   外网用户  0           NULL      是        NULL             Voice Centric  否                            NULL          否            NULL          是                           
  (结果个数 = 2)
  ---   END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VOICEDEPLOY.md`
