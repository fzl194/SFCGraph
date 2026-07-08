---
id: UNC@20.15.2@MMLCommand@RMV UECAPBYIMSI
type: MMLCommand
name: RMV UECAPBYIMSI（删除UE无线能力策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UECAPBYIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- UE无线能力策略
status: active
---

# RMV UECAPBYIMSI（删除UE无线能力策略）

## 功能

**适用网元：MME**

此命令用于删除UE无线能力策略 。

## 注意事项

- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI。<br>数据来源：整网规划<br>取值范围：14～15位的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UECAPBYIMSI]] · UE无线能力策略（UECAPBYIMSI）

## 使用实例

删除一条UE无线能力策略， “IMSI” 为 “460011418603055” ：

```
RMV UECAPBYIMSI: IMSI="460011418603055";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UECAPBYIMSI.md`
