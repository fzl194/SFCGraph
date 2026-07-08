---
id: UNC@20.15.2@MMLCommand@RMV N40UPFIDINUUID
type: MMLCommand
name: RMV N40UPFIDINUUID（删除N40接口非UUID格式与UUID格式的UPF实例标识的映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: N40UPFIDINUUID
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 全局配置
status: active
---

# RMV N40UPFIDINUUID（删除N40接口非UUID格式与UUID格式的UPF实例标识的映射关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除N40接口非UUID格式与UUID格式的UPF实例标识的映射关系。

## 注意事项

- 该命令执行后立即生效。

- 该命令对存量融合计费用户存在影响，可能导致SMF或CHF无法处理映射过的UPF实例标识的消息，建议无融合计费用户时使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~18。UPFINSTANCEID参数必须满足以下约束规则：1. 非UUID格式，不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF。2. 不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40UPFIDINUUID]] · N40接口非UUID格式与UUID格式的UPF实例标识的映射关系（N40UPFIDINUUID）

## 使用实例

删除N40接口非UUID格式"upfinstance1"与UUID格式“00000000-0000-0000-0000-000000000001”的UPF实例标识的映射关系：

```
RMV N40UPFIDINUUID:UPFINSTANCEID="upfinstance1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除N40接口非UUID格式与UUID格式的UPF实例标识的映射关系（RMV-N40UPFIDINUUID）_70462601.md`
