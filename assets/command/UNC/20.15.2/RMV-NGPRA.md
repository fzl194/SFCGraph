---
id: UNC@20.15.2@MMLCommand@RMV NGPRA
type: MMLCommand
name: RMV NGPRA（删除5G PRA）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPRA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 网络开放管理
- 5G PRA管理
- 5G PRA标识管理
status: active
---

# RMV NGPRA（删除5G PRA）

## 功能

**适用NF：AMF**

该命令用于删除5G PRA基本信息。

## 注意事项

- 该命令执行后立即生效。

- 在PRA内的所有位置成员都已经删除的情况下，才允许删除PRA基本信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRAID | PRA标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PRA区域的标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是8388608~16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGPRA]] · 5G PRA（NGPRA）

## 使用实例

删除系统中当前配置的标识为16777211的PRA，执行如下命令：

```
RMV NGPRA: PRAID=16777211;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGPRA.md`
