---
id: UNC@20.15.2@MMLCommand@LST PNFSERVICEVER
type: MMLCommand
name: LST PNFSERVICEVER（查询对端NF的服务实例的版本信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFSERVICEVER
command_category: 查询类
applicable_nf:
- AMF
- NSSF
- SMF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- 对端服务实例版本信息管理
status: active
---

# LST PNFSERVICEVER（查询对端NF的服务实例的版本信息）

## 功能

**适用NF：AMF、NSSF、SMF、SMSF、NCG**

该命令用于查询本地配置的对端NF实例支持的服务实例的版本信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFSERVICEVER]] · 对端NF的服务实例的版本信息（PNFSERVICEVER）

## 使用实例

查询本地配置的对端NF支持的服务实例版本信息。

```
%%LST PNFSERVICEVER:;%%
RETCODE = 0 操作成功

结果如下
------------------------
  NF实例标识 = amf_instance_0
服务实例标识 = Service_Instance_0
APIURI版本号 = v1
 API完整版本 = 1.0.0
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询对端NF的服务实例的版本信息（LST-PNFSERVICEVER）_09653093.md`
