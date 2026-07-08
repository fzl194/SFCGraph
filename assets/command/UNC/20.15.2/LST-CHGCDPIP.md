---
id: UNC@20.15.2@MMLCommand@LST CHGCDPIP
type: MMLCommand
name: LST CHGCDPIP（查询计费相关的IP配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHGCDPIP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- CDPIP 配置
status: active
---

# LST CHGCDPIP（查询计费相关的IP配置参数）

## 功能

**适用网元：SGSN**

该命令用于查询CDP进程上所有IP地址。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGCDPIP]] · 计费相关的IP配置参数（CHGCDPIP）

## 使用实例

查询CDP IP地址：

LST CHGCDPIP:;

```
%%LST CHGCDPIP:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
          IP地址类型  =  IPv4地址
            IPv4地址  =  10.141.149.100
          起始端口号  =  3699
          结束端口号  =  3700
             VPN名称  =  a
是否为拨测CDP IP端点  =  否
仍有后续报告输出
---    END
%%LST CHGCDPIP:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
          IP地址类型  =  IPv6地址
            IPv6地址  =  2001:db8:10:19:44:55:10:12
          起始端口号  =  3699
          结束端口号  =  3700
             VPN名称  =  a
是否为拨测CDP IP端点  =  否
(结果个数 = 2)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CHGCDPIP.md`
