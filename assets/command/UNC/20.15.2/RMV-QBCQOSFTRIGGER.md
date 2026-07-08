---
id: UNC@20.15.2@MMLCommand@RMV QBCQOSFTRIGGER
type: MMLCommand
name: RMV QBCQOSFTRIGGER（删除QBC计费QoS Flow级的trigger参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QBCQOSFTRIGGER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费QoS Flow级Trigger
status: active
---

# RMV QBCQOSFTRIGGER（删除QBC计费QoS Flow级的trigger参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除QBC计费QoS Flow级的trigger参数。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 默认记录不可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定融合计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QBCQOSFTRIGGER]] · QBC计费QoS Flow级的trigger参数（QBCQOSFTRIGGER）

## 使用实例

删除绑定名称为“test”的CCT融合计费模板的QBC计费QoS Flow级的trigger参数。

```
RMV QBCQOSFTRIGGER: CCTMPLTNAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除QBC计费QoS-Flow级的trigger参数（RMV-QBCQOSFTRIGGER）_09653273.md`
