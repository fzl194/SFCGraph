---
id: UNC@20.15.2@MMLCommand@RMV NGEMGCFG
type: MMLCommand
name: RMV NGEMGCFG（删除运营商紧急呼叫功能配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGEMGCFG
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- 紧急呼叫业务管理
- 紧急呼叫配置
status: active
---

# RMV NGEMGCFG（删除运营商紧急呼叫功能配置）

## 功能

**适用NF：AMF**

该命令用于删除指定的MNO或MVNO对应的紧急呼叫配置数据。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [运营商紧急呼叫功能配置（NGEMGCFG）](configobject/UNC/20.15.2/NGEMGCFG.md)

## 使用实例

删除“运营商标识”为“0”的运营商紧急呼叫功能的配置，执行如下命令：

```
RMV NGEMGCFG: NOID=0;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除运营商紧急呼叫功能配置（RMV-NGEMGCFG）_09652963.md`
