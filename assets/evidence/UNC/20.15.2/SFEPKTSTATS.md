# 清除SFE统计信息（RTR SFEPKTSTATS）

- [命令功能](#ZH-CN_CONCEPT_0000001549961854__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001549961854__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001549961854__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001549961854__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001549961854__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001549961854)

该命令用于命令清除指定资源单元上的SFE统计信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001549961854)

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001549961854)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001549961854)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATISTTYPE | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待清除的SFE内部统计信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fei_packet_count：报文计数。<br>- fei_error_count：错误计数。<br>- fei_event_count：事件计数。<br>默认值：无 |
| STATISTSUBTYPE | 统计子类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATISTTYPE”配置为“fei_packet_count”时为可选参数。<br>参数含义：该参数用于指定待清除的统计信息子类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fei_sub_discard：被SFE丢弃的报文计数。<br>- fei_sub_tocp：准备上送CP的报文计数。<br>- fei_sub_cache：SFE中的报文缓存计数。<br>- fei_sub_in：入SFE报文计数。<br>- fei_sub_out：出SFE报文计数。<br>默认值：无<br>配置原则：如果不设置该参数，则清除所有类型计数。 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001549961854)

清除指定资源单元的被SFE丢弃的报文计数：

```
RTR SFEPKTSTATS:STATISTTYPE=fei_packet_count,STATISTSUBTYPE=fei_sub_discard,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```
