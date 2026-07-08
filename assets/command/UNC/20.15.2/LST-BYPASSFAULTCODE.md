---
id: UNC@20.15.2@MMLCommand@LST BYPASSFAULTCODE
type: MMLCommand
name: LST BYPASSFAULTCODE（查询BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BYPASSFAULTCODE
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- Bypass故障状态码管理
status: active
---

# LST BYPASSFAULTCODE（查询BYPASS故障状态码）

## 功能

**适用NF：AMF、SMF**

该命令用于查询BYPASS故障状态码。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端网元类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端网元类型。<br>数据来源：全网规划<br>取值范围：<br>- “UDM（UDM）”：UDM<br>- “AUSF（AUSF）”：AUSF<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | 网元实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成或者配置为通配符（*）。该参数不区分大小写。配置为“*”时，表示针对所有的网元实例生效，如果用户所在的网元实例标识在配置表中无法匹配到对应的记录，则使用“*”对应的记录。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BYPASSFAULTCODE]] · BYPASS故障状态码（BYPASSFAULTCODE）

## 使用实例

若查询网元类型为UDM、网元实例标识为instanceid01的BYPASS故障状态码配置，执行如下命令：

```
%%LST BYPASSFAULTCODE: PEERNFTYPE=UDM, NFINSTANCEID="instanceid01";%%
RETCODE = 0  操作成功

结果如下
--------
 对端网元类型  =  UDM
 网元实例标识  =  instanceid01
 自定义故障码  =  504|509|602
     错误信息  =  NF_FAILOVER
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BYPASSFAULTCODE.md`
