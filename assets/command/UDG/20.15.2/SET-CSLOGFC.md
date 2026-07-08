---
id: UDG@20.15.2@MMLCommand@SET CSLOGFC
type: MMLCommand
name: SET CSLOGFC（设置日志流控开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CSLOGFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# SET CSLOGFC（设置日志流控开关）

## 功能

![](设置日志流控开关（SET CSLOGFC）_09587953.assets/notice_3.0-zh-cn.png)

当日志级别为ERR以下时，关闭日志流控，会造成CPU升高，可能触发进程复位，导致业务呼损等严重后果，不建议操作。

此命令用于设置日志流控开关。

日志流控是指同一文件同一行的日志在1分钟之内打印数量不能超过10条，超过10条将进行流控，同一文件同一行的日志不进行打印。

> **说明**
> - 该命令执行后立即生效。
>
> - 日志流控只流控ERR级别以下的日志。在流控开关关闭时，不进行流控，此时如果日志级别调整为ERR以下，可能会导致CPU和内存升高。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH |
> | --- |
> | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示日志流控开关。<br>数据来源：本端规划<br>取值范围：<br>- “ON（打开）”：打开流控开关<br>- “OFF（关闭）”：关闭流控开关<br>默认值：无。<br>配置原则：<br>业务同一文件同一行日志打印1分钟内打印频繁，业务需要进行减少重复日志的日志量时需要打开流控开关。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CSLOGFC]] · 日志流控开关（CSLOGFC）

## 使用实例

启动日志流控功能：

```
SET CSLOGFC: FCSWITCH=ON;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CSLOGFC.md`
