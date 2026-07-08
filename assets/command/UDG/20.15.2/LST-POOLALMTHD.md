---
id: UDG@20.15.2@MMLCommand@LST POOLALMTHD
type: MMLCommand
name: LST POOLALMTHD（查询本地指定地址池占用率告警阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: POOLALMTHD
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务告警管理
- 指定地址池占用率告警阈值
status: active
---

# LST POOLALMTHD（查询本地指定地址池占用率告警阈值）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询本地指定地址池使用率的告警阈值和告警恢复阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLNAME | 地址池名称 | 可选必选说明：可选参数<br>参数含义：地址池的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：此参数必须是ADD POOL已配置的地址池名称。 |

## 操作的配置对象

- [本地指定地址池占用率告警阈值（POOLALMTHD）](configobject/UDG/20.15.2/POOLALMTHD.md)

## 使用实例

显示本地地址池使用率的告警阈值和告警恢复阈值：

```
LST POOLALMTHD:;
```

```

RETCODE = 0  操作成功。

地址池占用率告警阈值
--------------------
地址池名                   =  pool1
告警产生阈值（%）           =  80
告警恢复阈值（%）           =  70
指定地址池告警阈值配置开关   =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询本地指定地址池占用率告警阈值（LST-POOLALMTHD）_88368925.md`
