---
id: UNC@20.15.2@MMLCommand@ADD UECAPBYIMSI
type: MMLCommand
name: ADD UECAPBYIMSI（增加UE无线能力策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UECAPBYIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- UE无线能力策略
status: active
---

# ADD UECAPBYIMSI（增加UE无线能力策略）

## 功能

**适用网元：MME**

此命令用于增加UE无线能力策略， 配置IMSI后，会强制保存UE Radio Capability信元。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为64条。
- 此命令功能生效后，被强制保存的UE Radio Capability信元长度受如下软参影响：BYTE_EX_B113 BIT3、BYTE_EX_B107 BIT4、BYTE_EX_B51 BIT4、DWORD_EX40 BIT19、BYTE_EX20 BIT5。

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

增加一条UE无线能力策略， “IMSI” 为 “460011418603055” ：

```
ADD UECAPBYIMSI: IMSI="460011418603055";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-UECAPBYIMSI.md`
