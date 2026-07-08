---
id: UDG@20.15.2@MMLCommand@DSP RAWLINKSTATUS
type: MMLCommand
name: DSP RAWLINKSTATUS（查询Raw-link状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RAWLINKSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SOCKET
status: active
---

# DSP RAWLINKSTATUS（查询Raw-link状态）

## 功能

该命令用于查看Raw-link连接状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPCID | APP组件CID | 可选必选说明：可选参数<br>参数含义：该参数用于指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SOCKETFD | Socket实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147418111。<br>默认值：无 |

## 操作的配置对象

- [Raw-link状态（RAWLINKSTATUS）](configobject/UDG/20.15.2/RAWLINKSTATUS.md)

## 使用实例

显示当前系统的Raw-link状态：

```
DSP RAWLINKSTATUS:;
```

```

        RETCODE = 0  操作成功

        结果如下
        --------------------------
        APP组件CID    Socket实例ID

        0x807703FD    1
        0x8069042E    2
        0x8069042E    3
        0x8069042E    4
        0x807703FD    6
        0x8069042E    7
        (结果个数 = 6)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Raw-link状态（DSP-RAWLINKSTATUS）_00866625.md`
