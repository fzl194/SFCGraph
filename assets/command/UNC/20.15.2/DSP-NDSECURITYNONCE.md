---
id: UNC@20.15.2@MMLCommand@DSP NDSECURITYNONCE
type: MMLCommand
name: DSP NDSECURITYNONCE（查询ND安全随机数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NDSECURITYNONCE
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

# DSP NDSECURITYNONCE（查询ND安全随机数）

## 功能

该命令用于显示ND安全的随机数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NDSECURITYNONCE]] · ND安全随机数（NDSECURITYNONCE）

## 使用实例

显示ND安全随机数：

```
DSP NDSECURITYNONCE:IFNAME="Ethernet65/0/8";
```

```

        RETCODE = 0  操作成功
        结果如下
        -------------------------
        IPv6地址  =  2001:db8::11
          随机数  =  1500
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NDSECURITYNONCE.md`
