---
id: UNC@20.15.2@MMLCommand@RMV NFGROUP
type: MMLCommand
name: RMV NFGROUP（删除NF组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NFGROUP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF实例组信息管理
status: active
---

# RMV NFGROUP（删除NF组）

## 功能

**适用NF：NRF**

该命令用于删除NRF上配置的NF实例组信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFGROUPID | NF实例组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示在NRF上配置的NF实例组的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。该参数只能由字母（A-Z或者a-z）、数字（0-9），中划线（-）组成，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NF组（NFGROUP）](configobject/UNC/20.15.2/NFGROUP.md)

## 使用实例

在NRF上删除NF标识为nfgroup001的实例组：

```
RMV NFGROUP:NFGROUPID="nfgroup001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除NF组（RMV-NFGROUP）_09652193.md`
