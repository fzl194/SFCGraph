---
id: UNC@20.15.2@MMLCommand@DSP RAWIPSTATUS
type: MMLCommand
name: DSP RAWIPSTATUS（查询RawIP状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RAWIPSTATUS
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

# DSP RAWIPSTATUS（查询RawIP状态）

## 功能

该命令用于查看RawIP连接状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SOCKETFD | Socket实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147418111。<br>默认值：无 |
| APPCID | APP组件CID | 可选必选说明：可选参数<br>参数含义：该参数用于指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| LOCALADDRESS | 本端地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESS | 远端地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RAWIPSTATUS]] · RawIP状态（RAWIPSTATUS）

## 使用实例

显示当前系统的RawIP状态：

```
DSP RAWIPSTATUS:;
```

```

        RETCODE = 0  操作成功

        结果如下
        ------------------------
        Socket实例ID  =  8
          APP组件CID  =  0x8069042E
            本端地址  =  0.0.0.0
            远端地址  =  0.0.0.0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RAWIPSTATUS.md`
