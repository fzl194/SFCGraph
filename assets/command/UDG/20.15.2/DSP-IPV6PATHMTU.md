---
id: UDG@20.15.2@MMLCommand@DSP IPV6PATHMTU
type: MMLCommand
name: DSP IPV6PATHMTU（显示IPv6 Path MTU配置）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPV6PATHMTU
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 Path MTU
status: active
---

# DSP IPV6PATHMTU（显示IPv6 Path MTU配置）

## 功能

该命令用于显示IPv6路径MTU。

若不指定VRFNAME时，则显示本节点公网接口路径MTU信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| IPV6DSTADDR | IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPV6PATHMTU]] · IPv6 Path MTU配置（IPV6PATHMTU）

## 使用实例

显示IPv6 Path MTU：

```
DSP IPV6PATHMTU:VRFNAME="_public_";
```

```

       RETCODE = 0  操作成功。

   结果如下
   --------
               VPN名称  =  _public_
              IPv6地址  =  2001:db8::11
       路径MTU（byte）  =  1500
   表项超时时间（min）  =  NULL
           路径MTU类型  =  静态
              分片标记  =  0
  (结果个数 = 1)
   ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示IPv6-Path-MTU配置（DSP-IPV6PATHMTU）_00841589.md`
