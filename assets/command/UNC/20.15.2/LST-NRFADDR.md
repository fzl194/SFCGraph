---
id: UNC@20.15.2@MMLCommand@LST NRFADDR
type: MMLCommand
name: LST NRFADDR（查询NRF实例地址信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFADDR
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
- CBCF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NRF管理
- NRF地址管理
- NRF实例地址管理
status: active
---

# LST NRFADDR（查询NRF实例地址信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF**

该命令用于查询NRF实例地址信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFADDR]] · NRF实例地址信息（NRFADDR）

## 使用实例

该命令用于查询NRF实例地址信息。

```
%%LST NRFADDR:;%%
RETCODE = 0  操作成功

结果如下
--------
NRF实例名称  =  NRF_Instance_0
 IP地址类型  =  IPTypeV4
   IPV4地址  =  192.168.0.1
   IPV6地址  =  ::
       端口  =  8081
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFADDR.md`
