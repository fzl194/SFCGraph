---
id: UDG@20.15.2@MMLCommand@DSP IPPATH
type: MMLCommand
name: DSP IPPATH（查询PP4路径信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPPATH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- PP4
status: active
---

# DSP IPPATH（查询PP4路径信息）

## 功能

该命令用于查询PP4路径信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CID | 组件CID | 可选必选说明：可选参数<br>参数含义：该参数用来显示PP4组件的CID，可通过DSP COMPONENT查询。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPPATH]] · PP4路径信息（IPPATH）

## 使用实例

查询PP4路径信息：

```
DSP IPPATH: CID="0x80660014";
```

```

RETCODE = 0  操作成功。

结果如下
--------
显示索引    路径ID      组件PID     组件CID       路径状态    路径中断原因    路径优先级    下个PID       下个段      VPN实例ID    发送标志    扩展标志    实例标志    源地址         目的地址       接口索引    指定接口    下一跳     隧道类型    隧道ID    XC索引    主标志    路径子状态

1           4           0x660015    0x80660014    3           0               1             0x660015      67109224    0            5           0           0           192.168.2.1    192.168.2.2    8           0           0.0.0.0    0           0         0         0         0
2           3           0x660015    0x80660014    3           0               1             0x660015      67109221    0            5           0           0           192.168.1.1    192.168.1.2    6           0           0.0.0.0    0           0         0         0         0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PP4路径信息（DSP-IPPATH）_49801906.md`
