---
id: UNC@20.15.2@MMLCommand@LST NRFCLIENTADDR
type: MMLCommand
name: LST NRFCLIENTADDR（查询NRF实例客户端地址信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFCLIENTADDR
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例客户端地址管理
status: active
---

# LST NRFCLIENTADDR（查询NRF实例客户端地址信息）

## 功能

**适用NF：NRF**

该命令用于查询NRF实例客户端地址信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFCLIENTADDR]] · NRF实例客户端地址信息（NRFCLIENTADDR）

## 使用实例

该命令用于查询NRF实例客户端地址信息。

```
LST NRFCLIENTADDR:;
%%LST NRFCLIENTADDR:;%%
RETCODE = 0  执行成功

结果如下
------------------------
 NRF实例名称  =  nrf1
  IP地址类型  =  IPTypeV4 
    IPV4地址  =  192.168.10.12
    IPV6地址  =  ::
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFCLIENTADDR.md`
