---
id: UNC@20.15.2@MMLCommand@LST ACCESSLISTIP
type: MMLCommand
name: LST ACCESSLISTIP（查询黑白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACCESSLISTIP
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 黑白名单地址列表
status: active
---

# LST ACCESSLISTIP（查询黑白名单）

## 功能

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来查询黑白名单配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACCESSLISTIP]] · 黑白名单（ACCESSLISTIP）

## 使用实例

显示黑白名单配置：

```
%%LST ACCESSLISTIP:;%%
RETCODE = 0 操作成功
结果如下
IP地址版本类型            IPV4地址       掩码长度       IPV6地址               掩码长度

 IPv4                    10.10.10.10       27          ::                     128 
 IPv4                    10.0.0.0          11          ::                     128
 IPv6                    255.255.255.255   32          2001:db8               32
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ACCESSLISTIP.md`
