---
id: UNC@20.15.2@MMLCommand@LST UPLOADBALANCE
type: MMLCommand
name: LST UPLOADBALANCE（查询UP负载均衡功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPLOADBALANCE
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
- 会话管理
- 接入管理
- UPF选择管理
- UPF负载均衡
status: active
---

# LST UPLOADBALANCE（查询UP负载均衡功能）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询UP负载均衡功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPLOADBALANCE]] · UP负载均衡功能（UPLOADBALANCE）

## 使用实例

查询UNC的UP负载均衡功能。

```
%%LST UPLOADBALANCE:;%%
RETCODE = 0  操作成功

结果如下
----------------
UNC支持处理UPF上报的LCI  =  关闭处理LCI功能
          UPF轻负载门限  =  45
          UPF重负载门限  =  75
UNC支持处理UPF上报的OCI  =  关闭处理OCI功能
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPLOADBALANCE.md`
