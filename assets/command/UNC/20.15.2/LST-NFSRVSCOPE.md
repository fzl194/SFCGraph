---
id: UNC@20.15.2@MMLCommand@LST NFSRVSCOPE
type: MMLCommand
name: LST NFSRVSCOPE（查询NF支持服务区信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFSRVSCOPE
command_category: 查询类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 服务区管理
status: active
---

# LST NFSRVSCOPE（查询NF支持服务区信息）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于查询NF实例支持的服务区信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NF支持服务区信息（NFSRVSCOPE）](configobject/UNC/20.15.2/NFSRVSCOPE.md)

## 使用实例

运营商A需要查询NF实例支持的服务区信息。

```
%%LST NFSRVSCOPE:;%%
RETCODE = 0  操作成功

结果如下
--------
NF实例名称  =  AMF_Instance_0
服务区名称  =  CityA
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF支持服务区信息（LST-NFSRVSCOPE）_16634738.md`
