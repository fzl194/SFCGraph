---
id: UDG@20.15.2@MMLCommand@LST DNSIPRESOURCE
type: MMLCommand
name: LST DNSIPRESOURCE（查询DNS IP地址资源列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNSIPRESOURCE
command_category: 查询类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- IP资源管理
status: active
---

# LST DNSIPRESOURCE（查询DNS IP地址资源列表）

## 功能

**适用NF：CloudEPSN**

该命令用于查询DNS的管理接口和业务接口IP地址资源信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DNSIPRESOURCE]] · DNS IP地址资源列表（DNSIPRESOURCE）

## 使用实例

查询IP地址资源信息：

```
+++    CloudEPSN/*MEID:0 MENAME:APP-VNF-CloudEPSN-X86-B003_IP60*/        2024-02-20 13:05:02
O&M    #3699
%%LST DNSIPRESOURCE:;
```

```
%%
RETCODE = 0  操作成功

结果如下
--------
接口类型  IP地址类型  IPv4地址列表             IPv6地址列表             

Dns       IPv4        192.168.0.1,192.168.0.2  NULL  
Mgt       IPv4和IPv6  NULL                     NULL                     
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DNSIPRESOURCE.md`
