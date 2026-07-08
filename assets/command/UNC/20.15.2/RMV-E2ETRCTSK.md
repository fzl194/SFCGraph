---
id: UNC@20.15.2@MMLCommand@RMV E2ETRCTSK
type: MMLCommand
name: RMV E2ETRCTSK（删除端到端跟踪任务）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: E2ETRCTSK
command_category: 配置类
applicable_nf:
- AMF
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# RMV E2ETRCTSK（删除端到端跟踪任务）

## 功能

**适用NF：AMF、MME**

该命令用于删除端到端跟踪任务。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCTSK]] · 端到端跟踪任务（E2ETRCTSK）

## 使用实例

删除端到端跟踪任务，删除“SUPI”为“460123456789000”的端到端跟踪任务，执行如下命令：

```
RMV E2ETRCTSK: IMSI="460123456789000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-E2ETRCTSK.md`
