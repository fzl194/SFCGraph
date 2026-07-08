---
id: UNC@20.15.2@MMLCommand@RMV NRFGROUP
type: MMLCommand
name: RMV NRFGROUP（删除对端NRF实例组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFGROUP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例组管理
status: active
---

# RMV NRFGROUP（删除对端NRF实例组）

## 功能

**适用NF：NRF**

当运营商不再需要原规划的NRF实例组时，可以使用此命令。该命令用于删除对端NRF实例组。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | 实例组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，不能以“.”开始，也不能以“.”结束。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFGROUP]] · 对端NRF实例组（NRFGROUP）

## 使用实例

当不再需要实例组名称为nrfgroup001的NRF实例组时，执行此命令。

```
RMV NRFGROUP: GROUPNAME="nrfgroup001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFGROUP.md`
