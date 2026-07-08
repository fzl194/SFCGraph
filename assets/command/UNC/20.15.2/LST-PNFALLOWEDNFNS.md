---
id: UNC@20.15.2@MMLCommand@LST PNFALLOWEDNFNS
type: MMLCommand
name: LST PNFALLOWEDNFNS（查询对端NF允许的切片信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFALLOWEDNFNS
command_category: 查询类
applicable_nf:
- AMF
- SMF
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
- 本地NRF功能管理
- 对端NF服务切片信息管理
status: active
---

# LST PNFALLOWEDNFNS（查询对端NF允许的切片信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询对端NF服务支持的允许访问的切片信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFALLOWEDNFNS]] · 对端NF允许的切片信息（PNFALLOWEDNFNS）

## 使用实例

查询对端NF支持的切片信息。

```
%%LST PNFALLOWEDNFNS:;%%
RETCODE = 0 操作成功

结果如下
------------------------
   NF实例标识 = smf_instance_0
 服务实例标识 = service_instance_0
切片/服务类型 = 1
  切片区分码 = 010101
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFALLOWEDNFNS.md`
