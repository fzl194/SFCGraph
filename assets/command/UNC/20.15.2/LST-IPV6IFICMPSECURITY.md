---
id: UNC@20.15.2@MMLCommand@LST IPV6IFICMPSECURITY
type: MMLCommand
name: LST IPV6IFICMPSECURITY（查询接口下安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6IFICMPSECURITY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- 接口下IPv6安全配置
status: active
---

# LST IPV6IFICMPSECURITY（查询接口下安全配置）

## 功能

该命令用于查询接口下安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6IFICMPSECURITY]] · 接口下安全配置（IPV6IFICMPSECURITY）

## 使用实例

查询接口下安全配置：

```
LST IPV6IFICMPSECURITY:IFNAME="Ethernet65/0/8";
```

```

RETCODE = 0  操作成功。

结果如下
--------
        接口名  =  Ethernet65/0/8
  发送还是接收  =  发送报文
    配置的类型  =  报文类型
      报文类型  =  端口不可达
收发报文的TYPE  =  1
收发报文的CODE  =  4
          开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询接口下安全配置（LST-IPV6IFICMPSECURITY）_49801466.md`
