---
id: UNC@20.15.2@MMLCommand@LST GTPCWHITELIST
type: MMLCommand
name: LST GTPCWHITELIST（查询GTP-C路径白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCWHITELIST
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径白名单
status: active
---

# LST GTPCWHITELIST（查询GTP-C路径白名单）

## 功能

**适用网元：MME**

本命令用于查询GTP-C路径白名单。

输出结果将IPv4和IPv6分成2个报表显示，并按“接口类型”（第一优先级）、“对端IP地址”（第二优先级）、“本端IP地址”（第三优先级）进行排序。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCWHITELIST]] · GTP-C路径白名单（GTPCWHITELIST）

## 使用实例

查询GTP-C路径白名单：

LST GTPCWHITELIST:;

```
%%LST GTPCWHITELIST:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
    接口类型 = Sv
  IP地址类型 = IPV4
本端IPv4地址 = 192.168.3.4
对端IPv4地址 = 192.168.4.5
        描述 = NULL    

仍有后续报告输出
---    END
```

```
%%LST GTPCWHITELIST:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
    接口类型 = Sv
  IP地址类型 = IPV6
本端IPv6地址 = 2001:db8:10:19:44:55:10:12
对端IPv6地址 = 2001:db8:10:19:44:55:10:13
        描述 = NULL    
(结果个数 = 2)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTPCWHITELIST.md`
