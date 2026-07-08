---
id: UNC@20.15.2@MMLCommand@LST CPGTPUADDR
type: MMLCommand
name: LST CPGTPUADDR（查询CP GTP-U地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPGTPUADDR
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- N4 GTP-U地址管理
status: active
---

# LST CPGTPUADDR（查询CP GTP-U地址）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询与UPF对接的用户面本端地址。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定与UPF对接的本端GTP-U IP地址类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPGTPUADDR]] · CP GTP-U地址（CPGTPUADDR）

## 使用实例

查询所有与UPF对接的本端GTP-U地址：

```
%%LST CPGTPUADDR:;%%
RETCODE = 0  操作成功

结果如下
------------------------
IP地址类型  =  IPv4
  IPv4地址  =  192.168.0.20
  IPv6地址  =  ::
   VPN名称  =  _public_
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CPGTPUADDR.md`
