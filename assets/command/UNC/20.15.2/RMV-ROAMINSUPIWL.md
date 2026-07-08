---
id: UNC@20.15.2@MMLCommand@RMV ROAMINSUPIWL
type: MMLCommand
name: RMV ROAMINSUPIWL（删除漫入场景SUPI白名单）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ROAMINSUPIWL
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# RMV ROAMINSUPIWL（删除漫入场景SUPI白名单）

## 功能

**适用NF：NRF**

该命令用于删除漫入场景SUPI白名单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGSTART | 号段起始字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的起始号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |
| SEGEND | 号段结束字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示号段的结束号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ROAMINSUPIWL]] · 漫入场景SUPI白名单（ROAMINSUPIWL）

## 使用实例

删除漫入场景SUPI白名单，号段起始字符串123456789876501，号段结束字符串123456789876505：

```
RMV ROAMINSUPIWL: SEGSTART="123456789876501", SEGEND="123456789876505";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ROAMINSUPIWL.md`
