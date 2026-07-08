---
id: UNC@20.15.2@MMLCommand@LST PDPAPN
type: MMLCommand
name: LST PDPAPN（查询本地APN NI配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDPAPN
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地APNNI管理
status: active
---

# LST PDPAPN（查询本地APN NI配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询指定用户PDP类型与APN NI地址的映射关系。

UNC 中一次激活场景和MME中PDN连接建立场景，用户匹配到野卡或者匹配到多组签约数据时，需要根据IMSI和PDP/PDN类型查询本地的APN NI。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定签约用户的范围。<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “IMSI_RANGE(指定IMSI范围)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：系统根据该参数值对用户的IMSI进行匹配，从而区分不同的用户群<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据<br>“IMSI前缀 ”<br>、<br>“PDP/PDN类型”<br>映射唯一的<br>“APN NI”<br>。 |
| IMSI | IMSI | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定所要查询的IMSI。<br>前提条件：该参数在<br>“用户范围”<br>参数设置为<br>“IMSI_RANGE(指定IMSI范围)”<br>时，才需要配置。<br>取值范围：1～15位数字<br>默认值：无<br>说明：根据<br>“IMSI ”<br>、<br>“PDP/PDN类型”<br>映射唯一的<br>“APN NI”<br>。 |
| PDPTYPE | PDP/PDN类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDP类型。<br>取值范围：<br>- “PT_IPV4(IPV4协议)”：表示用户激活的PDP类型为IPV4协议。<br>- “PT_IPV6(IPV6协议)”：表示用户激活的PDP类型为IPV6协议。<br>- “PT_PPP(点对点通信协议)”：表示用户激活的PDP类型为点对点通信协议。<br>- “PT_IPV4_IPV6(IPV4和IPV6协议)”：表示用户激活的PDP类型为IPV4和IPV6协议。<br>- “PT_ALL(所有类型)”：表示用户激活的PDP类型为所有类型，不包含Non-IP类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDPAPN]] · 本地APN NI配置（PDPAPN）

## 使用实例

查询所有记录

LST PDPAPN:;

```
%%LST PDPAPN:;%%
RETCODE = 0  操作成功。

查询结果如下
--------------
   用户范围  =  指定IMSI前缀
   IMSI前缀  =  11111111
PDP/PDN类型  =  IPV4协议
     APN NI  =  2222
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDPAPN.md`
