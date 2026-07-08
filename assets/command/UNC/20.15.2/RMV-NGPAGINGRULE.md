---
id: UNC@20.15.2@MMLCommand@RMV NGPAGINGRULE
type: MMLCommand
name: RMV NGPAGINGRULE（删除5G寻呼规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPAGINGRULE
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP接口寻呼管理
- NG寻呼规则管理
status: active
---

# RMV NGPAGINGRULE（删除5G寻呼规则）

## 功能

**适用NF：AMF**

此命令用于删除全部或者指定的5G寻呼规则。

## 注意事项

- 该命令执行后立即生效。

- 在不指定规则索引参数的情况下，执行本命令将删除所有已配置的5G寻呼规则，从而导致精准寻呼功能不可用，请慎重操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEIDX | 规则索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G寻呼规则的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPAGINGRULE]] · 5G寻呼规则（NGPAGINGRULE）

## 使用实例

删除一条“规则索引”为“1”的5G寻呼规则，执行如下命令：

```
RMV NGPAGINGRULE: RULEIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGPAGINGRULE.md`
