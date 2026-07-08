---
id: UNC@20.15.2@MMLCommand@RMV SMSCHRPRCTMPL
type: MMLCommand
name: RMV SMSCHRPRCTMPL（删除SMS CHR流程控制模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSCHRPRCTMPL
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# RMV SMSCHRPRCTMPL（删除SMS CHR流程控制模板）

## 功能

**适用NF：SMSF**

该命令用于删除SMS CHR流程控制模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TMPLIDX | 流程控制模板索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示流程控制模板索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SMS CHR流程控制模板（SMSCHRPRCTMPL）](configobject/UNC/20.15.2/SMSCHRPRCTMPL.md)

## 使用实例

运营商希望删除“流程控制模板索引”为“1”的SMS CHR流程控制模板，执行如下命令：

```
RMV SMSCHRPRCTMPL: TMPLIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SMS-CHR流程控制模板（RMV-SMSCHRPRCTMPL）_53481542.md`
