---
id: UDG@20.15.2@MMLCommand@RTR HEADENRATTYPE
type: MMLCommand
name: RTR HEADENRATTYPE（恢复头增强RAT类型定义）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: HEADENRATTYPE
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 头增强控制
- 头增强RAT类型
status: active
---

# RTR HEADENRATTYPE（恢复头增强RAT类型定义）

## 功能

**适用NF：PGW-U、UPF**

该命令用于恢复头增强全局参数默认值，初始化RAT类型设置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATTYPEVALUE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个RAT类型，查询其相应字符串的值。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- RESERVED：预留RAT类型。<br>- UTRAN：无线接入类型为UMTS陆地无线接入网。<br>- GERAN：无线接入类型为GSM/EDGE无线接入网。<br>- WLAN：无线接入类型为无线局域网。<br>- GAN：无线接入类型为通用接入网络。<br>- HSPAE：无线接入类型为增强型高速分组接入。<br>- EUTRAN：无线接入类型为演进UMTS陆地无线接入网。<br>- VIRTUAL：无线接入类型为Virtual。<br>- EUTRANNBIOT：无线接入类型为EUTRAN-NB-IoT。<br>- LTEM：无线接入类型为LTE-M。<br>- NR：无线接入类型为NR。<br>- REDCAPNR：无线接入类型为RedCap-NR。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HEADENRATTYPE]] · 头增强RAT类型定义（HEADENRATTYPE）

## 使用实例

假如运营商希望恢复无线接入类型为WLAN的头增强参数默认值WLANSTR，可以通过该命令恢复该无线接入类型的头增强参数默认值：

```
RTR HEADENRATTYPE:RATTYPEVALUE=WLAN;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/恢复头增强RAT类型定义（RTR-HEADENRATTYPE）_86527135.md`
