---
id: UDG@20.15.2@MMLCommand@ADD TOPOLICYCFG
type: MMLCommand
name: ADD TOPOLICYCFG（增加TCP优化策略配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TOPOLICYCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
max_records: 7
category_path:
- TCP优化服务管理
- TCP策略配置
status: active
---

# ADD TOPOLICYCFG（增加TCP优化策略配置）

## 功能

**适用NF：UPF**

该命令用于增加TCP优化策略配置,实现基于小区/IMSI/RAT类型的TCP优化参数定制化功能。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为7。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYID | 策略ID | 可选必选说明：必选参数<br>参数含义：策略ID。<br>数据来源：本端规划<br>取值范围：整数类型,取值范围为1~7。<br>默认值：无<br>配置原则：无 |
| CCALG | TCP拥塑控制算法 | 可选必选说明：必选参数<br>参数含义：设置TCP拥塑控制算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- CUBIC：CCALG_CUBIC。<br>- MW3：CCALG_MW3。<br>- BIC：CCALG_BIC。<br>- BBR：CCALG_BBR。<br>- EBBR：CCALG_EBBR。<br>默认值：无<br>配置原则：无 |
| RCVBUF | 接收缓存区大小 | 可选必选说明：可选参数<br>参数含义：用于设置为TCP Socket预留的接收缓存大小。<br>数据来源：本端规划<br>取值范围：整数类型,取值范围4096~31457280。<br>默认值：无<br>配置原则：无 |
| SNDBUF | 发送缓存区大小 | 可选必选说明：可选参数<br>参数含义：用于设置为TCP Socket预留的发送缓存大小。<br>数据来源：本端规划<br>取值范围：整数类刑,取值范围为4096~31457280。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TCP优化策略配置（TOPOLICYCFG）](configobject/UDG/20.15.2/TOPOLICYCFG.md)

## 使用实例

运营商需要增加一个策略ID为1,拥塞控制算法为EBBR的TCP优化策略配置：

```
ADD TOPOLICYCFG: POLICYID=1,CCALG=EBBR;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加TCP优化策略配置（ADD-TOPOLICYCFG）_86856890.md`
