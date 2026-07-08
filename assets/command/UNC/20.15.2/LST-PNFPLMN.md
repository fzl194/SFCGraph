---
id: UNC@20.15.2@MMLCommand@LST PNFPLMN
type: MMLCommand
name: LST PNFPLMN（查询对端NF的PLMN信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PNFPLMN
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
- 对端NF实例PLMN管理
status: active
---

# LST PNFPLMN（查询对端NF的PLMN信息）

## 功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG**

该命令用于查询本地配置对端NF实例支持的PLMN的信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PNFPLMN]] · 对端NF的PLMN信息（PNFPLMN）

## 使用实例

查询对端NF的PLMN信息。

```
%%LST PNFPLMN:;%%
RETCODE = 0 操作成功

结果如下
---------
  NF实例标识 = udm_instance_0
  移动国家码 = 460
    移动网号 = 03
  NF Set ID = 123
（结果个数 = 1）

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PNFPLMN.md`
