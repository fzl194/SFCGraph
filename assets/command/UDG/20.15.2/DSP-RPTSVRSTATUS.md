---
id: UDG@20.15.2@MMLCommand@DSP RPTSVRSTATUS
type: MMLCommand
name: DSP RPTSVRSTATUS（查询报表服务器状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RPTSVRSTATUS
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器地址
status: active
---

# DSP RPTSVRSTATUS（查询报表服务器状态）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询报表服务器状态。

## 注意事项

使用ADD RPTSVR添加报表服务器时，当RPTSVRTYPE配置为SUBSCRIPTION，可查询到该链路状态，不受SVRFUNC参数控制。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTSVRSTATUS]] · 报表服务器状态（RPTSVRSTATUS）

## 使用实例

假如运营商需要查询报表服务器状态：

```
DSP RPTSVRSTATUS:;
```

```

RETCODE = 0 操作成功

报表服务器状态信息
------------------
报表容器名称    接入点名称    链路状态      IPv4地址       IPv6地址  报表服务器名称   VPN实例名称    端口号       IP类型    报表消息类型
rpt-pod-1       access01      normal       192.168.0.1    ::        und01            test_vpn       10700        IPV4        UFDR     
rpt-pod-1       access02      abnormal     192.168.0.10   ::        und02            test_vpn       10700        IPV4        ADR      
rpt-pod-0       access01      normal       192.168.0.1    ::        und01            test_vpn       10700        IPV4        SUBSCRIPTION     
rpt-pod-0       access02      abnormal     192.168.0.10   ::        und02            test_vpn       10700        IPV4        BASIC

(结果个数 = 4)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RPTSVRSTATUS.md`
