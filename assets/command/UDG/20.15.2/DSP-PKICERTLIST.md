---
id: UDG@20.15.2@MMLCommand@DSP PKICERTLIST
type: MMLCommand
name: DSP PKICERTLIST（显示证书列表）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PKICERTLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 公钥基础设施
- 查询证书列表
status: active
---

# DSP PKICERTLIST（显示证书列表）

## 功能

该命令用于显示证书列表。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILETYPE | 文件类型 | 可选必选说明：可选参数<br>参数含义：文件类型。<br>数据来源：本端规划<br>取值范围：<br>- “CA（CA证书）”：CA证书<br>- “LOCAL（本地证书）”：本地证书<br>默认值：无<br>配置原则：无 |
| FILENAME | 文件名称 | 可选必选说明：可选参数<br>参数含义：文件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |
| PODNAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PKICERTLIST]] · 证书列表（PKICERTLIST）

## 使用实例

显示证书列表：

```
DSP PKICERTLIST:;
RETCODE = 0  操作成功

结果如下
-------------------------
    文件类型  =  本地证书
    文件名称  =  ee1.cer
    Pod名称  =  ipsecexec-pod-0192-168-1-1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示证书列表（DSP-PKICERTLIST）_30311459.md`
