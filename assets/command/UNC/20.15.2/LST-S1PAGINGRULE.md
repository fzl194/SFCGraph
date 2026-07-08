---
id: UNC@20.15.2@MMLCommand@LST S1PAGINGRULE
type: MMLCommand
name: LST S1PAGINGRULE（查询S1寻呼规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1PAGINGRULE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1寻呼规则管理
status: active
---

# LST S1PAGINGRULE（查询S1寻呼规则）

## 功能

**适用网元：MME**

此命令用于查询系统中全部或者指定条件的S1寻呼规则。查询结果按 “匹配优先级” 排序后显示。

## 注意事项

- 此命令执行后立即生效。
- 当不指定任何条件时，表示查询系统中所有的S1寻呼规则；否则按照输入的条件查询指定的S1寻呼规则。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECID | 规则索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的索引。<br>取值范围：1～1001<br>默认值：无<br>说明：- 当执行[**ADD S1PAGINGRULE**](增加S1寻呼规则(ADD S1PAGINGRULE)_26306058.md)命令增加S1寻呼规则时，系统会自动为该规则分配一个1～1001之间未使用的最小的索引，以唯一的标识该S1寻呼规则。可以在不输入“规则索引”时，执行本命令查询系统分配的索引值。<br>- 因为“规则索引”唯一的标识一条S1寻呼规则，故执行本命令时，如果指定了“规则索引”，建议不用再指定其它的查询条件。 |
| GRPTYPE | 用户群类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的用户群类型。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “MSISDN_PREFIX(指定MSISDN前缀)”<br>- “IMEI_TAC(指定IMEI TAC)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的IMSI前缀。<br>前提条件：该参数在<br>“用户群类型”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才生效。<br>取值范围：1～15位十进制数字串<br>默认值：无 |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的MSISDN前缀。<br>前提条件：该参数在<br>“用户群类型”<br>参数设置为<br>“MSISDN_PREFIX(指定MSISDN前缀)”<br>时，才生效。<br>取值范围：1～15位十进制数字串<br>默认值：无 |
| IMEITAC | IMEI TAC | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的IMEI TAC。<br>前提条件：该参数在<br>“用户群类型”<br>参数设置为<br>“IMEI_TAC(指定IMEI TAC)”<br>时，才生效。<br>取值范围：位数为8的十进制数字<br>默认值：无 |
| SVRTYPE | 业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的业务类型。<br>取值范围：<br>- “S11_DOWNLINK(下行数据触发)”：表示由S11接口的下行业务（包含DDN或者CBR/UBR消息）触发的寻呼。<br>- “SGS_PAGING(SGs寻呼触发)”：表示由SGs接口的CS Call、SMS等业务触发的寻呼。<br>- “S102_PAGING(S102寻呼触发)”：表示由S102接口的CS Call、SMS等业务触发的寻呼。<br>- “S6A_IDR_PAGING(S6a接口IDR寻呼触发)”：表示由S6a接口的实时位置查询或状态查询业务触发的寻呼。<br>- “OTHER(其它)”：表示由其它业务触发的寻呼，如LCS等。<br>默认值：无 |
| PRIORITY | 匹配优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的S1寻呼规则的匹配优先级。<br>取值范围：0～255<br>默认值：无 |
| ACTGRP | 寻呼动作组合 | 可选必选说明：可选参数<br>参数含义：该参数用于指定寻呼规则使用的寻呼动作组合。<br>取值范围：<br>- LAST_ENODEB(最近访问eNodeB)<br>- NEIGH_ENODEB(邻接eNodeB)<br>- LAST_TAI(最近访问TA)<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1PAGINGRULE]] · S1寻呼规则（S1PAGINGRULE）

## 使用实例

查询一条 “规则索引” 为 “1” 的S1寻呼规则：

LST S1PAGINGRULE: RECID=1;

```
%%LST S1PAGINGRULE: RECID=1;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
       规则索引  =  1
     用户群类型  =  所有用户
       IMSI前缀  =  NULL
     MSISDN前缀  =  NULL
       IMEI TAC  =  NULL
       业务类型  =  S6a接口IDR寻呼触发
        APN指示  =  NULL
     移动国家码  =  NULL
       移动网号  =  NULL
         APN NI  =  NULL
          QCI值  =  NULL
      ARP优先级  =  NULL
SGs接口业务指示  =  NULL
       消息类型  =  CBR/UBR & DDN
     匹配优先级  =  200
   寻呼动作组合  =  最近访问TA
       规则描述  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1寻呼规则(LST-S1PAGINGRULE)_72225927.md`
