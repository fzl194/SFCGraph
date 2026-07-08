---
id: UNC@20.15.2@MMLCommand@DSP IFIPV6CGA
type: MMLCommand
name: DSP IFIPV6CGA（显示IPv6 CGA地址信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IFIPV6CGA
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6 CGA地址配置
status: active
---

# DSP IFIPV6CGA（显示IPv6 CGA地址信息）

## 功能

该命令用于显示IPv6 CGA地址状态信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址CGA动态信息的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFIPV6CGA]] · IPv6 CGA地址信息（IFIPV6CGA）

## 使用实例

显示接口IPv6 CGA信息：

```
DSP IFIPV6CGA:IFNAME="ethernet64/0/3";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  接口名  =  Ethernet64/0/3
密钥名称  =  aa
安全级别  =  高
修正地址  =  2001:db8::1
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IPv6-CGA地址信息（DSP-IFIPV6CGA）_00441249.md`
