---
id: UNC@20.15.2@MMLCommand@LST PNFSMFINFO
type: MMLCommand
name: LST PNFSMFINFO（查询对端SMF的信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFSMFINFO
command_category: 查询类
applicable_nf:
- AMF
- NCG
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端SMF域名信息管理
status: active
---

# LST PNFSMFINFO（查询对端SMF的信息）

## 功能

**适用NF：AMF、NCG、SMF**

该命令用于查询本地配置的对端SMF支持的PGW域名信息和接入方式等信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSMFINFO]] · 对端SMF的信息（PNFSMFINFO）

## 使用实例

查询对端SMF的信息。

```
%%LST PNFSMFINFO:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = smf_instance_0
     PGW域名 = huawei1.com.epc.mcc308.3gppnetwork.org
    接入类型 = NULL
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFSMFINFO.md`
