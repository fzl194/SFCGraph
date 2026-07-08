---
id: UNC@20.15.2@MMLCommand@LST PDUSCACT
type: MMLCommand
name: LST PDUSCACT（查询PDU异常返回码动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PDUSCACT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- PDU级结果码处理动作
status: active
---

# LST PDUSCACT（查询PDU异常返回码动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询PDU异常返回码动作。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| CODETYPE | 返回码类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDU异常返回码类型。<br>数据来源：本端规划<br>取值范围：<br>- “DEFAULT（针对未指定的异常返回码设置处理动作）”：当收到配置指定之外的结果码时需要执行的动作<br>- “VALUE（针对指定异常返回码设置处理动作）”：当收到配置指定的结果码时需要执行的动作<br>默认值：无<br>配置原则：无 |
| STATUSCODE | 状态码 | 可选必选说明：该参数在"CODETYPE"配置为"VALUE"时为条件可选参数。<br>参数含义：该参数用于配置PDU级异常状态返回码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是300~999，65535。<br>默认值：无<br>配置原则：<br>返回码500,502,504,601,602,603,605的默认动作为FAILOVER。<br>返回码604的默认动作需参考ADD CCT命令中FHACTION的动作，FHACTION为CONTINUE时，604的默认动作为CONTINUE，其余情况的默认动作为TERM_WITH_REL。<br>内部异常码606默认动作：主备Chf在同一个SCP组时，动作同604，否则，默认动作为FAILOVER。<br>其他返回码的默认动作为TERM_WITH_REL。<br>异常码604/605，内部异常码606动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 上述的默认动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。<br>其他异常码动作优先级：通过命令ADD PDUSCACT中的参数SCACT配置的异常码动作 > 通过命令ADD PDUSCACT中参数CODETYPE配置的DEFAULT动作 > 未配置的异常码默认动作。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PDUSCACT]] · PDU异常返回码动作（PDUSCACT）

## 使用实例

查询CCT模板名称为"test"的PDU异常返回码配置。

```
%%LST PDUSCACT: CCTMPLTNAME="test";%%
RETCODE = 0  操作成功

结果如下
--------
融合计费模板名称  =  test
      返回码类型  =  针对指定异常返回码设置处理动作
          状态码  =  300
        处理动作  =  阻塞业务，使业务不能继续进行
  重定向IPV4地址  =  0.0.0.0
  重定向IPV6地址  =  ::
阻塞处理时间间隔  =  30
   原因值GtpV0-1  =  0
     原因值GtpV2  =  0
    重新激活请求  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PDUSCACT.md`
