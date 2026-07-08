---
id: UNC@20.15.2@MMLCommand@DSP NDSECURITYTIMESTAMP
type: MMLCommand
name: DSP NDSECURITYTIMESTAMP（查询ND安全时间戳）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDSECURITYTIMESTAMP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND安全
status: active
---

# DSP NDSECURITYTIMESTAMP（查询ND安全时间戳）

## 功能

该命令用于显示ND安全时间戳。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NDSECURITYTIMESTAMP]] · ND安全时间戳（NDSECURITYTIMESTAMP）

## 使用实例

显示ND安全时间戳：

```
DSP NDSECURITYTIMESTAMP:IFNAME="Ethernet65/0/8";
```

```

        RETCODE = 0  操作成功
        结果如下
        -------------------------
                                IPv6地址  =  2001:db8::11
        接收的上一个SEND报文中的时间戳值  =  1500
           接收上一个SEND报文的时间（s）  =  1500
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NDSECURITYTIMESTAMP.md`
