# 设置NAS兼容性参数（SET NASCMPT）

- [命令功能](#ZH-CN_MMLREF_0000001158192283__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001158192283__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001158192283__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001158192283__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001158192283)

**适用NF：AMF**

该命令用于为NAS（Non-Access-Stratum protocol）设置兼容性控制参数。NAS是AMF与UE之间的应用协议，通过本命令可以控制AMF是否在该协议层的下行消息中携带指定的可选信元。

## [注意事项](#ZH-CN_MMLREF_0000001158192283)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NASMSGTYPE | SNDREJNS |
| --- | --- |
| REGISTRATION_REJECT | NO |

#### [操作用户权限](#ZH-CN_MMLREF_0000001158192283)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001158192283)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NASMSGTYPE | NAS消息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NAS消息类型，根据消息类型来确认是否需要配置相应的消息接口兼容性。<br>数据来源：全网规划<br>取值范围：<br>- “REGISTRATION_REJECT（注册拒绝消息）”：AMF发给UE的注册拒绝消息。<br>默认值：无。<br>配置原则：无 |
| SNDREJNS | 是否携带拒绝切片信元 | 可选必选说明：该参数在"NASMSGTYPE"配置为"REGISTRATION_REJECT"时为条件可选参数。<br>参数含义：该参数用于控制AMF是否在给UE下发的Registration Reject消息中携带Rejected NSSAI信元。<br>数据来源：全网规划<br>取值范围：<br>- “NO（否）”：否<br>- “YES（是）”：是<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NASCMPT查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001158192283)

当用户无网络切片原因导致注册拒绝时，设置AMF在注册拒绝消息中携带拒绝切片列表，让用户知道拒绝切片的内容，执行如下命令：

```
SET NASCMPT:NASMSGTYPE=REGISTRATION_REJECT,SNDREJNS=YES;
```
