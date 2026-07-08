---
id: UNC@20.15.2@MMLCommand@LST RGRCACT
type: MMLCommand
name: LST RGRCACT（查询RG级异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RGRCACT
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
- RG级结果码处理动作
status: active
---

# LST RGRCACT（查询RG级异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询RG级异常返回码的处理动作配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |
| RCCODE | RG级异常返回码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RG级异常返回码。<br>数据来源：全网规划<br>取值范围：<br>- “DEFAULT（缺省值）”：当收到配置指定之外的结果码时需要执行的动作。<br>- “SERVICEDENIED（因终端用户限制拒绝服务）”：因为终端用户业务限制而拒绝服务。<br>- “QUOTAMNOTAPPL（转离线计费）”：业务不再做配额管理。<br>- “QUOTALIMITRCH（配额不足）”：配额不足。<br>- “SERVICEREJECT（拒绝服务）”：拒绝服务请求，以终止请求信用的服务。<br>- “USERUNKNOWN（未知用户）”：未知用户。<br>- “RATINGFAILED（计费失败）”：计费失败。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [RG级异常返回码处理动作（RGRCACT）](configobject/UNC/20.15.2/RGRCACT.md)

## 使用实例

查询全局融合计费模板的所有RG级异常返回码处理动作：

```
%%LST RGRCACT: CCTMPLTNAME="global";%%
RETCODE = 0  操作成功

结果如下
--------
            融合计费模板名称  =  global
              RG级异常返回码  =  缺省值
          RG级异常返回码动作  =  阻塞业务，后续有Trigger触发时，上报Charging Data Request Update消息
  RG级阻塞处理时间间隔(分钟)  =  0
            RG级重新激活请求  =  不使能
RG级重定向处理重定向IPv4地址  =  0.0.0.0
RG级重定向处理重定向IPv6地址  =  ::
          用户保持时长(分钟)  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RG级异常返回码处理动作（LST-RGRCACT）_09652230.md`
