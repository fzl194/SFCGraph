---
id: UNC@20.15.2@MMLCommand@RMV NGAPPARA
type: MMLCommand
name: RMV NGAPPARA（删除NGAP协议参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGAPPARA
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- NGAP协议参数管理
status: active
---

# RMV NGAPPARA（删除NGAP协议参数）

## 功能

**适用NF：AMF**

该命令用于删除NGAP协议参数配置。

## 注意事项

- 该命令执行后立即生效。

- 不允许删除NGAP协议参数索引为0的默认配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPPARAIDX | NGAP协议参数索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NGAP参数配置的索引。唯一表示一个NGAP实体的参数配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGAPPARA]] · NGAP协议参数（NGAPPARA）

## 使用实例

删除索引值为1的NGAP接口协议控制参数，执行如下命令：

```
RMV NGAPPARA: NGAPPARAIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGAPPARA.md`
