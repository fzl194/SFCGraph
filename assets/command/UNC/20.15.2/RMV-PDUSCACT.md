---
id: UNC@20.15.2@MMLCommand@RMV PDUSCACT
type: MMLCommand
name: RMV PDUSCACT（删除PDU异常返回码动作）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PDUSCACT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- PDU级结果码处理动作
status: active
---

# RMV PDUSCACT（删除PDU异常返回码动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除PDU异常返回码动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| CODETYPE | 返回码类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PDU异常返回码类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（针对未指定的异常返回码设置处理动作）”：当收到配置指定之外的结果码时需要执行的动作<br>- “VALUE（针对指定异常返回码设置处理动作）”：当收到配置指定的结果码时需要执行的动作<br>默认值：无<br>配置原则：无 |
| STATUSCODE | 状态码 | 可选必选说明：该参数在"CODETYPE"配置为"VALUE"时为条件必选参数。<br>参数含义：该参数用于配置PDU级异常状态返回码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，65535。<br>默认值：无<br>配置原则：<br>返回码500,502,504,601,602,603,605的默认动作为FAILOVER。<br>返回码604的默认动作需参考ADD CCT命令中FHACTION的动作，FHACTION为CONTINUE时，604的默认动作为CONTINUE，其余情况的默认动作为TERM_WITH_REL。<br>内部异常码606默认动作：主备Chf在同一个SCP组时，动作同604，否则，默认动作为FAILOVER。<br>其他返回码的默认动作为TERM_WITH_REL。<br>异常码604/605，内部异常码606动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 上述的默认动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。<br>其他异常码动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PDUSCACT]] · PDU异常返回码动作（PDUSCACT）

## 使用实例

删除模板"test"的PDU异常返回码300的动作配置。

```
RMV PDUSCACT: CCTMPLTNAME="test", CODETYPE=VALUE, STATUSCODE=300;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PDUSCACT.md`
