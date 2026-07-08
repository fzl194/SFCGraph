---
id: UNC@20.15.2@MMLCommand@LST LOCALUDMINSTID
type: MMLCommand
name: LST LOCALUDMINSTID（查询本省UDM实例标识）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCALUDMINSTID
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 基于IMSI号段的QoS管理
- 本省UDM实例标识
status: active
---

# LST LOCALUDMINSTID（查询本省UDM实例标识）

## 功能

**适用NF：SMF**

该命令用于查询本省UDM实例标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UDMINSTID | UDM实例标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UDM实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。UDMINSTID参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。3.不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALUDMINSTID]] · 本省UDM实例标识（LOCALUDMINSTID）

## 使用实例

查询本省UDM实例标识。

```
%%LST LOCALUDMINSTID: ;%%
RETCODE = 0  操作成功

结果如下
---------
UDM实例标识  =  udm_instance_0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCALUDMINSTID.md`
