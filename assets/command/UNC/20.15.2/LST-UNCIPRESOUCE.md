---
id: UNC@20.15.2@MMLCommand@LST UNCIPRESOUCE
type: MMLCommand
name: LST UNCIPRESOUCE（查询UNC接口IP地址）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UNCIPRESOUCE
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
- GGSN
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- 北向配置管理
status: active
---

# LST UNCIPRESOUCE（查询UNC接口IP地址）

## 功能

**适用NF：SGSN、MME、SGW-C、PGW-C、AMF、SMF、NRF、NSSF、GGSN、SMSF、NCG**

该命令用于查询已经上报至网管北向的UNC网元业务和管理接口的IP地址。

## 注意事项

当UNC各接口不存在有效IP地址信息时，将生成IP地址为0.0.0.0的无效默认记录，这些默认记录在查询命令结果中不显示。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UNCIPRESOUCE]] · UNC接口IP地址（UNCIPRESOUCE）

## 使用实例

查询已经上报至网管北向的UNC网元业务和管理接口的IP地址，执行以下命令:

```
%%LST UNCIPRESOUCE:;%%
RETCODE = 0  操作成功

结果如下
------------------------
接口类型  IP地址类型  本端IP地址               

N4              IPv4             10.1.3.11                      
N4              IPv6             2001:0DB8::800:200C:510A
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UNCIPRESOUCE.md`
